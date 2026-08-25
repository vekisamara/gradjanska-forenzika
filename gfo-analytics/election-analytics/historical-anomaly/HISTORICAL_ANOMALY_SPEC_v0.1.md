# GFO Election Analytics — Historical Anomaly Engine v0.1

Status: **IMPLEMENTED**

## Purpose

Historical Anomaly Engine v0.1 produces separate, auditable deviation signals for a current polling-station observation against:

1. that polling station's historical baseline; and
2. its non-political peer-group reference.

The engine does **not** produce a composite anomaly score, fraud label, intent inference, legal conclusion, or LLM interpretation.

Statistical deviation is a screening signal only: an anomaly is a question, not an accusation.

## Inputs

The engine consumes:

- current election observations in the canonical Historical Baseline long-form format;
- reviewed polling-station mapping;
- historical polling-station baseline features;
- peer-group feature output from Peer Group Engine v0.1;
- explicit `current_election_id`.

Only mappings with `usable_for_baseline=true` and confidence at or above the configured threshold are used.

## Signals

For each mapped current polling station the engine may produce:

### Historical signals

- `historical_turnout_delta`
- `historical_turnout_z` when historical standard deviation is available and non-zero
- `historical_invalid_rate_delta`
- `historical_invalid_rate_z` when historical standard deviation is available and non-zero
- `registered_voter_change_pct`

### Peer signals

- `peer_turnout_delta`
- `peer_turnout_z`
- `peer_invalid_rate_delta`
- `peer_invalid_rate_z`

### Interaction signal

- `turnout_invalid_interaction = peer_turnout_z × peer_invalid_rate_z`

The interaction value is descriptive. It is not a probability, risk score, or finding of irregularity.

## Missing-data behavior

A signal is left null when its denominator or reference variance is unavailable. The engine must not manufacture variance or substitute arbitrary constants.

If a polling station lacks a historical baseline row, it is excluded from signal output and a warning is written.

If a peer reference is unavailable, historical signals remain valid while peer fields remain null.

## Comparability requirement

The engine is mechanically capable of comparing different election contexts, but substantive interpretation requires an explicit comparability decision upstream.

Election type, election timing, candidate field, legal context, turnout incentives and whether an election is general, early, repeat or partial-repeat can materially shift the entire distribution. A large signal created by such a context change must not be interpreted as a polling-station anomaly.

For this reason, validation of mechanics may use a non-comparable retrospective pair, but production anomaly interpretation must use a comparison set declared analytically comparable.

## Political variables

v0.1 does not use candidate, party or political-bloc variables. Candidate/bloc swing signals are deferred until an explicit cross-election political mapping exists.

## Outputs

```text
historical-anomaly-output/
├── historical_anomaly_signals.csv
├── validation_flags.csv
└── historical_anomaly_manifest.json
```

The manifest explicitly records:

- `composite_score_produced: false`
- `political_variables_used: false`

## Interpretation boundary

None of the following may be inferred from a signal alone:

- manipulation;
- fraud;
- intent;
- causality;
- illegality;
- responsibility of an individual or institution.

A signal only identifies a result that may deserve contextual or evidentiary review.
