# Grounding and PE/N topology

## Inputs that must come from the user or building documentation

- Grounding system: TN-S / TN-C-S / TN-C / (rarely TT). **Never inferred**
  from building age or "typical practice". Unknown → every dependent
  decision (RCD guarantees, SPD connection scheme, PE origin) is UNRESOLVED
  and the deliverable says a field survey is required.
- PEN separation point (for TN-C-S): location and conductor sizes.
- Riser conductor arrangement (4- or 5-wire).

## Hard warnings (always include when relevant)

- **Never split, re-purpose, or fabricate a PEN inside an apartment.**
  Creating a local "ground" by bridging N to a socket PE (занулення на
  розетці), to plumbing, or to the panel enclosure is dangerous and defeats
  RCD protection. If the riser is TN-C (no PE available), the design must
  say so and route the resolution through the building owner/ОСББ and a
  qualified designer — not improvise.
- No switching devices, fuses, or removable links in PE.
- Downstream of every RCD, N is dedicated to that group; cross-connecting
  N between RCD groups causes nuisance trips and defeats protection.

## Design outputs

- PE bus: single, sized per verified rule (ДСТУ HD 60364-5-54 — cite only
  if excerpt available), all circuit PEs landed individually.
- N buses: one per RCD group + one for non-RCD circuits (if any legitimately exist).
- Supplementary bonding in wet zones: per bathrooms.md.
- Statement of the assumed system with its label, e.g.
  `ASSUMPTION: TN-C-S per building documentation dated …` or
  `UNRESOLVED (needs: grounding system from building survey)`.
