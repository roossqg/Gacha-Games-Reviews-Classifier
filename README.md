# Gacha Review Analyst & AI Support 

An exploratory **Data application** for processed reviews of five gacha games (Genshin Impact,Honkai Star Rail,Zenless Zone Zero,Wuthering Waves,Blue Archive) with an **AI Chatbot**. It provides Graphs of NLP,resumes about each game aspect and one Specialized Customer Chatbot with gacha games knowledge.

The purpouse is to analyst users behavior and opinion about the games,which can provide insights that lead improvements in game features.

Specialized chabot provide support to users,helping with the game features,resuming aspects of game,etc.

## Features
1. **Explore reviews**: descriptive NLP outputs include frequent tokens and sentences, review lengths, word clouds, and TF-IDF terms, overall and by game.create review labels by its content such as __Topic__: what is discussed and __Sentiment__: emotional reaction.

- **Topic Classification**: Classification of each review in topic labels by its content.topics are the aspects which will be compared in graphs and used in __Sentiment Analyst__.  
- **Sentiment Analyst**: Understand user emotional reactions against Game aspects.provide graphs with overview of counts-frequencies to compare each aspect.

2. **Generate model-assisted reports**: a local Ollama model is asked to return a structured report for a game. Output quality and factual grounding still need evaluation.

3. **Chat interface**: an experimental local-LLM chat to user interact.

4. **Vector-search & Context Engineering**: gacha games context to the llm customer chatbot.

### Flow 

    Processed datasets -> NLP -> descriptive dashboard
    Processed reviews -> local Ollama -> structured report (experimental)
    ChromaDB scripts + Tolls + Reviews -> LLM customer chatbot
    Local Ollama -> experimental chat interface 

## Tech

- Python & Pytest: Application logic and Validation
- Pydantic: Structured data models
- spaCy & Pandas: NLP processing
- ChromaDB: vector storage prototype
- Sentence Transformers: local embedding model
- Langchain: Agent architecture
- Streamlit: Interface | Dashboard

### Local model

- The report and chat code uses a quantized Llama model served by Ollama.
- Embedding generation is a separate step and should be benchmarked before indexing larger datasets.

### Architecture

#### Directories

## Data Models and Computing

### Data Source: 
Dataset source: https://www.kaggle.com/datasets/jeremypurukan/gacha-game-review
privided by: https://www.kaggle.com/jeremypurukan

### Schemas
### Preprocessing
### Models & Algorithms used

### Evaluation methods:
Evaluations\benchmark_plan.md


## Quick Start
### Prerequisites
### Install-config
### usage
### tests


