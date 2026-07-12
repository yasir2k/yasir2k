# Mission Control — Operating System

*How Saddlery Inc.'s AI team runs. Established 2026-07-12. Updated 2026-07-12: CEO model moved to Opus 4.8; Hermes added as a commanded employee.*

## The agent hierarchy (token economics by design)

| Role | Model | Does | Doesn't |
|---|---|---|---|
| **CEO** (main session) | Opus 4.8 (switched from Fable 5 for cost; run `/model claude-opus-4-8`) | Diagnosis, strategy, prioritization, specs, verification of results, decisions, coordinating Hermes | Bulk coding, data shoveling, long mechanical loops |
| **builder** (`.claude/agents/builder.md`) | Sonnet | Implementation: ingests, SQL, scripts, integrations, dashboards | Deciding what to build; DDL or destructive ops without instruction |
| **ops** (`.claude/agents/ops.md`) | Haiku | Chores: status checks, single queries, formatting, housekeeping | Anything requiring judgment |
| **Hermes** (VPS, via `hermes_tasks` bridge) | Own stack | Everything requiring VPS credentials/state: Shopify, SkuVault, ShipStation, DataDoe daily sync, SEO agent pipeline, forecast pipeline, eBay intelligence module | Setting strategy or priorities unilaterally — reports to CEO, does not run independently |

Rule of thumb: CEO turns should be short and decision-dense. Anything that takes more than ~10 tool calls of mechanical work gets a spec and goes to builder (cloud) or Hermes (VPS-resident work). Anything trivial goes to ops.

Governance decision (2026-07-12): Hermes already runs substantial production infrastructure (24 crons: forecast pipeline, eBay intelligence, SEO agents, inventory/Faire/ecom-health watchdogs, DataDoe Amazon sync since 2026-06-22). Rather than duplicate it from the cloud side, the CEO routes Phase 0/1 build-queue items that need VPS-side credentials to Hermes via the command bridge, and keeps the cloud builder scoped to work Hermes doesn't already own (e.g. the pre-2026-06-22 Amazon historical backfill). Hermes proposed operating independently; the user decided against it — Hermes stays a commanded employee, reporting through the bridge, so nothing is built twice or drifts out of sync.

## Current build queue (from SADDLERY-CEO-GAMEPLAN.md)

1. ✅ RLS enabled + policies on 5 exposed carrier/shipping tables (2026-07-12).
2. 🔄 Amazon ingest: DataDoe → `amazon_accounts`, `amazon_daily_metrics`, `amazon_sku_metrics`, `amazon_sync_logs` (builder, in flight).
3. `channel_pnl_daily` unified view: Amazon (new tables) + Shopify + eBay (`ebay_order_profit`) + in-store.
4. Alert wiring on `monitor_status`: eBay account collapse, TACOS breach, conversion drop, sync failure.
5. eBay account 22722 June-collapse investigation; work `ebay_opportunity_queue` (123 items).
6. DTC: email flows, bot filtering, product_type backfill, reviews import audit.

## Travel week (July 14–20, 2026) — autonomous coverage

A daily Routine resumes the main session each morning and:
1. Refreshes the Amazon ingest with the latest day's data (delegated to builder).
2. Advances the build queue above, in order — analysis and internal builds only.
3. Commits a daily progress report to `progress/YYYY-MM-DD.md` on branch `claude/saddlery-sales-strategy-z0542c` and pushes.
4. **Also writes the same report to the `ceo_progress_reports` StaffHub table** (report_date PK, body_md, metrics jsonb) so Yasir can scroll past dates in StaffHub. A StaffHub `/progress` page to render this table is scoped (routes are Next app-router client pages under `apps/skuvault/src/app/(app)/`, supabase server client in `src/lib/supabase/`) and queued to build during the travel window.

**Standing guardrails during autonomous operation:**
- No destructive operations, no DDL beyond the assigned amazon_*/view scope, no Shopify/customer-facing mutations, no spending, no external communications.
- Anything ambiguous or risky gets written up in the daily report as a decision-for-Yasir instead of acted on.
- The Routine self-disables after July 20.

## Security log

- 2026-07-12: RLS enabled with `authenticated`-only policies on `carrier_invoice_uploads`, `carrier_invoice_charges`, `shipstation_shipments`, `shipping_audit_findings`, `carrier_shipment_details`. Anon key locked out; service-role/server code unaffected.
- 2026-07-12: Audited legacy `ebay_Orders` card columns — `cardno`/`cardcvv` are EMPTY in all 58,998 rows (schema debris, no live PCI data). Drop the columns during legacy archival.

## Hermes command bridge — status

- Live since 2026-07-12. `hermes_claude_bridge.py` runs as systemd on the VPS, polling `hermes_tasks` in StaffHub Supabase every 20s. See `vps/INSTALL-HERMES-BRIDGE.md`.
- Verified two-way: CEO writes shell/ping tasks, Hermes executes and writes results back. Asynchronous (poll-based), not real-time push — no alert channel from Hermes back to a live CEO session yet (future work if needed).
- 2026-07-12 findings via the bridge: two Amazon-sync code bugs from 2026-07-05 (TEXT-column keyset `>` filter; wrong account-health field names) were confirmed **already fixed same-day** in `ecom-platform` commit `8374020d` and later. BarH Equine's daily sync has produced zero rows since 2026-07-05 despite `is_active`/`sync_enabled` both `true` today — root cause not yet confirmed; a Vercel runtime-logs check to see the actual cron invocation history hit a permission wall this session couldn't clear (`get_runtime_errors` requires interactive approval). **Next step: check the Vercel dashboard directly for `/api/cron/amazon-intelligence/daily-sync` invocation history around 2026-07-06–11**, or re-attempt from an interactive session.
- SEO report and action items live at `https://staff.uhorse.com/seo` (sub-pages: `/agents`, `/gsc`, `/batch`, `/collections`, `/history`, `/knowledge`); weekly summary via WhatsApp Mondays 7am. Open items found 2026-07-12: PR #7 (Hilason alt-text) approved but never merged; the auto-fixer is re-queuing already-fixed alt-text issues (dedup bug against `crawl_issues`); only ~9 of 4,577 open crawl issues have ever been queued for a fix (coverage gap beyond alt-text).

## Email / Klaviyo hygiene (2026-07-12)

- **Correction to SADDLERY-CEO-GAMEPLAN.md:** the "32,210 newsletter contacts" figure is inflated. Only **~787 are real, importable emails**; ~20,300+ rows are stored SQL-injection attack payloads (`PG_SLEEP`/`waitfor delay`) from the retired legacy signup form, plus other malformed junk. The owned-email asset rests on the **Shopify buyer base (≥10k subscribed), not the newsletter table.**
- **Security — resolved/no action:** the SQLi strings came from the OLD custom ecommerce platform, which is confirmed **decommissioned** (no nginx/Apache/PHP/legacy service listening on the VPS; hilason.com signup is now Shopify-handled and safe). Historical residue, no live exposure.
- **Klaviyo plan:** start with Hilason store. Source list = Shopify customers via **Klaviyo's native Shopify sync, configured subscribers-only** (handles consent + dedup automatically — no manual pre-clean of Shopify buyers needed) **+** the 787 verified legacy emails. Do NOT import the legacy newsletter table wholesale.
- Shopify Admin API token is NOT usable from the VPS (only Storefront-type tokens present; real admin tokens live in Vercel prod env). Not a blocker — Klaviyo syncs Shopify directly; the CEO session also has a working Shopify MCP connection for spot checks.

## Live status & pending queue — 2026-07-12 pre-travel (Yasir away Jul 14–20)

**Validated & ready (keys in `~/hermes-deployment/claude-bridge/integrations.env`):**
- ✅ Klaviyo private key works (account readable, suppression endpoint reachable).
- ✅ Cloudflare token works, correctly scoped to the hilason.com zone ONLY.

**In-flight / queued for the daily autonomous runs, in priority order:**
1. ✅ **Klaviyo hygiene DONE (2026-07-12).** Tally: 48,852 total → 12,380 subscribed (KEEP), 36,472 non-subscribed (SUPPRESS). **36,431 suppressed, 0 failures** (41 no-email unsuppressable). Billable count → ~12,380; the $682 quote should drop ~2/3. Reversible via `/home/yasir/klaviyo-hygiene/suppress.txt`. NOTE: user is still on Klaviyo FREE tier and will subscribe only after confirming the reduced quote — do NOT trigger any paid action.
2. **Klaviyo Shopify-sync config** — set to subscribers-only so the bot accounts don't silently re-inflate the billable count after suppression (the trap most people miss).
3. **Cloudflare bot filtering** — key ready; create WAF rules + Super Bot Fight Mode on hilason.com to stop the junk traffic feeding fake signups. Measure sessions before/after via Analytics:Read.
4. **Klaviyo flows** — build welcome, abandoned-checkout, post-purchase/replenishment, warmed win-back in DRAFT. Nothing sends without Yasir's copy sign-off.
5. **Amazon historical backfill** (cloud builder) — pre-2026-06-22 daily/SKU metrics; Hermes owns 2026-06-22+. 2,208 daily rows landed pre-interruption; resume after the API session limit resets (was hitting "session limit resets 9pm UTC").
6. **BarH Amazon sync** — code bugs already fixed 2026-07-05 (commit 8374020d); still zero rows since. Needs the Vercel dashboard log check for `/api/cron/amazon-intelligence/daily-sync` (Yasir-only; runtime-logs MCP call needs interactive approval).

**Closed / corrected this session:**
- ~~product_type backfill~~ **NOTHING TO DO.** Live Shopify catalog is already 100% typed (`-product_type:*` = 0 products). The "$197k untyped" in sales analytics is a historical artifact from deleted/archived products and gift cards in past orders — not a current gap, and not retroactively fixable. Supersedes the game plan's Phase-0 item.

## Notes

- Legacy `sales-manager` Supabase project is read-only source material (reviews, newsletter list, in-store sales) pending archival.
