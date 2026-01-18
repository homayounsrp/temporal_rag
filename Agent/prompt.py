"""Model and prompt configuration"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_model():
    return ChatOpenAI(
        model=os.getenv('MODEL_CHOICE', 'gpt-4o-mini'),
        openai_api_key=os.getenv('OPENAI_API_KEY')
    )


SYSTEM_PROMPT = """You are a helpful assistant with access to a temporal knowledge graph.
Use search_graphiti to find information.
Use add_episode_to_graphiti to add new information.
Be concise and helpful."""
