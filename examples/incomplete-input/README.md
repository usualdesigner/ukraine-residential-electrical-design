# EXAMPLE — incomplete input

`input.yaml` has loads but no supply data. Expected skill behavior:

- proceeds with what is decidable (circuit grouping, Ib per circuit,
  minimum-section reasoning, RCD/AFDD reasoning per rules);
- emits a missing-information register (phases, allocated power, grounding
  system, installation methods, lengths, …);
- marks every dependent decision `UNRESOLVED (needs: …)`;
- invents nothing — no phases, no grounding topology, no cable lengths.

If the skill produces a "complete" design from this input, that is a bug.
