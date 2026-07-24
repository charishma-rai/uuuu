import json
import os
from pathlib import Path
from typing import Dict, Any, List

class DialogueLoader:
    """Loads NPC dialogue style prompt templates from assets/dialogue/."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.dialogue_dir = self.root_dir / "assets" / "dialogue"

    def load_all_dialogue_styles(self) -> Dict[str, Dict[str, Any]]:
        styles = {}
        if not self.dialogue_dir.exists():
            return styles

        for file in sorted(self.dialogue_dir.glob("*.json")):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                style_name = data.get("style", file.stem)
                styles[style_name] = data
        return styles
