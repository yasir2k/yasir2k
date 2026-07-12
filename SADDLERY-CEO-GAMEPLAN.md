# Saddlery Inc. — CEO Turnaround Game Plan

*Prepared 2026-07-12. Scope: Saddlery Inc. only (Hilason, Uhorse, BarH Equine). American Darling explicitly excluded.*
*All figures below are pulled live from Shopify Analytics (hilasonretail.myshopify.com), Supabase (StaffHub / ecom-platform), and DataDoe.*

---

## 1. The Honest Diagnosis — what is actually happening

### 1.1 The topline (Shopify DTC, net sales)

| Year | Net sales | Orders | Trend |
|---|---|---|---|
| 2022 | ~$1.03M | 5,414 | — |
| 2023 | ~$1.25M | 6,738 | **+21.6%** |
| 2024 | ~$1.62M | 8,615 | **+29.4%** (peak: Dec 2024, $199.7k) |
| 2025 | ~$1.34M | 6,258 | **−17.6%** |
| 2026 H1 | $586k (vs $658k 2025 H1, $801k 2024 H1) | 2,430 | **−10.9% YoY, −27% vs 2024** |

The business is not "slowly fading" — it grew strongly for two years and then broke in **January 2025**. Something specific changed; this is diagnosable and fixable.

### 1.2 It is a NEW-CUSTOMER problem, not a product or loyalty problem

- Orders fell **harder** than revenue (−27% vs −18% in 2025): volume is the issue, not pricing.
- AOV is **rising**: $203 (2024) → $237 (Q4 2025) → $267 (Q2 2026).
- Returning-customer rate is **rising**: 13% → 19.6%.
- New customers per quarter: **Q4 2024: 1,933 → Q4 2025: 1,290 → Q1 2026: 834** (−37% YoY).

Translation: the people who know Hilason love it and are spending more. **The top of the funnel has collapsed.** Existing customers are propping up the P&L while acquisition dies.

### 1.3 The funnel is broken in two places

**(a) Conversion rate is structurally bad — and getting worse.**
- Best months ever: ~0.6–0.7%. E-commerce benchmark for this AOV range: 1.5–3%.
- June 2024: 0.59% → June 2025: 0.13% → June 2026: **0.11%**.

**(b) Your analytics are polluted with junk traffic, so you can't see the truth.**
- May–Aug 2025 and May–Jun 2026 show massive session spikes (up to 196k/month vs a normal ~60k) converting at ~0.1%.
- May–Jun 2026: **236k of 260k sessions (91%) are "direct"** — no real store has that profile. This is bot/junk traffic. When it disappeared (Sep–Dec 2025), conversion "recovered" to ~0.5%. Your true traffic is roughly flat; your true conversion on real humans is likely ~0.5–0.7% — still less than half of benchmark.

### 1.4 You have essentially ONE acquisition channel

Full-year 2024 orders by source: ~82% direct/unknown, **18% search, 0.3% social (28 orders all year), ~0% email (18 email sessions in 2 months)**.

When search/organic softened in 2025 (Google algorithm shifts + AI-search eating product queries hit every niche retailer), there was no email program, no paid program, and no social presence to backstop it. A single-channel business fell with its channel. That is the root cause of the decline.

### 1.5 Unused assets sitting in your own databases

- **32,210 newsletter emails** (`ecom_newsletter`) + 14,578 Shopify customers — with effectively zero email revenue. Email should be 15–25% of DTC revenue for a repeat-purchase niche like tack. That alone is a ~$200–300k/yr hole.
- **1,023,619 product reviews** in the legacy DB (`ecom_reviews`) — verify provenance, but even a fraction imported to the storefront transforms conversion trust signals.
- **$197k of the last 12 months' net sales (~25%) has NO product type** — data hygiene that blinds every category-level decision.
- Returns run $5–20k/month (~7–10% of gross in bad months) with an empty returns-analysis pipeline.

### 1.6 StaffHub today: a Mission Control with the screens unplugged

StaffHub (Supabase `ecom-platform` + Vercel `ecom-platform-skuvault`) is ambitious — ~190 tables. Honest audit:

| Module | State |
|---|---|
| eBay intelligence (orders, profit-per-order, listing health, overlap audit) | ✅ **Live, well-documented, verified. The gold standard — this pattern works.** |
| Forecasting (`fc_*`: 42k reorder suggestions, 23.7k snapshots, 116k velocity rows) | 🟡 Data present; check `fc_sales` (0 rows after Jun/Jul backups — possible wipe during dedup) |
| **Amazon intelligence (17 tables)** | ❌ **ALL EMPTY — while Amazon (3 seller accounts, 1.1M rows sitting ready in DataDoe) is likely your largest channel** |
| CAI chat widget | ❌ 161k widget tokens served, **52 messages, 4 conversions** — installed but effectively dead or broken |
| Purchase orders / suppliers / shipments | ❌ Empty |
| SEO agents, content queue, GEO citations | ❌ Mostly empty (532 GSC rows, 464 keyword ranks — stalled) |
| Decision Desk, Council (multi-agent governance) | ❌ Empty — built, never used |
| Reddit CRM, brand mentions, image generation | ❌ Empty |
| Trading scanner + paper-trading bot | ⚠️ **Does not belong in the business. Founder-attention red flag.** |

**The pattern: engineering hours went into building tools, while the two levers that actually move revenue — email and conversion — got zero hours.** The business has a demand problem; it has been treated as a tooling problem.

### 1.7 Security (fix this week)

Supabase flags 5 tables with **Row Level Security disabled** — readable/writable by anyone holding the anon key: `carrier_invoice_uploads`, `carrier_invoice_charges`, `shipstation_shipments`, `shipping_audit_findings`, `carrier_shipment_details`.

```sql
-- Run only after adding appropriate policies, or access will be blocked entirely:
ALTER TABLE public.carrier_invoice_uploads ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.carrier_invoice_charges ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.shipstation_shipments ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.shipping_audit_findings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.carrier_shipment_details ENABLE ROW LEVEL SECURITY;
```

---

## 2. What I would do differently as CEO

1. **Ruthless focus.** Freeze every StaffHub module that doesn't touch revenue in the next 90 days (Council, Decision Desk, Reddit CRM, image gen). Move the trading system out of the business entirely — separate repo, separate database, evenings. Until growth resumes, 80% of build hours go to the funnel.
2. **Run the business on true numbers.** You cannot manage what you measure wrong: bot-polluted sessions, blank referrers, untyped products, an Amazon channel with zero telemetry. Fix measurement before strategy.
3. **Monetize what you already own before buying anything new.** The 32k email list and 1M reviews are worth more than any new module.
4. **Diversify demand deliberately.** One-channel dependence is what broke the business; the fix is a portfolio: email (owned), paid search/Shopping (bought), social/ambassador (earned), marketplaces (rented).
5. **Institute a weekly operating rhythm.** One Monday scorecard, five numbers, decisions made against targets. Mission Control is only useful if the CEO actually flies the ship from it weekly.

---

## 3. The Game Plan

### Phase 0 — This week: see clearly + stop obvious leaks

| # | Action | Why |
|---|---|---|
| 0.1 | Enable RLS on the 5 exposed tables (with policies) | Security |
| 0.2 | Turn on bot filtering / challenge junk traffic (Cloudflare rules on hilason.com; exclude "direct" spike traffic from reporting) | Every metric is currently a lie |
| 0.3 | Stand up email flows on Shopify Email or Klaviyo: welcome, abandoned checkout, post-purchase cross-sell, 60-day win-back. Import + clean `ecom_newsletter` (32k) | Fastest revenue in the whole plan; effectively free |
| 0.4 | Fix product taxonomy: assign `product_type` to the untyped catalog ($197k/yr of untyped sales) | Enables all category analytics |
| 0.5 | Decide fate of CAI widget: fix it or remove it (161k loads → 52 messages) | Dead weight on every page load |

### Phase 1 — 30 days: Conversion Rate Offensive (0.5% → 1.0% = ~2× DTC revenue at flat traffic)

1. **Reviews on the storefront.** Audit provenance of the 1M legacy reviews; import the legitimate, own-brand ones (Judge.me/Loox). Saddles are a $400–2,000 considered purchase — social proof is the #1 lever.
2. **Financing above the fold.** Shop Pay Installments / Affirm messaging on every saddle PDP ("From $54/mo"). At your AOV this routinely lifts conversion 10–20%.
3. **Saddle-fit confidence.** Fit guide + quiz ("Find your saddle in 60 seconds"), gullet/tree explainer videos, and a plain-English fit-guarantee/exchange policy on every PDP. Fear of mis-fit is the silent killer of saddle conversion — and likely a chunk of your 8–10% returns.
4. **Speed & mobile pass** on the top-20 traffic pages (saddles = 60% of revenue; start there).
5. **Site search fixes** using `search_analytics` + `search_synonyms` (already in StaffHub — rare example of a module that maps to money).

**KPI: real-human conversion ≥1.0% by day 30; email ≥8% of DTC revenue.**

### Phase 2 — 60–90 days: rebuild the demand portfolio

1. **Paid search restart, measured properly:** branded + high-intent category terms (barrel saddle, treeless saddle, roping saddle), Google Shopping feed hygiene, hard ROAS floor of 3, UTM discipline on every link the company touches.
2. **Ambassador/UGC program:** barrel racers and trail riders (western equine is an influencer-dense niche; 28 social orders/yr is inexcusable). Target: social from 0.3% → 5% of orders.
3. **Email cadence:** 2 campaigns/week (new drops, fit content, restocks) on top of Phase-0 flows. Target: email = 15% of DTC revenue by day 90.
4. **Returns program:** mine `return_returndetails` (3,064 rows) for top return-reason SKUs; fix listings (measurements, photos) or products. Every 1pt of return-rate = ~$15k/yr.

**KPI: new customers/quarter back above 1,200; ≥25% of orders from attributable channels (search/email/social/paid).**

### Phase 3 — 90–180 days: StaffHub becomes true Mission Control (see §4)

---

## 4. StaffHub → Mission Control HQ (Past · Present · Future, 360°)

**Design principle: one data spine, three time horizons, and a kill-switch for dead modules.** Replicate the eBay-intelligence pattern (documented, cron-fed, live-verified) — it's already your best work.

### 4.1 The data spine (build first — everything else reads from it)

```
channel_orders  — one row per order across ALL channels
  (source: Shopify MCP/API · Amazon via DataDoe exports (3 accounts, data already flowing)
   · eBay (already built ✅) · Faire (cache exists))
sku_master      — one row per SKU: landed cost, channel listings, velocity, stock
channel_pnl_daily — net sales, fees, ads, shipping, returns → TRUE MARGIN per channel/SKU/day
```

Priority #1: **populate the 17 empty `amazon_*` tables from DataDoe** (`exports_create` → ingest; 703k rows for Hilason alone are sitting there ready). Until then, Mission Control is blind on your biggest channel.

### 4.2 Three screens

**PAST — "What happened":** YoY/MoM by channel & category, cohort LTV, returns Pareto, marketing attribution. Answers "why are sales sinking" in one view instead of a month of wondering.

**PRESENT — "What needs me today":** today vs forecast pulse; alert feed (conversion drop >20% WoW, bot-traffic spike, top-20 SKU stockout, Amazon account-health, ad waste, sync failures — `monitor_status` already exists, wire it to alerts); cash position.

**FUTURE — "What's coming":** demand forecast (`fc_*` is your strongest asset — verify `fc_sales` integrity post-backup, then trust it), reorder suggestions → one-click PO into the empty `purchase_orders` module (build it now that it has a purpose), seasonal prep (Nov–Dec is 22–25% of your year), scenario planning.

### 4.3 Governance rules (this is what keeps Mission Control honest)

1. Every module has an owner, a cron, and a `last_sync` monitor. **No data for 30 days → module is deleted.** Shelfware is negative value: it costs attention.
2. New modules require a one-line answer to: *"Which of the 5 scorecard numbers does this move?"* No answer, no build.
3. Archive the legacy `sales-manager` project after extracting the two assets that matter (reviews, newsletter list). Don't carry 2014-era schema into the future.
4. Trading system moves out of the business stack entirely.

### 4.4 The Monday Scorecard (the 5 numbers Saddlery Inc. runs on)

| # | Metric | Current | 90-day target | 12-month target |
|---|---|---|---|---|
| 1 | Weekly net sales, all channels | ~$25k (DTC only visible!) | full visibility + growth vs LY | $1.6M DTC run-rate by mid-2027 |
| 2 | New customers / week | ~65 | 100 | 150 (2024 level) |
| 3 | Real-human conversion rate | ~0.5% | 1.0% | 1.5% |
| 4 | Email share of DTC revenue | ~0% | 15% | 20% |
| 5 | True margin per channel | **unknown** | known weekly | managed weekly |

---

## 5. The one-paragraph version

Saddlery Inc. doesn't have a product problem — customers who find you spend more and return more often every quarter. It has an **acquisition and conversion problem** caused by depending on a single traffic channel that weakened in 2025, a storefront that converts at a third of benchmark, and a completely unused email/reviews asset base — all hidden under bot-polluted analytics. Meanwhile, engineering effort went into a dozen half-finished tools instead of the funnel. The plan: clean the data and turn on email this week; run a 30-day conversion offensive (reviews, financing, fit-confidence); rebuild a four-channel demand portfolio in 90 days; and rebuild StaffHub around one data spine with Past/Present/Future screens and a five-number Monday scorecard — starting by plugging in Amazon, the biggest screen currently dark in Mission Control.
