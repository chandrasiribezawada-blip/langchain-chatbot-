# Local LangChain Chatbot (No API Key)

This is a chatbot built using LangChain and a local LLM via Ollama. No OpenAI API key is required.

## Setup

### 1. Install Ollama
Download from: https://ollama.com

### 2. Pull a model
ollama pull llama3

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run Ollama
ollama run llama3

### 5. Run app
streamlit run app.py

## Features
- Fully offline chatbot
- Conversation memory
- Streamlit UI
