"""Neo4j and LLM configuration"""

import os
from dotenv import load_dotenv
from graphiti_core.llm_client import OpenAIClient, LLMConfig

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

LLM_CLIENT = OpenAIClient(
    config=LLMConfig(
        model=os.getenv("LLM_MODEL", "gpt-4o-mini")
    )
)
