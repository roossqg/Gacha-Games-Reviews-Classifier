# Gacha Review Analyst

Ai system which classify reviews from gacha games using scores/summary and group them for a better overview.

## Features
1. Classify gacha review based on its content
2. Get similar-Keywords reviews using RAG (Grouping)

## Tech

- Chromadb: Vector storage and search
- Sentence Transformer: Free embedding models


- The time for computing embeddings with local model is long,so i will use just 1000 embeddings from **wuwa** dataset for this first experiment.

dataset from: https://www.kaggle.com/datasets/jeremypurukan/gacha-game-review

