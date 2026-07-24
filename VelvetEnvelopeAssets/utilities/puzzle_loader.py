import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

CATEGORIES = [
    "cipher",
    "riddles",
    "logic",
    "timeline",
    "hidden_messages",
    "code_breaking",
    "witness_statements",
    "evidence_analysis"
]

CATEGORY_DISPLAY_NAMES = {
    "cipher": "🔐 Cipher",
    "riddles": "🧩 Detective Riddles",
    "logic": "🧠 Logic Deduction",
    "timeline": "⏳ Timeline Reconstruction",
    "hidden_messages": "🕵️ Hidden Messages",
    "code_breaking": "🔢 Code Breaking",
    "witness_statements": "📝 Witness Statements",
    "evidence_analysis": "📄 Evidence Analysis"
}

class PuzzleLoader:
    """Loads, filters, presents, and validates data-driven puzzles for Velvet Envelope."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.puzzles_dir = self.root_dir / "puzzles"

    def load_all_puzzles(self) -> List[Dict[str, Any]]:
        """Scans and loads all 120 new puzzle JSON files across the 8 category directories."""
        puzzles = []
        if not self.puzzles_dir.exists():
            return puzzles

        for cat in CATEGORIES:
            cat_dir = self.puzzles_dir / cat
            if cat_dir.exists():
                for json_file in sorted(cat_dir.glob(f"{cat}_*.json")):
                    try:
                        with open(json_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            if isinstance(data, dict) and "id" in data and len(data.get("hints", [])) == 3:
                                puzzles.append(data)
                    except Exception as e:
                        print(f"Error reading puzzle {json_file}: {e}")
        return puzzles

    def get_puzzles_by_category(self, category: str) -> List[Dict[str, Any]]:
        cat_lower = category.lower().strip()
        return [p for p in self.load_all_puzzles() if p.get("category", "").lower() == cat_lower]

    def get_puzzles_by_difficulty(self, difficulty: str) -> List[Dict[str, Any]]:
        diff_lower = difficulty.lower().strip()
        return [p for p in self.load_all_puzzles() if p.get("difficulty", "").lower() == diff_lower]

    def validate_answer(self, puzzle: Dict[str, Any], user_answer: str) -> bool:
        """Validates player answer against solution key using flexible normalization."""
        if not puzzle or "answer" not in puzzle or user_answer is None:
            return False
        
        target = str(puzzle["answer"]).strip().upper()
        given = str(user_answer).strip().upper()
        
        if given == target:
            return True
            
        target_clean = "".join(c for c in target if c.isalnum() or c.isspace())
        given_clean = "".join(c for c in given if c.isalnum() or c.isspace())
        
        return target_clean == given_clean

    def get_hint(self, puzzle: Dict[str, Any], hint_index: int) -> str:
        """Returns requested hint (1, 2, or 3) for a puzzle."""
        hints = puzzle.get("hints", [])
        if 1 <= hint_index <= len(hints):
            return f"💡 Hint {hint_index}: {hints[hint_index - 1]}"
        return "No further hints available."

    def format_puzzle_presentation(self, puzzle: Dict[str, Any]) -> str:
        """Formats puzzle with evidence discovery header for Velvet Envelope detective vibe."""
        cat = puzzle.get("category", "")
        cat_name = CATEGORY_DISPLAY_NAMES.get(cat, cat.title())
        diff = puzzle.get("difficulty", "medium").upper()
        
        header = (
            f"\n"
            f"===============================================================\n"
            f"🕵️ VELVET ENVELOPE — CASE EVIDENCE FILE [{puzzle.get('id', 'N/A')}]\n"
            f"Category: {cat_name} | Difficulty: [{diff}]\n"
            f"Title: {puzzle.get('title', 'Untitled')}\n"
            f"===============================================================\n\n"
            f"{puzzle.get('description', '')}\n\n"
            f"❓ INVESTIGATION QUESTION:\n"
            f"{puzzle.get('question', '')}\n"
            f"---------------------------------------------------------------\n"
        )
        return header
