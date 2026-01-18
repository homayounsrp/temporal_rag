"""Episode data for the knowledge graph"""

from graphiti_core.nodes import EpisodeType


EPISODES = [
    # Initial state - Dr. Chen at Stanford (2018)
    {
        'content': 'In 2018, Dr. Sarah Chen was a research scientist at Stanford University. She was studying coastal marine ecosystems and teaching undergraduate biology courses.',
        'type': EpisodeType.text,
        'description': 'career history - 2018',
    },
    # State change - Dr. Chen moves to Woods Hole (2020)
    {
        'content': 'In 2020, Dr. Sarah Chen left Stanford University to join Woods Hole Oceanographic Institution as a Senior Researcher. She shifted her focus to deep sea bioluminescence.',
        'type': EpisodeType.text,
        'description': 'career history - 2020',
    },
    # State change - Dr. Chen joins expedition (2024)
    {
        'content': 'In 2024, Dr. Sarah Chen left Woods Hole Oceanographic Institution to lead the Pacific Deep Sea Expedition as Lead Marine Biologist. She is now based on the research vessel Ocean Explorer.',
        'type': EpisodeType.text,
        'description': 'career history - 2024',
    },
    # Captain Mitchell history
    {
        'content': 'Captain James Mitchell served as First Officer on the research vessel "Neptune" from 2010 to 2018. During this period, he participated in over 50 deep sea research missions.',
        'type': EpisodeType.text,
        'description': 'captain history - 2010-2018',
    },
    # Captain Mitchell promotion
    {
        'content': 'In 2019, Captain James Mitchell was promoted to Captain and took command of the research vessel "Ocean Explorer". He has been the commanding officer ever since.',
        'type': EpisodeType.text,
        'description': 'captain history - 2019',
    },
    # Expedition status changes
    {
        'content': {
            'name': 'Pacific Deep Sea Expedition',
            'status': 'Planning Phase',
            'start_date': 'January 2024',
            'location': 'San Diego Harbor',
            'lead_scientist': 'Dr. Sarah Chen',
            'vessel': 'Ocean Explorer',
        },
        'type': EpisodeType.json,
        'description': 'expedition status - January 2024',
    },
    {
        'content': 'In March 2024, the Pacific Deep Sea Expedition departed San Diego Harbor and entered the Active Research phase. The vessel is now operating in the Pacific Ocean near the Mariana Trench.',
        'type': EpisodeType.text,
        'description': 'expedition status - March 2024',
    },
    # Species discovery timeline
    {
        'content': 'In April 2024, the expedition observed an unidentified bioluminescent jellyfish species at 3000 meters depth. The species was given temporary designation "Species X-1" pending further study.',
        'type': EpisodeType.text,
        'description': 'discovery - April 2024',
    },
    {
        'content': 'In June 2024, after DNA analysis and morphological study, Species X-1 was officially named "Aurelia profundis". The species status changed from "Unidentified" to "Formally Described".',
        'type': EpisodeType.text,
        'description': 'discovery - June 2024',
    },
    # Funding changes
    {
        'content': 'The initial expedition funding of $1.5 million was provided by the Marine Science Foundation in late 2023. This covered equipment preparation and initial crew hiring.',
        'type': EpisodeType.text,
        'description': 'funding - 2023',
    },
    {
        'content': 'In May 2024, the expedition received an additional $1 million grant from the National Science Foundation, bringing total funding to $2.5 million. This extended the expedition duration from 4 months to 6 months.',
        'type': EpisodeType.text,
        'description': 'funding - May 2024',
    },
    # Location changes for team
    {
        'content': {
            'name': 'Dr. Sarah Chen',
            'current_location': 'Pacific Ocean - Mariana Trench Region',
            'previous_location': 'San Diego Harbor',
            'role': 'Lead Marine Biologist',
            'vessel': 'Ocean Explorer',
            'as_of': 'March 2024',
        },
        'type': EpisodeType.json,
        'description': 'scientist location - March 2024',
    },
]
