# TemporalRAG

Simple Graphiti knowledge graph demo with LLM agent for querying and updating the knowledge graph.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create `.env` with Neo4j credentials and OpenAI API key:
   ```
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_password
   OPENAI_API_KEY=your_openai_api_key
   LLM_MODEL=gpt-4o-mini  # Optional, defaults to gpt-4o-mini
   ```
3. Ingest episodes: `python ingestion.py`
4. Run the interactive LLM agent: `python main.py`

## Features

- **Ingestion** (`ingestion.py`): Ingests episodes into the knowledge graph
- **LLM Agent** (`main.py`): Interactive agent that can:
  - Search the knowledge graph to answer questions
  - Add new episodes to update the graph
  - Handle both text and JSON episode types

## LLM Agent Usage

The LLM agent provides an interactive interface where you can:
- Ask questions about the data in the knowledge graph
- Request to add or update information in the graph
- The agent will use its tools to search and update data as needed

Example queries:
- "What is the Pacific Deep Sea Expedition?"
- "Add a new episode: In July 2024, a new species was discovered."
- "Who leads the expedition?"
