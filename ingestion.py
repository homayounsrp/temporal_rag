"""Ingestion module for adding episodes to the graph"""

import asyncio
import json
from datetime import datetime, timezone
from graphiti_core import Graphiti
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, LLM_CLIENT
from episodes import EPISODES


async def ingest_episodes(graphiti: Graphiti) -> None:
    """Add all episodes to the graph"""
    print("Adding episodes to graph...")
    for i, episode in enumerate(EPISODES):
        try:
            await graphiti.add_episode(
                name=f'Expedition Episode {i+1}',
                episode_body=episode['content'] if isinstance(episode['content'], str) else json.dumps(episode['content']),
                source=episode['type'],
                source_description=episode['description'],
                reference_time=datetime.now(timezone.utc),
            )
            print(f'Added episode: Expedition Episode {i+1} ({episode["type"].value})')
        except Exception as e:
            print(f'Warning: Error adding episode {i+1}: {e}')
            continue


async def main():
    """Initialize Graphiti, build indices, and ingest episodes"""
    graphiti = Graphiti(
        uri=NEO4J_URI,
        user=NEO4J_USER,
        password=NEO4J_PASSWORD,
        llm_client=LLM_CLIENT,
    )
    
    try:
        await graphiti.build_indices_and_constraints()
        print("Graphiti indices built successfully.\n")
        
        await ingest_episodes(graphiti)
        print("\nEpisodes ingested successfully!")
    
    finally:
        await graphiti.close()


if __name__ == "__main__":
    asyncio.run(main())
