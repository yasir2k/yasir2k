# Winter Blankets — Execution Log & Ready-to-Apply Package

*Companion to `WINTER-BLANKETS-STRATEGY.md`. What was actually produced by the 2026-07-19 implementation run, and exactly what Yasir needs to apply. Full source reports live on the VPS at `~/.hermes/inbox/reports/winter-amazon-setup.md` and `winter-seo-setup.md`.*

---

## AMAZON — DONE (prepared, needs manual apply)

MD verified the ASINs and produced a complete optimization package. **Tooling limit:** listing edits + Sponsored-campaign creation can't be pushed via DataDoe API — they must be applied in **Seller Central** (listings) and the **Ads console** (campaign). Copy below is ready to paste.

### The winter ASINs
Three full-size 1200D / **400g** belly-wrap variants share parent **B0CLVR3ZPS**: `B083B6C6QV` (Pink 78"), `B0BH6ZFWPN` (Brown 78"), `B01MTK2GXC` (Red 72"). Plus `B08NWJ1WFX` (mini, low activity). ~133 Hilason turnout-blanket child ASINs total (mostly 600D).

### Current title (all three) — weak
`HILASON 1200D Winter Waterproof Poly Horse Blanket Belly Wrap | Turnout Blankets for Horses`
Problems: no size, "Poly" not "Ripstop", **400g differentiator buried**, no gussets/tail-flap/breathability, no A+.

### Optimized titles (apply per ASIN)
`HILASON 1200D Horse Turnout Blanket - Waterproof Breathable Ripstop Winter Blanket, Heavyweight 400g Fill, Belly Wrap, Shoulder Gussets & Tail Flap, [SIZE] in, [COLOR]`
- B083B6C6QV → `…, 78 in, Pink`
- B0BH6ZFWPN → `…, 78 in, Brown`
- B01MTK2GXC → `…, 72 in, Red`
- B08NWJ1WFX → `HILASON 1200D Miniature Horse Turnout Blanket - Waterproof Breathable Ripstop Winter Blanket, Heavyweight 400g Fill, Belly Wrap, Shoulder Gussets & Tail Flap, Mini/Shetland`

### 5 bullets (lead with the 400g differentiator)
1. **HEAVIER THAN THE REST:** 400g polyfill — warmer than standard 300g turnouts; comfortable in freezing temps without layering; won't flatten or shift.
2. **WATERPROOF & BREATHABLE:** 1200D ripstop shell + sealed seams keep rain/snow out while moisture escapes; UV-resistant coating.
3. **STAYS IN PLACE ALL NIGHT:** deep belly wrap, adjustable double-buckle front, reinforced shoulder gussets, removable elastic leg straps — no twisting/rubbing/slipping.
4. **TAIL-TO-SHOULDER COVERAGE:** insulated tail flap; D-rings for neck cover/hood (sold separately); high-cut neck prevents wither rub.
5. **BUILT TO LAST:** double-stitched stress seams, rust-resistant nickel hardware, reinforced surcingle points; backed by Hilason's quality guarantee.

### Backend search terms (~250 bytes, no title repeats)
`horse rug winter blanket paddock rug pony blanket mini horse blanket foal turnout 1680d 600d midweight lightweight rain sheet detachable neck combo neck reflective hi vis mare gelding gusseted no rub fleece wither snow windproof stable rug`

### A+ / Brand Store — #1 GAP (currently NONE)
Biggest impact move vs page-1 competitors (Harrison Howard, Derby). Build 4 A+ modules: (1) comparison chart Hilason 400g vs generic 200–300g; (2) weight-selection guide (°F → fill); (3) size chart + how-to-measure; (4) feature close-ups (belly wrap, gussets, tail flap, D-rings, sealed seams). Enroll Brand Registry + Brand Store.

### Sponsored Products campaign — SPEC READY, create PAUSED
Name **"Hilason Winter Turnout — 1200D"**, budget $15–20/day, dynamic-down bids, ACOS target <25%, placement Top-of-Search +25%.
- Exact: `horse turnout blanket` $0.65 · `winter horse blanket` $0.65 · `1200d turnout blanket` $0.60 · `waterproof turnout blanket` $0.55 · `heavyweight turnout blanket` $0.55
- Phrase: `turnout blanket` $0.45 · `pony turnout blanket` $0.40 · `mini horse blanket` $0.40
- ASIN targets: Tough-1 Snuggit, Derby Nordic-Tough, TGW Riding, Kensington
- Negatives at launch: sheet, rain sheet, fly sheet, mesh, 600d, 200g, 300g, lightweight, midweight, used, repair
- **Activate only when the first FBA shipment checks in (early Aug).** Don't spend on out-of-stock.

## eBAY — pipeline ready, needs a manual run
Item-specifics pipeline exists (`~/ecom-platform/apps/seo-agents/agents/deepseek_full_pipeline.py`); winter blanket listings likely under the Uhorse eBay store (Rithum APID 12045671). Run to align denier/fill/size/waterproof/neck specifics + titles.

## GOOGLE ORGANIC (SEO) — IN PROGRESS at session end
MD SEO task (PID 3682447) was **still running when this session ended** — it's generating the guide-article cluster through the judge-gated content pipeline (the heaviest, slowest step; each article is a full LLM generation + judge pass, so the run legitimately takes 30–60+ min).

**Next session — pick it up:**
1. Check `~/.hermes/inbox/reports/winter-seo-setup.md`. If present → fold in the published/queued pages (size-chart rebuild, collection temp/fill table, content cluster) and verify the size-chart page went live with CTAs into `/collections/turnout-blankets`.
2. Also check Supabase `content_queue` (status='published', domain_slug ilike 'hilason%', recent `published_at`) and `seo_judge_log` for what actually shipped vs held at the >=90% quality gate.
3. If the run died without a report, re-dispatch it — the exact prompt is saved on the VPS at `~/.hermes/inbox/reports/winter-seo.prompt` (relaunch via `hermes -z "$(cat …/winter-seo.prompt)" --provider deepseek -m deepseek-v4-pro --yolo`).

---

## What needs Yasir (to convert this into live rank)
1. **Apply the Amazon listing copy** (titles + bullets + backend) in Seller Central for the 4 ASINs — or authorize MD to do it via browser/computer-use.
2. **Build A+ content + Brand Store** (biggest lever) — enroll Brand Registry if not done.
3. **Create the paused Sponsored campaign** from the spec (ads console); flip on when Aug stock lands.
4. (From strategy) Tue Jul 21: clear Google Ads access → unlock Shopping/PMax.
