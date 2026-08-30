# Gacha Review Analyst

Ai system which analyses gacha reviews using **NLP** and **Sentiment Analyst** to get insights about Users experience and provides an Ai with **Rag** to recomend games and sugest improvements.

## Features
1. **Classify gacha review based on its content**: using Nlp techniques,we will extract specifc feature informations about user experience and create dashboards to help in decision-making.

2. **Get similar-Keywords reviews using RAG (Grouping)**: Ai will process reviews data and respond some questions about using Rag.we can extract some new features about data and pattners. 

3. **Reviews Chatbot**: Also using Rag with Wiki informations about each game and its reviews,ai can provide recommendations,discuss or to analyze a specifc game. 

## Tech

- Chromadb: Vector storage and search
- Sentence Transformer: Free embedding models


- The time for computing embeddings with local model is long,so i will use just 1000 embeddings from **wuwa** dataset for this first experiment.

dataset from: https://www.kaggle.com/datasets/jeremypurukan/gacha-game-review

