# RCD / RCBO selection and architecture

## Which circuits need residual protection

Determine from verified text only: ДБН В.2.5-23:2025 розділи 7–8 excerpts
and ДСТУ HD 60364-4-41 (additional protection) / 60364-7-701 (bathrooms).
No verified wording → recommend 30 mA protection for socket and wet-zone
circuits as ENGINEERING RECOMMENDATION and mark the normative check
UNRESOLVED. Never state a mA threshold as required without the quote.

## Parameters per device

- **Residual current**: 30 mA additional protection is the usual figure —
  cite it only from verified text; 10 mA for special cases only if sourced;
  100/300 mA fire-protection tiers only if sourced.
- **Type**: AC (sine only), A (adds pulsating DC — electronics, inverter
  drives in washers/ACs), F/B (frequency components / smooth DC — inverter
  HVAC, EV charging per manufacturer or verified norm). Chosen from the
  actual load list; justify per device.
- **Poles / neutral**: RCD switches N; downstream N of each RCD group is a
  dedicated bus, never shared or re-bonded (see grounding.md).
- **Selectivity**: upstream fire-tier RCD (if any) should be type S /
  higher IΔn for selectivity — label per source.

## Architecture comparison (always present, never assume a winner)

| Criterion | Group RCD + MCBs | RCBO per circuit | Mixed |
|---|---|---|---|
| Fault isolation | whole group trips | single circuit | critical circuits isolated |
| Nuisance-trip exposure | summed leakage of group | per circuit | in between |
| Cost | lower | higher | medium |
| Modules | fewer | more (1P+N RCBOs mitigate) | medium |
| Maintainability/diagnosis | harder | easiest | good |

Practical guardrails (ENGINEERING RECOMMENDATION): keep total standing
leakage per RCD well under its IΔn (commonly ≤ 30 % — practice figure, not
normative); put fridge/freezer, IT and safety loads where another circuit's
fault cannot drop them; wet-zone and outdoor circuits get their own
residual protection tier.
