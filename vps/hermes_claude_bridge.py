#!/usr/bin/env python3
"""
Hermes <-> Claude command bridge.

Polls the hermes_tasks table in StaffHub Supabase (same DB-mediated control
pattern as bot_control) and executes tasks written by the Claude CEO session.
Results (exit code, stdout, stderr) are written back to the same row, giving
Claude full command access to the Hermes VPS with a complete audit trail.

Runs as whatever user starts it (recommended: yasir). Every task is recorded
permanently in hermes_tasks — nothing executes without a row to show for it.

Env (reuses what hermes-agent already has):
  SUPABASE_URL          e.g. https://hvlwtpedsioogfguleon.supabase.co
  SUPABASE_SERVICE_KEY  service role key (RLS bypass; keep on VPS only)

Usage:
  python3 hermes_claude_bridge.py            # poll forever (systemd)
  python3 hermes_claude_bridge.py --once     # single poll cycle (cron/testing)
"""

import os
import subprocess
import sys
import time
from datetime import datetime, timezone

import requests

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://hvlwtpedsioogfguleon.supabase.co")
SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
POLL_SECONDS = 20
MAX_OUTPUT = 50_000  # chars kept per stream

S = requests.Session()
S.headers.update({
    "apikey": SERVICE_KEY,
    "Authorization": f"Bearer {SERVICE_KEY}",
    "Content-Type": "application/json",
})
REST = f"{SUPABASE_URL}/rest/v1/hermes_tasks"


def now():
    return datetime.now(timezone.utc).isoformat()


def claim_next():
    """Atomically claim the oldest pending task (claim wins only if still pending)."""
    r = S.get(REST, params={
        "status": "eq.pending",
        "order": "created_at.asc",
        "limit": "1",
        "select": "id,task_type,command,timeout_seconds,title",
    }, timeout=30)
    r.raise_for_status()
    rows = r.json()
    if not rows:
        return None
    task = rows[0]
    r = S.patch(
        REST,
        params={"id": f"eq.{task['id']}", "status": "eq.pending"},
        json={"status": "running", "claimed_at": now()},
        headers={"Prefer": "return=representation"},
        timeout=30,
    )
    r.raise_for_status()
    return task if r.json() else None  # empty -> someone else claimed it


def finish(task_id, **fields):
    fields["finished_at"] = now()
    S.patch(REST, params={"id": f"eq.{task_id}"}, json=fields, timeout=30).raise_for_status()


def run_task(task):
    ttype = task.get("task_type", "shell")
    if ttype == "ping":
        finish(task["id"], status="done", exit_code=0,
               stdout=f"pong from {os.uname().nodename} at {now()}")
        return
    if ttype != "shell" or not task.get("command"):
        finish(task["id"], status="error", stderr=f"unsupported task_type={ttype} or empty command")
        return
    timeout = min(int(task.get("timeout_seconds") or 300), 3600)
    try:
        p = subprocess.run(
            task["command"], shell=True, capture_output=True, text=True, timeout=timeout,
        )
        finish(task["id"],
               status="done" if p.returncode == 0 else "error",
               exit_code=p.returncode,
               stdout=p.stdout[-MAX_OUTPUT:],
               stderr=p.stderr[-MAX_OUTPUT:])
    except subprocess.TimeoutExpired as e:
        finish(task["id"], status="error", exit_code=-1,
               stdout=(e.stdout or "")[-MAX_OUTPUT:] if isinstance(e.stdout, str) else "",
               stderr=f"timeout after {timeout}s")
    except Exception as e:  # report, never crash the bridge
        finish(task["id"], status="error", stderr=repr(e)[:2000])


def cycle():
    task = claim_next()
    if task:
        print(f"[{now()}] running task {task['id']}: {task.get('title') or task.get('command', '')[:80]}")
        run_task(task)
        return True
    return False


if __name__ == "__main__":
    if "--once" in sys.argv:
        while cycle():
            pass
        sys.exit(0)
    print(f"[{now()}] hermes_claude_bridge started, polling every {POLL_SECONDS}s")
    while True:
        try:
            while cycle():
                pass
        except Exception as e:
            print(f"[{now()}] poll error: {e!r}", file=sys.stderr)
        time.sleep(POLL_SECONDS)
