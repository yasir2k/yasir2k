# Hermes ⟷ Claude command bridge — 5-minute install

This makes Hermes a commandable employee of the Claude CEO session: Claude writes
tasks into the `hermes_tasks` table in StaffHub Supabase; this runner executes
them on the VPS and writes results back. Same pattern as `bot_control`, with a
full audit trail (every command + output stays in the table).

## Install (on the Hermes VPS, as user `yasir`)

```bash
# 1. Get the script (pull this repo, or copy vps/hermes_claude_bridge.py manually)
mkdir -p ~/hermes-deployment/claude-bridge
cp hermes_claude_bridge.py ~/hermes-deployment/claude-bridge/

# 2. Env — reuse the same Supabase service key hermes-agent already uses
#    (check: grep -r SUPABASE ~/hermes-deployment/hermes-agent/.env* )
cat > ~/hermes-deployment/claude-bridge/.env <<'EOF'
SUPABASE_URL=https://hvlwtpedsioogfguleon.supabase.co
SUPABASE_SERVICE_KEY=<paste service role key>
EOF
chmod 600 ~/hermes-deployment/claude-bridge/.env

# 3. Run as a systemd service
sudo tee /etc/systemd/system/hermes-claude-bridge.service <<'EOF'
[Unit]
Description=Hermes-Claude command bridge
After=network-online.target

[Service]
User=yasir
EnvironmentFile=/home/yasir/hermes-deployment/claude-bridge/.env
ExecStart=/usr/bin/python3 /home/yasir/hermes-deployment/claude-bridge/hermes_claude_bridge.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload && sudo systemctl enable --now hermes-claude-bridge
```

## Verify

A `ping` task is already queued. Within ~20s of the service starting it should
flip to `done` with "pong from <hostname>". Claude checks this from its side; you
can also check in Supabase: `select * from hermes_tasks order by created_at desc;`

## Security notes

- `hermes_tasks` has RLS enabled: only the service key (VPS) and authenticated
  StaffHub users can read/write it. The anon key is locked out.
- Commands run as user `yasir` with that user's permissions.
- Everything is auditable in the table — nothing executes without a row.
- To pause Claude's access: `sudo systemctl stop hermes-claude-bridge`.
