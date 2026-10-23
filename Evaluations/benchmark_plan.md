# Benchmark and Evaluation Plan

## 1. Objective

Measure preprocessing correctness, generated-analysis quality, model-call cost and latency, and dashboard usability separately. The benchmark must not treat correlation as proof of retention: the impact on retention requires a later experiment with users and an appropriate study design.

## 2. Scope and Components

1. **Preprocessing:** loading, tokenization, stopword removal, normalization, and vectorization.
2. **Tabular analyses:** frequencies, lengths, and TF-IDF terms, overall and by game.
3. **Topic classification:** `extract_game_features` output compared against human labels.
4. **Reports:** per-game JSON assessed for validity, coverage, faithfulness to reviews, and usefulness.
5. **Chat:** answers tested with known questions, questions without supporting evidence, and recommendation questions.
6. **Interface:** time to open/render views and complete analysis tasks.

## 3. Reference Dataset Preparation

- Pin the version, source, and hash of the five CSVs; record row counts, fields, nulls, duplicates, and distribution by game.
- Split by game.
- Draw stratified review samples and obtain two independent human labels for sentiment, topic, and evidence; adjudicate disagreements.
- Use a fixed subset for development and a separate, untouched set for final evaluation. Do not send personal data or credentials to external services.

## 4. Scenarios and Protocol

| Scenario | Input | Reference / comparison | Repetitions |
|---|---|---|---|
| Text transformations | synthetic sentences and fixed CSVs | expected outputs and type invariants | n per unit case |
| Batch preprocessing | fixed sample and full dataset | pandas/Scikit-learn baseline without an LLM | n runs per size |
| Topic classification | human-labeled sample | majority baseline and TF-IDF + Logistic Regression | n runs per configuration |
| Reports | sampled reviews for each game | human rubric and valid JSON/schema | n runs per game/configuration |
| Chat | fixed set of reference questions and answers | evidence-supported answers and unsupported-question scenarios | n runs per question |
| Dashboard | documented machine and environment | load/render time and memory usage | n runs per screen |

Pin the commit, Python version, dependencies, hardware, parameters, Ollama model version/quantization, and cache state. Separate cold-start time (model/data not loaded) from warm-start time. Record failures and timeouts; do not remove them from latency samples.

## 5. Metrics

- **Data and processing:** rows retained/dropped, missing-value coverage, tokens per second, total time, peak memory, and equality with expected outputs.
- **Classification:** precision, recall, macro and per-class F1, confusion matrix, and balanced accuracy.
- **Reports/chat:** JSON/schema validity, field coverage, citation/evidence precision, factual consistency, relevance, and unsupported-claim rate. Blind human evaluation using a 1–5 rubric for relevance, faithfulness, clarity, and usefulness.
- **Performance:** p50/p95 latency, throughput, error/timeout rate, and memory; record token counts and model resource consumption when available.
- **Interface:** load/render time, failures per session, and completion rate for tasks using a fixed script.

## 6. Proposed Acceptance Criteria

Establish a baseline before tuning the model. The following are initial gates, subject to product-owner approval:

- 100% of unit and schema cases pass.
- 100% of evaluated reports produce valid JSON matching the schema; failures count as failures, not as empty outputs.
- more...

An evaluation showing no improvement over the baseline should lead to a review of the data, labels, and method—not a declaration of success.

## 7. Execution and Reporting

1. Run unit tests: `python -m pytest tests/`.
2. Run the deterministic preprocessing benchmark first; save the environment and results as versioned evaluation artifacts.
3. Run local models only in a controlled environment; record prompts, parameters, and versions without storing secrets.
4. Repeat runs according to the table and calculate aggregates and confidence intervals.
5. Compare with baselines, analyze errors by game/class, and have evaluators review a sample of responses.

