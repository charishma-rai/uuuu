import json
import os
from pathlib import Path
from typing import Dict, Any

REQUIRED_PUZZLE_FIELDS = [
    "id", "title", "category", "difficulty",
    "description", "question", "answer", "hints", "solution"
]

VALID_CATEGORIES = [
    "cipher", "riddles", "logic", "timeline",
    "hidden_messages", "code_breaking", "witness_statements", "evidence_analysis"
]

class RepositoryValidator:
    """Validates repository files and JSON schemas against root game_schema.json."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.schema_path = self.root_dir / "game_schema.json"

    def load_game_schema(self) -> Dict[str, Any]:
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Root schema file not found at {self.schema_path}")
        with open(self.schema_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def validate_repository(self) -> Dict[str, Any]:
        schema = self.load_game_schema()
        results = {
            "valid": True,
            "errors": [],
            "checked_files": 0,
            "checked_directories": []
        }

        # Check required directories
        for req_dir in schema.get("required_asset_directories", []):
            dir_path = self.root_dir / req_dir
            if not dir_path.exists():
                results["valid"] = False
                results["errors"].append(f"Missing required directory: {req_dir}")
            else:
                results["checked_directories"].append(req_dir)

        # Scan and validate all JSON files in the 8 puzzle categories
        puzzles_dir = self.root_dir / "puzzles"
        for cat in VALID_CATEGORIES:
            cat_dir = puzzles_dir / cat
            if not cat_dir.exists():
                results["errors"].append(f"Missing puzzle category directory: {cat}")
                continue

            for json_file in cat_dir.glob(f"{cat}_*.json"):
                results["checked_files"] += 1
                try:
                    with open(json_file, "r", encoding="utf-8") as f:
                        data = json.load(f)

                    for field in REQUIRED_PUZZLE_FIELDS:
                        if field not in data:
                            results["errors"].append(f"Puzzle {json_file.name} missing required field '{field}'")

                    if "hints" in data:
                        if not isinstance(data["hints"], list) or len(data["hints"]) != 3:
                            results["errors"].append(f"Puzzle {json_file.name} must have exactly 3 hints")

                    cat_val = data.get("category", "").lower()
                    if cat_val != cat:
                        results["errors"].append(f"Puzzle {json_file.name} category '{cat_val}' does not match directory '{cat}'")

                except Exception as e:
                    results["errors"].append(f"Invalid JSON format in {json_file.relative_to(self.root_dir)}: {str(e)}")

        if results["errors"]:
            results["valid"] = False

        return results
