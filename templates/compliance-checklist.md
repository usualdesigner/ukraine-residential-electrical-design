# Compliance review checklist

Every line gets: a classification label, evidence (citation / calculation /
input reference), or `UNRESOLVED (needs: …)`. No line may be silently skipped.
Split verdicts into **DESIGN-TIME CHECK** (what this review can establish)
vs **FIELD VERIFICATION REQUIRED** (measurements only an electrician can do).

## Design-time checks

- [ ] **Cable vs breaker** — Ib ≤ In ≤ Iz holds for every circuit; Iz from a verified table for the actual installation method
- [ ] **RCD coverage** — every circuit either protected by RCD/RCBO with verified-required parameters, or exemption justified with citation
- [ ] **RCD types** — residual current and type (AC/A/F/B) appropriate for the loads served; nuisance-trip and fault-isolation trade-offs recorded
- [ ] **AFDD (ПВДП)** — applicability per ДБН В.2.5-23:2025 Додаток Д checked
- [ ] **Neutral topology** — no PEN inside the apartment; N downstream of each RCD isolated from other groups; grounding system stated by user, not inferred
- [ ] **PE continuity concept** — PE to every socket/fixed appliance; no switching or fusing in PE; bonding of wet-zone extraneous parts addressed
- [ ] **Bathroom / wet zones** — zones, equipment placement, IP, RCD per verified 60364-7-701 text (else UNRESOLVED)
- [ ] **Dedicated loads** — each high-power/fixed appliance on an adequate circuit; manufacturer requirements from real documentation only
- [ ] **Voltage drop** — computed per circuit (worst case), compared to a verified limit
- [ ] **Phase balance** (3-phase) — imbalance % reported from `elec_calc.py balance`
- [ ] **Load vs allocated power** — aggregate demand vs contract power; demand factors sourced
- [ ] **Panel capacity** — modules required (incl. reserve) ≤ enclosure size
- [ ] **SPD** — necessity/type/coordination assessed against building supply data (else UNRESOLVED)
- [ ] **Breaking capacity** — vs prospective fault current if known (else UNRESOLVED)
- [ ] **Assumptions register** — all ASSUMPTION items listed for user confirmation
- [ ] **Conflicts register** — any standard-vs-standard conflicts surfaced, not silently resolved

## Field verification required (always emit this list)

- [ ] Actual grounding system and PEN/PE/N arrangement at the building
- [ ] Insulation resistance testing
- [ ] Continuity of protective conductors
- [ ] Earth loop impedance / prospective fault current measurement
- [ ] RCD trip current and time testing
- [ ] Verification of upstream protection and building SPD
- [ ] Commissioning per applicable procedure

> This review is an engineering planning aid. It does not replace a licensed
> electrical designer where legally required, nor acceptance by a qualified
> electrician.
