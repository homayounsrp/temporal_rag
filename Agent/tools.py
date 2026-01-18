"""Simple tools for Graphiti agent"""

from typing import Annotated, Optional
import json
from datetime import datetime, timezone

from langchain_core.tools import tool
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType


# Global Graphiti client
_graphiti_client: Optional[Graphiti] = None

def set_graphiti_client(client: Graphiti):
    global _graphiti_client
    _graphiti_client = client

def get_graphiti_client() -> Graphiti:
    return _graphiti_client


@tool
async def search_graphiti(query: Annotated[str, "Search query for the knowledge graph"]) -> str:
    """Search the Graphiti knowledge graph."""
    graphiti = get_graphiti_client()
    results = await graphiti.search(query)
    
    if not results:
        return "No results found."
    
    formatted = [{"fact": r.fact, "uuid": r.uuid} for r in results]
    return json.dumps(formatted, indent=2)


@tool
async def add_episode_to_graphiti(
    name: Annotated[str, "Episode name"],
    content: Annotated[str, "Episode content"]
) -> str:
    """Add a new episode to the knowledge graph."""
    graphiti = get_graphiti_client()
    
    await graphiti.add_episode(
        name=name,
        episode_body=content,
        source=EpisodeType.text,
        source_description="Added via agent",
        reference_time=datetime.now(timezone.utc),
    )
    
    return f"Successfully added episode: {name}"


# Export tools
graphiti_tools = [search_graphiti, add_episode_to_graphiti]
