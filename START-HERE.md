# START HERE — Saddlery Inc. CEO Session Handoff

*Read this first. It's the single entry point to resume without re-deriving anything. Last updated 2026-07-19 by the CEO session (Opus 4.8). When you finish reading, you are the acting **CEO of Saddlery Inc.** — continue the initiatives below.*

> **To start a new session and pick up where we left off:** open a new Claude Code session on this repo (`yasir2k/yasir2k`) and make your **first message**:
> *"You are the acting CEO of Saddlery Inc. Read START-HERE.md and the docs it links, then continue."*
> The repo is cloned fresh into every session, so this file + all the docs below travel with you. Live state also lives in Supabase `ceo_progress_reports` and MD's memory — check the latest `/progress` entry for anything newer than this file's date.

---

## 1. The business (30-second brief)
- **Saddlery Inc.** — ~$6M western tack & saddlery. Brands: **Hilason** (primary), Uhorse, BarH Equine, American Darling.
- Channels: **Amazon ~69%** (was declining ~22%/yr — the core crisis), **Shopify DTC ~22%** (hilason.com), eBay + in-store the rest.
- **Turnaround thesis:** demand was never *bought* or *owned* — no ads, no email until mid-2026. Fix = **buy demand profitably** (Amazon ads ✓, Google ads = in progress) + **own the audience** (email ✓) + **earn organic** (SEO ✓).
- You act as **CEO**: strategy + decisions; delegate ops to **MD** (the autonomous agent) and the pipelines. Model: Opus 4.8. Yasir = the owner.

## 2. Read-order doc index (all in repo root)
| Doc | What's in it |
|---|---|
| **`SADDLERY-CEO-GAMEPLAN.md`** | The master turnaround gameplan / strategy. |
| **`MISSION-CONTROL-OPS.md`** | StaffHub / Mission Control ops, the data pipelines, how the machine runs. |
| **`EMAIL-FLOWS.md`** | Klaviyo email program (popup, Welcome, Abandoned Cart, Post-Purchase, Win-back). |
| **`GOOGLE-ADS-BRIEF.md`** | Google Ads initiative background + plan (see §3 for the big update since). |
| **`WINTER-BLANKETS-STRATEGY.md`** | Seasonal cross-channel plan to rank winter turnout blankets top-of-page (Amazon/Google/eBay), competitor-grounded. |
| **`INFRA-VPS.md`** | The MD/Hermes VPS specs (2 vCPU, ~8GB RAM, 38GB disk @86%). |

## 3. Current state of every initiative (as of 2026-07-19)

### Email / Klaviyo — LIVE
On-brand newsletter popup live on hilason.com (code `FIRSTRIDE`, double opt-in). **5 flows live** (Welcome, Abandoned Cart, Thank-You, Post-Purchase, Review); Win-back held for deliverability. ~211+ signups. Company id `Sd8MeD`, Newsletter list `XyprBz`. **Open:** verify Klaviyo↔Shopify server-side events (Placed Order / Checkout Started) actually flow so Abandoned Cart can fire — Shopify was reintegrated 07-16.

### SEO / Google organic — LIVE & working
Pipeline (agent1–6 + SEO Judge) optimizing product pages (2,405 done) + publishing buyer's-guide content. **Measurable lift:** GSC clicks +35% and avg position 21→~18 over 6 weeks. The turnout-blankets collection page is already excellently optimized.

### Amazon — LIVE (ads) + winter build in progress
Amazon ads running profitably (~7× ROAS; ~13% ACOS). We **dominate fly sheets** (#1–2). DataDoe MCP manages it. Seller IDs in §5.

### Google Ads — DISCOVERED, PAUSED, partially blocked
**Big finding (07-17):** the "new" account was actually Hilason's **legacy 18-year-old account** (CID `839-426-3831`, sales@hilason.com, $160K lifetime) left running on autopilot by departed agency **Netelixr** — 5 live campaigns spending ~$1,484/mo. **MD paused all 5** (leak stopped). Billing is healthy (no debt). A **daily billing watchdog** now alerts on any new spend/re-enable (cron, 8AM CT → Telegram). **BLOCKED:** removing Netelixr's 2 manager-account links (CIDs `2218652780`, `4131958774`) + the temp user, and creating any new campaigns, needs **Basic API access** (current token is Explorer-tier). → **Yasir clears this Tue Jul 21 in Houston** (manual UI removal, ~5 min, or apply for Basic access).

### Winter turnout blankets — STRATEGY DONE, IMPLEMENTATION RUNNING
See `WINTER-BLANKETS-STRATEGY.md`. Two MD tasks launched 07-19 (**in flight** — reports land at `~/.hermes/inbox/reports/winter-seo-setup.md` and `winter-amazon-setup.md`):
1. **SEO:** rebuild the size-chart page (#1 rank, 0 clicks → capture ~1,540 impr), add temp/fill table to collection, build content cluster.
2. **Amazon/eBay:** optimize winter ASINs (400g-led titles/bullets/keywords), stage a **paused** Sponsored campaign, eBay item specifics.
Differentiator to lead with everywhere: **400g heavyweight fill + belly-wrap + western colorways.** Inventory in transit, lands **early August** → throttle paid to stock arrival.

### Reporting — automated
**Weekly Hilason snapshot** cron (`hilason-weekly-snapshot`, Mondays 8AM CT → Telegram): SEO + sales + email trend. First real numbers showed **organic-search DTC revenue ~5×'d WoW**. Daily progress logged to Supabase `ceo_progress_reports`.

## 4. Open items needing Yasir
1. **Tue Jul 21 (Houston):** clear Google Ads access — remove the two Netelixr manager-account links (Admin → Access & Security → Managers → CIDs `2218652780` and `4131958774`) + the temp user `sales%hilason.com@gtempaccount.com`, or apply for **Basic API access** so MD can do it. Unblocks the whole Google-paid + winter-blanket-Shopping push.
2. **Confirm turnout *sheets* are in the early-Aug inbound** (only 1 in stock).
3. Fix 2 mis-categorized Hilason SKUs (blanket/sheet titled as hardware) — needs the real product identity.

## 5. Access map & how to get things done
- **Shopify:** hilason.com ("Hilason Saddles and Tack" / hilasonretail). Shopify MCP connected (products, collections, orders, analytics, `update-collection`/`update-product`, `graphql_*`). Klaviyo company `Sd8MeD`.
- **Amazon:** DataDoe MCP (ads: `AMAZON_ADS_CAMPAIGNS_FIND/UPDATE`). Sellers — Hilason `de72a0e0-b12d-4736-9bf9-aee2ef61b5a1`, Uhorse `a741cde9-3a41-459f-881a-a2bbdc32738d`, BarH `ce5c2f8b-92ea-4e87-b850-263caf9700fd`, American Darling `ac9ce622-e58f-42db-99bf-df75a24c62cf`.
- **Supabase (StaffHub):** project `hvlwtpedsioogfguleon`. Log to `ceo_progress_reports` (one row per date — UPDATE to append, don't INSERT-dupe). Rich data: `search_console_metrics`, `keyword_rankings`, `seo_results`, `content_queue`, `amazon_sqp_rankings`, `amazon_*`.
- **MD (Hermes agent) — the ops workhorse.** VPS (see `INFRA-VPS.md`). Three ways to reach it:
  1. **Shell bridge:** insert into Supabase `hermes_tasks` (`requested_by, task_type='shell', title, command, timeout_seconds, status='pending'`); poll `stdout`. Runs `/bin/sh`; **base64-encode payloads** to avoid quoting hell.
  2. **Live autonomous agent (for real multi-step work):** `nohup /home/yasir/hermes-deployment/hermes-agent/.venv/bin/hermes -z "<prompt>" --provider deepseek -m deepseek-v4-pro --yolo > logfile 2>&1 &` (via the shell bridge). **Use the `.venv/bin/hermes`** (has `openai`); the bare wrapper fails. It writes a report file you then read. Runs ~5–15 min.
  3. **Passive inbox** (`~/.hermes/inbox/*.md`): MD only *memorizes* these (a cron digests to memory) — does NOT execute them. Don't use the inbox to make MD *do* things; use path 2.
- **GitHub:** this repo `yasir2k/yasir2k`, working branch **`claude/saddlery-sales-strategy-z0542c`**. Commit strategy/state docs here.

## 6. Standing guardrails
- **No blind ad spend** — verify conversion tracking first; ads paused-first; scale on ROAS. Amazon Sponsored ACOS < 25%.
- **No customer-facing email/SMS sends** without Yasir's copy sign-off.
- **No secrets in chat** — keys live on the VPS (`~/hermes-deployment/claude-bridge/integrations.env`, `~/.hermes/.env`).
- **Don't advertise out-of-stock SKUs.** Reversible/protective actions OK autonomously; consequential/outward ones → surface as a decision for Yasir.
- Anything ambiguous → write it up, don't act blind.

## 7. First moves in a new session
1. Read this file + the linked docs. Read the latest `ceo_progress_reports` row for anything after 2026-07-19.
2. Check the two winter task reports (`~/.hermes/inbox/reports/winter-{seo,amazon}-setup.md`) — relay results, verify the size-chart page + paused Amazon campaign.
3. If it's on/after Jul 21: confirm Yasir cleared Google Ads access → finish the Netelixr link removal, then build Merchant Center feed + draft Shopping/PMax for winter blankets.
4. Keep the weekly snapshot + billing watchdog honest; act on anything they surface.
