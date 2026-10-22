# Problem Definition — Gacha Reviews

## Problem

Players and product teams need to understand what people praise or criticize about gacha games. Reviews are distributed by game and written as free text, making it difficult to compare themes, identify points of friction, and quickly find useful information for players.

## Goal

Bring together processed reviews for five games — Genshin Impact, Honkai: Star Rail, Zenless Zone Zero, Wuthering Waves, and Blue Archive — and provide exploratory analyses and language-model-assisted summaries. The application aims to support understanding of player experience; it does not measure retention or demonstrate that recommendations reduce churn.

## Current Application Status

- The preprocessing layer provides tokenization, stopword removal, spelling correction (dependent on `pyspellchecker`), lemmatization or stemming, and Bag-of-Words/TF-IDF vectorization. `pyspellchecker` is not declared in `requeriments.txt` and was not found in the interpreter selected during this task.
- The Streamlit dashboard presents word clouds, frequent tokens and sentences, review lengths, and TF-IDF terms for the full dataset and by game.
- The report generator sends reviews for a game to an Ollama model and expects JSON containing a summary and sections for story, gameplay, characters, events, design, gacha, pros, and cons.
- A topic classification function queries Ollama for each review.
- A LangChain/LangGraph agent-based chat is configured to answer questions about the games.
- The repository contains sentiment algorithm selectors, but no implemented training or evaluation pipeline.

## Out of Scope or Not Yet Demonstrated

Personalized recommendations, RAG retrieval integrated with a vector database, and proven improvements in retention are not demonstrated by the current executable flow. Topic classification, reports, and chat depend on a locally available Ollama model; factual quality and latency are not guaranteed. Test coverage and label quality still need to be measured.

## Inputs and Outputs

- **Inputs:** processed CSV files in `Datasets/`, with the `content` column used by text workflows; the loader adds the `game` column.
- **Outputs:** descriptive tables and charts, TF-IDF-weighted terms, topic classes, and model-assisted JSON reports.

## Success Criteria to Evaluate

1. Processing preserves expected data and types and produces reproducible results for controlled inputs.
2. Analyses and reports identify relevant themes with quality measured against an annotated reference set.
3. Dashboard and model-call latency, failure rate, and resource usage are recorded in representative scenarios.
4. Recommendations and retention benefits should only be considered after implementation and evaluation with appropriate users and data.
