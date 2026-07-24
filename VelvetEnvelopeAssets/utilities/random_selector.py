import random
from typing import List, Dict, Any, Optional
from .metadata_loader import MetadataLoader
from .puzzle_loader import PuzzleLoader
from .story_loader import StoryLoader

class RandomSelector:
    """Random sampling helper for suspects, victims, puzzles, and stories."""

    def __init__(self, root_dir: str = None):
        self.meta_loader = MetadataLoader(root_dir)
        self.puzzle_loader = PuzzleLoader(root_dir)
        self.story_loader = StoryLoader(root_dir)

    def select_random_suspects(self, count: int = 4, gender_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """Randomly selects suspects. Used by notebook before calling LLM story generator."""
        suspects = self.meta_loader.load_all_suspects()
        if gender_filter:
            suspects = [s for s in suspects if s.get("gender") == gender_filter]
        if len(suspects) < count:
            return suspects
        return random.sample(suspects, count)

    def select_random_victim(self) -> Optional[Dict[str, Any]]:
        victims = self.meta_loader.load_all_victims()
        return random.choice(victims) if victims else None

    def select_random_puzzle(self, category: Optional[str] = None, difficulty: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Selects a random puzzle matching requested category or difficulty."""
        puzzles = self.puzzle_loader.load_all_puzzles()
        if category:
            puzzles = [p for p in puzzles if p.get("category") == category]
        if difficulty:
            puzzles = [p for p in puzzles if p.get("difficulty", "").lower() == difficulty.lower()]
        return random.choice(puzzles) if puzzles else None

    def select_random_story(self, difficulty: Optional[str] = None) -> Optional[Dict[str, Any]]:
        stories = self.story_loader.load_all_stories()
        if difficulty:
            stories = [s for s in stories if s.get("difficulty", "").lower() == difficulty.lower()]
        return random.choice(stories) if stories else None
