# Mission Control — Operating System

*How Saddlery Inc.'s AI team runs. Established 2026-07-12.*

## The agent hierarchy (token economics by design)

| Role | Model | Does | Doesn't |
|---|---|---|---|
| **CEO** (main session) | Fable 5 | Diagnosis, strategy, prioritization, specs, verification of results, decisions | Bulk coding, data shoveling, long mechanical loops |
| **builder** (`.claude/agents/builder.md`) | Sonnet | Implementation: ingests, SQL, scripts, integrations, dashboards | Deciding what to build; DDL or destructive ops without instruction |
| **ops** (`.claude/agents/ops.md`) | Haiku | Chores: status checks, single queries, formatting, housekeeping | Anything requiring judgment |

Rule of thumb: Fable turns should be short and decision-dense. Anything that takes more than ~10 tool calls of mechanical work gets a spec and goes to builder. Anything trivial goes to ops.

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

**Standing guardrails during autonomous operation:**
- No destructive operations, no DDL beyond the assigned amazon_*/view scope, no Shopify/customer-facing mutations, no spending, no external communications.
- Anything ambiguous or risky gets written up in the daily report as a decision-for-Yasir instead of acted on.
- The Routine self-disables after July 20.

## Security log

- 2026-07-12: RLS enabled with `authenticated`-only policies on `carrier_invoice_uploads`, `carrier_invoice_charges`, `shipstation_shipments`, `shipping_audit_findings`, `carrier_shipment_details`. Anon key locked out; service-role/server code unaffected.
- 2026-07-12: Audited legacy `ebay_Orders` card columns — `cardno`/`cardcvv` are EMPTY in all 58,998 rows (schema debris, no live PCI data). Drop the columns during legacy archival.

## Notes

- A connected MCP server (id `8d3945fb…`) requires OAuth authorization and is unreachable from non-interactive sessions — if this is the Hermes agent connector, authorize it in claude.ai connector settings to bring Hermes into the loop.
- Legacy `sales-manager` Supabase project is read-only source material (reviews, newsletter list, in-store sales) pending archival.
