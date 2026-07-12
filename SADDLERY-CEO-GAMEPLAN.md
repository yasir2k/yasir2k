# Saddlery Inc. — CEO Turnaround Game Plan (All-Channel Edition)

*Prepared 2026-07-12. Scope: Saddlery Inc. only (Hilason, Uhorse, BarH Equine) across ALL channels — Amazon, Shopify DTC, eBay, Walmart, in-store, Faire. American Darling excluded.*
*Every figure pulled live from: Shopify Analytics (hilasonretail.myshopify.com), DataDoe (3 Amazon Seller Central accounts), Supabase StaffHub (`ecom-platform`), and the legacy `sales-manager` database.*

---

## 1. The 360° Revenue Map — what the business actually is

| Channel | 2025 sales | Share | H1 2026 vs H1 2025 | Tracked in StaffHub? |
|---|---|---|---|---|
| **Amazon — Hilason Superstore** | ~$3.58M | ~60% | **−24%** | ❌ 17 tables, 0 rows |
| **Amazon — Uhorse Western** | ~$471k | ~8% | −3% | ❌ |
| **Amazon — BarH Equine** | ~$80k | ~1% | **−36%**, July profit negative | ❌ |
| **Shopify DTC (hilason.com)** | ~$1.34M net | ~22% | −10.9% | partial |
| **eBay (uhorse + tack4comfort)** | ~$250–300k/yr run-rate | ~4–5% | history starts Apr 2026 | ✅ best-built module |
| **In-store / POS** | ~$180k (972 orders) | ~3% | untracked | ❌ lives only in legacy DB |
| **Walmart** | $0 / dormant | — | no data anywhere | ❌ name in 2014 legacy list only |
| **Faire (wholesale)** | unknown | ? | sync exists, sales unmeasured | partial |
| **TOTAL (known)** | **~$5.9–6.0M** | | **≈ −19% H1 YoY** | |

**The single most important fact in this document: Amazon is ~3× your DTC business, it is declining FASTER than DTC (−22% vs −11%), and it is the one channel your Mission Control has zero telemetry on.** The Shopify decline is real, but the Amazon decline is the P&L. A 22% decline on $4.1M costs you ~$900k/year; the entire Shopify decline costs ~$150k.

### Consolidated trajectory (Amazon + Shopify, the two measured channels)
- H2 2024 run-rate: Amazon $2.42M/half + Shopify peak — the business was a ~$7M/yr business at Christmas 2024.
- H1 2025: $2.55M combined → H1 2026: $2.07M combined. **The company is shrinking ~$1M/year in run-rate.**
- Seasonality: Nov–Dec is the super-peak (Amazon alone did $1.21M in Nov–Dec 2024, $941k in Nov–Dec 2025 — holiday itself declined 22%). **Whatever we fix must be fixed before October.**

---

## 2. Channel-by-channel diagnosis

### 2.1 Amazon (~69% of revenue) — declining, under-advertised, and flying blind until 4 months ago

The DataDoe data (ingestion begins June 2024) shows:

1. **Ad spend was ~$0 from at least mid-2024 until May 2026.** You ran a $4M/yr Amazon business with no Sponsored Products while Amazon turned decisively pay-to-play. Organic rank erodes exactly this way: competitors buy the top of search, your velocity slips, rank slips, flywheel reverses — a slow −20%/yr bleed, which is precisely what the data shows. First ads appeared May 2026 ($8.4k) and June ($9.2k) with TACOS ~3.5% — the right direction, but a fraction of what defending the category takes (5–10% TACOS is normal for western/equine gear).
2. **Fee/settlement visibility only began ~March 2026.** Before that, "profit" in DataDoe excluded fees entirely. Where data is complete (Apr–Jun 2026), Amazon nets roughly **37–45% after fees, COGS, and ads** — genuinely excellent margins (own-brand manufacturing) worth defending aggressively.
3. **Per-account picture:** Hilason Superstore −24% (the crisis); Uhorse roughly flat (−3%) — note Feb 2026 orders spiked to 911 on flat dollars, meaning cheaper items are replacing saddle sales; BarH −36% and unprofitable in July 2026 — consolidate or fix listing-level economics.
4. **Zero systematic telemetry:** no account-health monitoring, no SQP rank tracking, no ad-waste detection, no reimbursement recovery — all 17 `amazon_*` StaffHub tables are empty while 1.1M rows sit ready in DataDoe.

**CEO call: Amazon is priority #1.** Restoring Amazon to 2025 levels alone recovers ~$750k/yr — more than everything else in this plan combined.

### 2.2 Shopify DTC (~22%) — a new-customer collapse under bot-polluted analytics

- Net sales: $1.03M (2022) → $1.25M (2023) → $1.62M (2024) → $1.34M (2025, −18%) → H1 2026 −11% further.
- Orders fell harder than revenue (−27% in 2025); AOV rising ($203→$267); returning-customer rate rising (13%→19.6%); new customers/quarter **1,933 (Q4'24) → 834 (Q1'26)**. The loyal core is fine; acquisition collapsed.
- One-channel dependence: 2024 orders ~82% direct/unknown, 18% search, **28 social orders all year, ~0 email**. When search weakened in 2025 (algorithm shifts + AI search), nothing backstopped it.
- Conversion at best ~0.6% vs 1.5–3% benchmark — and analytics are polluted: May–Jun 2026 shows 236k of 260k sessions as "direct" converting at ~0.1% (bot traffic). True human conversion ~0.5–0.7%.
- Unused assets: **32,210 newsletter emails**, 14,578 customers, **1,023,619 legacy product reviews** (verify provenance before import), all generating $0.

### 2.3 eBay (~4–5%) — the best-built system, the shallowest history

- The StaffHub eBay intelligence module (per-order profit with confidence scoring, listing health, two-account overlap audit, repricing queue) is the gold standard in your stack — documented, cron-fed, live-verified.
- But order history starts April 2026 (Rithum ingest), and **account 22722 collapsed in June (95 → 20 orders month-over-month)** while 22726 grew to 245 — investigate now (suppressed listings? defect rate? Rithum feed break?). The 123-item opportunity queue and 21,762-SKU overlap audit are built — work them.
- Legacy DB holds ~59k historical eBay orders for baseline/LTV analysis if ever needed.

### 2.4 Walmart — dormant, and that's a decision, not an accident

Walmart appears only as a channel name in the 2014-era legacy system. There is no active listing, order, or revenue data anywhere. Given Rithum (ChannelAdvisor) is already your eBay pipe and supports Walmart, the marginal cost of a structured Walmart pilot is low — but only AFTER Amazon and DTC are stabilized. Decide deliberately: **pilot in Q4 via Rithum with your top-50 proven SKUs, or formally kill it.** An untracked half-channel is worse than either choice.

### 2.5 In-store (~$180k/yr) — real money invisible to every dashboard

972 orders / $179,643 in 2025, recorded only in the legacy database. It must flow into the unified P&L like every other channel.

### 2.6 StaffHub — enormous ambition, screens unplugged

~190 tables; honest audit: eBay module ✅ live; forecasting (`fc_*`) 🟡 has data (verify `fc_sales` integrity — 0 rows alongside Jun 30 / Jul 3 backup tables); Amazon ❌ empty; CAI chat ❌ 161k widget loads → 52 messages → 4 conversions; PO/suppliers ❌ empty; SEO agents ❌ stalled; Decision Desk / Council / Reddit CRM / image gen ❌ empty; **plus a personal trading scanner and paper-trading bot living inside the business database** — scope creep that dilutes founder attention.

**The pattern: engineering hours went to building tools while the funnel (Amazon ads, email, conversion) got zero hours. This is a demand problem being treated as a tooling problem.**

### 2.7 Security & data hygiene (fix this week)

- **5 tables with Row Level Security disabled** (anyone with the anon key can read/write): `carrier_invoice_uploads`, `carrier_invoice_charges`, `shipstation_shipments`, `shipping_audit_findings`, `carrier_shipment_details`.
  ```sql
  -- Add policies first, or this blocks all access:
  ALTER TABLE public.carrier_invoice_uploads ENABLE ROW LEVEL SECURITY;
  ALTER TABLE public.carrier_invoice_charges ENABLE ROW LEVEL SECURITY;
  ALTER TABLE public.shipstation_shipments ENABLE ROW LEVEL SECURITY;
  ALTER TABLE public.shipping_audit_findings ENABLE ROW LEVEL SECURITY;
  ALTER TABLE public.carrier_shipment_details ENABLE ROW LEVEL SECURITY;
  ```
- The legacy `ebay_Orders` table has raw card-number and CVV columns (`cardno`, `cardcvv`) — a PCI liability even if stale. Audit and purge those columns during legacy archival.
- $197k (~25%) of trailing-12-month Shopify net sales has no `product_type`; legacy channel totals are zeroed migration artifacts. Category-level decisions are being made blind.

---

## 3. What I would do differently as CEO

1. **Manage the portfolio, not the website.** The mental model has been "hilason.com plus some marketplaces." The reality is an Amazon-first business (69%) with a DTC arm. Capital, hours, and dashboards should be allocated 60/30/10 — Amazon / DTC / everything else — until growth resumes.
2. **Buy demand deliberately on every channel.** Zero Amazon ads until two months ago, zero email, 28 social orders/year — the company has never systematically paid for or owned demand. That worked while organic was free; that era ended in 2025 on both Google and Amazon simultaneously. This is the root cause of "sinking sales."
3. **Run on true, consolidated numbers.** One P&L across 6+ channels, bots filtered, fees visible, COGS attached. Today no single view shows the whole company — StaffHub's most important screen (Amazon) is dark, and $180k of in-store sales isn't on any screen.
4. **Ruthless focus.** Freeze Council, Decision Desk, Reddit CRM, image gen; fix or kill the chat widget; move the trading system out of the business stack. Every build hour goes to revenue until the trend reverses.
5. **Operate on a weekly rhythm.** Monday scorecard, five numbers, decisions against targets — and everything must be fixed **before October**, because Nov–Dec is a quarter of the year.

---

## 4. The Game Plan

### Phase 0 — This week: see clearly, stop leaks
1. Enable RLS on the 5 exposed tables (with policies); schedule the legacy card-data purge.
2. Bot-filter hilason.com (Cloudflare challenge rules); exclude junk "direct" traffic from reporting.
3. Turn on email flows (Klaviyo or Shopify Email): welcome, abandoned checkout, post-purchase, win-back; import + clean the 32k `ecom_newsletter` list. Fastest revenue in this plan.
4. Investigate eBay account 22722's June collapse; work the existing 123-item opportunity queue.
5. Fix `product_type` on the untyped Shopify catalog; verify `fc_sales` integrity.

### Phase 1 — 30 days: the two revenue offensives

**A. Amazon Growth Engine (the big one)**
1. Ramp Sponsored Products on Hilason Superstore top-100 SKUs: exact-match on proven search terms, TACOS guardrail 5–8%, weekly negative-keyword pass. Target: back to 2025 monthly run-rate by October.
2. Populate StaffHub's `amazon_*` tables from DataDoe (Profit-by-SKU/Date + Sales & Traffic sources are ready today) → per-SKU, per-account true margin.
3. Triage the top-50 declining ASINs (Hilason −24%): buy-box %, suppressed listings, content quality, review velocity, price vs competitors — fix listing by listing.
4. BarH decision: fold winners into Hilason Superstore or fix per-listing economics; stop the negative-profit bleed.
5. Turn on account-health + SQP rank monitoring (tables already exist; wire the cron like the eBay module).

**B. DTC Conversion Offensive (0.5% → 1.0% ≈ 2× DTC at flat traffic)**
1. Reviews on storefront (audit the 1M legacy reviews' provenance; import legitimate own-brand ones).
2. Financing above the fold on every saddle PDP (Shop Pay Installments/Affirm — "From $54/mo").
3. Saddle-fit confidence: fit quiz, gullet/tree videos, plain-English exchange guarantee (also attacks the 7–10% return rate).
4. Speed/mobile pass + site-search fixes on top-20 pages (`search_analytics` is already collecting).

### Phase 2 — 60–90 days: rebuild the demand portfolio
1. Google paid search + Shopping feed with hard ROAS floor 3 and UTM discipline everywhere.
2. Ambassador/UGC program (barrel racers, trail riders). Social from 0.3% → 5% of DTC orders.
3. Email to 2 campaigns/week; target 15% of DTC revenue by day 90.
4. Returns program: mine `return_returndetails` (3,064 rows) for top return-reason SKUs; fix listings or products.
5. In-store sales flow into the unified P&L (even a nightly CSV from the POS beats invisible).
6. **Walmart decision:** Q4 pilot via Rithum with top-50 proven SKUs — or formally kill it. No half-channels.

### Phase 3 — 90–180 days: StaffHub becomes true Mission Control (§5)

---

## 5. StaffHub → Mission Control HQ (Past · Present · Future, 360°)

**Design principle: one data spine, three time horizons, a kill-switch for dead modules.** Replicate the eBay-intelligence pattern — documented, cron-fed, live-verified — across every channel.

### 5.1 The data spine (build first)
```
channel_orders   — one row per order: amazon_hilason | amazon_uhorse | amazon_barh |
                   shopify | ebay_uhorse | ebay_t4c | instore | faire | (walmart)
sku_master       — one row per SKU: landed cost, per-channel listings, velocity, stock
channel_pnl_daily — sales, fees, ads, shipping, returns → TRUE MARGIN per channel/SKU/day
```
Sources already available today: DataDoe exports (Amazon, incl. profit tables), Shopify API, eBay module (built), legacy DB (in-store), Faire cache. Priority #1 is the Amazon ingest — the biggest screen is currently dark.

### 5.2 Three screens
- **PAST:** YoY/MoM by channel & category, cohort LTV, returns Pareto, holiday post-mortems. Answers "why are sales sinking" in one view.
- **PRESENT:** today vs forecast across all channels; alert feed — Amazon account health, buy-box loss, TACOS breach, eBay account collapse (a 22722-style event should page you the same week, not surface in an annual review), DTC conversion drop >20% WoW, bot spike, top-20 SKU stockout, sync failures (`monitor_status` exists — wire it to alerts).
- **FUTURE:** demand forecast (`fc_*` is your strongest asset), reorder → one-click PO (build the empty PO module now that it has a purpose), Nov–Dec capacity/cash planning, Walmart pilot scenario.

### 5.3 Governance
1. Every module: an owner, a cron, a `last_sync` monitor. **No data for 30 days → deleted.** Shelfware costs attention.
2. New modules must answer: *"Which scorecard number does this move?"*
3. Archive `sales-manager` after extracting reviews, newsletter list, in-store feed; purge card-data columns.
4. Trading system leaves the business stack.

### 5.4 The Monday Scorecard — the 6 numbers Saddlery Inc. runs on

| # | Metric | Current | 90-day target | 12-month target |
|---|---|---|---|---|
| 1 | Weekly net sales — ALL channels | ~$100k, fragmented | one number, growing vs LY | $7M/yr run-rate (Christmas-2024 level) |
| 2 | Amazon sales vs LY | −22% | −5% | +10% |
| 3 | Amazon TACOS / true margin | ~3.5% / ~40% (new visibility) | 5–8% / ≥35% | managed weekly |
| 4 | DTC new customers/week + real conversion | ~65 / ~0.5% | 100 / 1.0% | 150 / 1.5% |
| 5 | Email share of DTC revenue | ~0% | 15% | 20% |
| 6 | % of revenue with true margin known | ~25% | 90% | 100% |

---

## 6. The one-paragraph version

Saddlery Inc. is a ~$6M multichannel business whose two engines stalled at once: Amazon (69% of revenue) has bled ~22%/yr since ads stopped mattering less and you weren't buying any, and DTC (~22%) lost its single free traffic channel with no email, paid, or social to backstop it — all obscured by bot-polluted analytics, invisible fees, and a Mission Control whose Amazon screen was never plugged in. The margins are excellent (~40% net on Amazon), the loyal customers spend more every quarter, and the assets to fix this (32k emails, 1M reviews, ready-to-ingest Amazon data, a proven eBay intelligence pattern) are already yours. The plan: this week, clean the data, secure the database, and turn on email; in 30 days, ramp Amazon ads with TACOS guardrails and run the DTC conversion offensive; in 90 days, a four-channel demand portfolio, an in-store feed, and a go/no-go Walmart pilot; and by day 180, StaffHub runs the company — one data spine, three time horizons, six Monday numbers — with everything live before the Nov–Dec quarter that decides the year.
