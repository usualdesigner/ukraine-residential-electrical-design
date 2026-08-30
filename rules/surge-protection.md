# Surge protection (SPD / ПЗІП)

SPD architecture cannot be designed from apartment data alone. Required
inputs before any firm recommendation:

- building supply type (overhead/underground service, transformer proximity);
- existence and type of a building-level SPD (main switchboard);
- grounding system (rules/grounding.md);
- lightning protection system on the building (ДСТУ EN 62305 domain).

Missing → the SPD section is UNRESOLVED (needs: building supply data), plus
an ENGINEERING RECOMMENDATION describing what would typically be installed
and what data would confirm it. **Never assume an upstream SPD exists.**

Assessment order:

1. **Necessity** — check ДБН В.2.5-23:2025 excerpts (розділи 5, 7) and ДСТУ
   HD 60364-5-53 (protective devices selection; local text availability per
   `references/local/dstu-hd-60364/`, if populated) for when SPDs are required in
   dwellings. Quote or mark UNRESOLVED.
2. **Type/class** — Type 1 (lightning current, service entrance with LPS or
   overhead line exposure), Type 2 (switching/induced surges, distribution
   board), Type 3 (point of use, sensitive equipment). Assign per the
   building context, coordinated: an apartment Type 2/3 presumes energy
   coordination with the upstream stage — if upstream is unknown, say so.
3. **Coordination & backup protection** — SPD manufacturer specifies backup
   fuse/breaker rating and required coordination distances (MANUFACTURER
   REQUIREMENT — from datasheet only).
4. **Connection** — connecting conductor total length target (commonly
   ≤ 0.5 m, cite as COMMON INDUSTRY PRACTICE / manufacturer figure unless a
   verified clause is available); connection scheme (CT1/CT2, 3+1 for
   TN-C-S/TT) depends on the grounding system.
5. **Voltage monitoring relay** is not an SPD; overvoltage from a broken
   riser neutral (обрив нуля) is a distinct, common Ukrainian failure mode —
   a voltage monitoring relay addresses it (ENGINEERING RECOMMENDATION,
   widely used; check excerpts for any normative status before citing).
