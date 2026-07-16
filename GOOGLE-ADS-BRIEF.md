# Google Ads — Session Handoff Brief (Hilason / Saddlery Inc.)

*Purpose: everything a fresh Claude session needs to run the Google Ads initiative without re-deriving context. Written 2026-07-16 by the CEO session. Start here.*

---

## 1. Who / what this is
- **Saddlery Inc.** — ~$6M western tack & saddlery business. Brands: **Hilason** (primary), Uhorse, BarH Equine, American Darling.
- Channels: **Amazon ~69%** (was declining ~22%/yr — the core crisis), **Shopify DTC ~22%**, eBay + in-store the rest.
- **Turnaround thesis:** demand was never *bought* or *owned* — no ads, no email until mid-2026. Fix = buy demand profitably (Amazon ads ✓, Google ads = this initiative) + own the audience (email ✓).
- You act as **CEO of the business** (strategy + decisions), delegating ops to agents. Model: Opus 4.8.

## 2. What's already live (don't rebuild)
- **Amazon ads:** Live across all brands. Last 10 days ~$2.3k spend → ~$17.5k attributed sales (~13% ACOS, ~7.5× ROAS). Star = Hilason **fly sheets** ($864→$8,022). Managed via **DataDoe** MCP.
- **DTC email (Klaviyo):** On-brand **newsletter popup** live on hilason.com (free-shipping hook, code `FIRSTRIDE`, double opt-in). **5 flows live** (Welcome, Abandoned Cart, Thank You, Post-Purchase, Review). ~211 confirmed signups.
- **Mission Control:** StaffHub (`staff.uhorse.com`) with a `/progress` daily log (Supabase table `ceo_progress_reports`).

## 3. Known open issues (in flight — don't duplicate)
- **Klaviyo↔Shopify events:** on reconnection, only login + onsite forms came back; server-side events (Placed Order / Checkout Started) were NOT flowing (Klaviyo metrics count = 0), so Abandoned Cart couldn't fire + no revenue attribution. **Yasir reintegrated Shopify 2026-07-16; MD is verifying.** *This matters for Google too — conversion tracking depends on clean Shopify measurement.*
- **Uhorse ads:** underwater "Low Sales – Auto" campaign keeps auto-re-enabling (MD tasked to kill the mechanism); POC campaigns live but winning ~0 impressions (MD tasked to fix bids/targeting).

## 4. The Google Ads plan (approved direction — start with hilason.com)
**Phase 0 — Foundation (zero spend, start now):**
- Google **Merchant Center** + product feed (Shopify "Google & YouTube" app auto-syncs). Review takes days — start early.
- **Conversion tracking:** Google Ads tag + GA4 + Enhanced Conversions. *Verify before any spend.*
- Confirm the site monetizes paid traffic (popup ✓ + Abandoned Cart working once the Klaviyo event fix lands).

**Phase 1 — Launch (conservative):**
- **Brand Search first** (defend "Hilason" terms — cheap, highest ROAS, near-zero risk).
- **Shopping / Performance Max** on proven winners — lead with **fly sheets**, then saddles, protective vests. Feed-driven, ROAS-target bidding.

**Phase 2 — Scale (on performance):** non-brand category Search, retargeting, more PMax asset groups. Scale on ROAS, not a fixed cap.

**Budget:** start ~$1.5–2k/mo (brand small, Shopping/PMax the bulk); loose ROAS target while learning, then scale winners.

**Timing decision (CEO call):** foundation NOW; **spend goes live only when (1) conversion tracking verified, (2) Shopify→Klaviyo cart-recovery confirmed working, (3) Yasir back to watch week 1.** ~1–2 weeks out. Brand Search first, Shopping right behind.

## 5. The one thing that needs Yasir
A **Google Ads account + Merchant Center** (his Google login) — an agent can't create these. Once they exist, MD can do the feed/tags/hygiene.

## 6. Access map & how to get things done
- **Shopify:** store = hilason.com ("Hilason Saddles and Tack"), Shopify MCP connected. Klaviyo company id `Sd8MeD`.
- **Amazon:** DataDoe MCP. Seller IDs — Hilason `de72a0e0-b12d-4736-9bf9-aee2ef61b5a1`, Uhorse `a741cde9-3a41-459f-881a-a2bbdc32738d`, BarH `ce5c2f8b-92ea-4e87-b850-263caf9700fd`, American Darling `ac9ce622-e58f-42db-99bf-df75a24c62cf`.
- **Supabase (StaffHub):** project `hvlwtpedsioogfguleon`. Log progress to `ceo_progress_reports`.
- **MD (Hermes agent) — delegate ops here.** Full autonomous agent on the VPS with live Shopify/Klaviyo/DataDoe/SkuVault/GA/etc. access, headless browser, image gen, cron. Reach it two ways:
  1. **Command bridge (shell):** insert a row into Supabase table `hermes_tasks` (`requested_by, task_type='shell', title, command, timeout_seconds, status='pending'`); poll `stdout`. Bridge runs `/bin/sh`; **base64-encode scripts** to avoid quoting issues. Klaviyo key etc. live in `~/hermes-deployment/claude-bridge/integrations.env` on the VPS (never paste keys in chat).
  2. **Natural-language tasks:** write a `Task / Context / Acceptance` brief to `~/.hermes/inbox/` (picked up every ~30 min); MD reports on Telegram. Full capabilities in `~/brain/MD-CAPABILITIES.md`.

## 7. Standing guardrails (apply to Google Ads too)
- **Conversion tracking verified before spend.** No blind spend.
- **Brand Search first**, then Shopping; **scale on ROAS**, not a fixed budget cap.
- Ads created **paused-first** where feasible; nothing scales without performance justification.
- **No secrets in chat** (keys on the VPS). No customer-facing email/SMS sends without Yasir's copy sign-off.
- Anything ambiguous → write it up as a decision-for-Yasir, don't act blind.

## 8. First moves in the new session
1. Read this file. Ask MD (via `~/.hermes/inbox/`) for status on the Klaviyo event fix + whether GA4/Google tag already exist on the store.
2. Confirm with Yasir that a Google Ads + Merchant Center account exists (or walk him through creating them).
3. Have MD set up the Merchant Center product feed (Shopify Google & YouTube app) + conversion tracking. Verify.
4. Draft the Brand Search + Shopping/PMax campaign structure (paused/draft). Do **not** enable spend until the 3 timing boxes are checked.
