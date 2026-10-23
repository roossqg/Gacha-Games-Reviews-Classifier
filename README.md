# Gacha Review Analyst

An exploratory application for processed reviews of five gacha games. It currently provides descriptive NLP dashboards and experimental local-LLM reports/chat. It does not yet demonstrate validated sentiment classification, review-grounded RAG, personalized recommendations, or retention impact.

## Features
1. **Explore reviews**: descriptive NLP outputs include frequent tokens and sentences, review lengths, word clouds, and TF-IDF terms, overall and by game.

2. **Generate model-assisted reports**: a local Ollama model is asked to return a structured report for a game. Output quality and factual grounding still need evaluation.

3. **Chat interface**: an experimental local-LLM chat is present, but the current flow does not retrieve supporting reviews from the vector database.

4. **Vector-search prototype**: scripts for ChromaDB and Sentence Transformers exist; ingestion and retrieval are not yet integrated into the chat or report flow.

## Flow 

    Processed datasets -> NLP -> descriptive dashboard
    Processed reviews -> local Ollama -> structured report (experimental)
    ChromaDB scripts -> vector-search prototype (not integrated with chat)
    Local Ollama -> experimental chat interface

## Tech

- ChromaDB: vector storage prototype
- Sentence Transformers: local embedding model

### Local model

- The report and chat code uses a quantized Llama model served by Ollama.
- Embedding generation is a separate step and should be benchmarked before indexing larger datasets.

Dataset source: https://www.kaggle.com/datasets/jeremypurukan/gacha-game-review
