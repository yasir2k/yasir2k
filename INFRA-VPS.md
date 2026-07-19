# MD / Hermes VPS — Infrastructure Reference

*Captured 2026-07-19. The host runs MD (Hermes Agent) + the SEO/forecast/e-com pipelines. Source of truth for "how big is the box" so we stop guessing.*

| Attribute | Value |
|---|---|
| Hostname | `ubuntu-2gb-ash-1` *(legacy name — box was resized; it is NOT 2GB)* |
| Provider / region | Hetzner Cloud, Ashburn (ash) |
| Public IP | `5.161.202.190` |
| SSH user | `yasir` |
| OS | Ubuntu 24.04.4 LTS (kernel 6.8.0) |
| **CPU** | **2 vCPU** — AMD EPYC-Milan (1 core × 2 threads) |
| **RAM** | **7.6 GiB (~8 GB)** — typically ~4.5 GiB available |
| **Swap** | 2 GB (swapfile) |
| **Disk** | **38 GB total, ~86% used, ~5.4 GB free** ⚠️ watch this |
| GPU | none |
| Python | 3.12.3 (system) · Hermes venv 3.11 |
| Node | v22.22.2 |
| Hermes Agent | v0.18.2 (build 2026.7.7.2) |
| Uptime (at capture) | 36 days, load ~0.03 (near-idle) |

### Practical implications
- **Concurrency:** 8GB comfortably runs 2–3 concurrent `hermes -z` agent runs (each DeepSeek/API-bound, a few hundred MB). No need to serialize small fan-outs. CPU is only 2 vCPU, so heavy parallel *compute* (not our agents' bottleneck) would contend.
- **Disk at 86%** is the real constraint to watch — the `weekly-snapshots`/report files, model caches, and logs grow. A `VPS Disk Watchdog` cron already exists (every 240m). If it alerts, prune caches/logs.
- **Model/provider:** MD runs DeepSeek `deepseek-v4-pro` (OpenAI-compatible SDK) via `.venv/bin/hermes`. Keys in `~/hermes-deployment/claude-bridge/integrations.env` and `~/.hermes/.env`.
- **Reaching MD:** shell bridge = Supabase `hermes_tasks` (project `hvlwtpedsioogfguleon`); live agent = `~/hermes-deployment/hermes-agent/.venv/bin/hermes -z "<prompt>" --provider deepseek -m deepseek-v4-pro --yolo` (nohup for long runs); passive digest = `~/.hermes/inbox/`.
