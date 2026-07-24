import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

class StoryLoader:
    """Loads sample case stories and binds suspect/victim metadata."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.stories_dir = self.root_dir / "stories"

    def load_all_stories(self) -> List[Dict[str, Any]]:
        stories = []
        if not self.stories_dir.exists():
            return stories

        for file in sorted(self.stories_dir.glob("*.json")):
            with open(file, "r", encoding="utf-8") as f:
                stories.append(json.load(f))
        return stories

    def get_story_by_id(self, story_id: str) -> Optional[Dict[str, Any]]:
        for story in self.load_all_stories():
            if story.get("id") == story_id:
                return story
        return None

    def get_stories_by_difficulty(self, difficulty: str) -> List[Dict[str, Any]]:
        return [s for s in self.load_all_stories() if s.get("difficulty", "").lower() == difficulty.lower()]
