import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

class PuzzleLoader:
    """Loads modular puzzles dynamically from category folders."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.puzzles_dir = self.root_dir / "puzzles"

    def load_all_puzzles(self) -> List[Dict[str, Any]]:
        """Scans all puzzle JSON templates across all 8 category directories."""
        puzzles = []
        if not self.puzzles_dir.exists():
            return puzzles

        for json_file in sorted(self.puzzles_dir.rglob("*.json")):
            with open(json_file, "r", encoding="utf-8") as f:
                puzzles.append(json.load(f))
        return puzzles

    def get_puzzles_by_category(self, category: str) -> List[Dict[str, Any]]:
        return [p for p in self.load_all_puzzles() if p.get("category") == category]

    def get_puzzles_by_difficulty(self, difficulty: str) -> List[Dict[str, Any]]:
        return [p for p in self.load_all_puzzles() if p.get("difficulty") == difficulty.lower()]

    def get_puzzles_for_evidence(self, evidence_type: str) -> List[Dict[str, Any]]:
        """Returns puzzles matching evidence context (e.g. 'Diary', 'Safe')."""
        matches = []
        for p in self.load_all_puzzles():
            recs = [r.lower() for r in p.get("recommended_for", [])]
            if any(evidence_type.lower() in r for r in recs):
                matches.append(p)
        return matches
