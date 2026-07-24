import json
import os
from pathlib import Path
from typing import Dict, Any, List

class RepositoryValidator:
    """Validates repository files and JSON schemas against root game_schema.json."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            # Default to parent directory of utilities
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

        # Scan and validate schema_version on all JSON files
        for json_file in self.root_dir.rglob("*.json"):
            if json_file.name == "game_schema.json":
                continue
            results["checked_files"] += 1
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict) and "schema_version" not in data:
                    results["errors"].append(f"Missing 'schema_version' in {json_file.relative_to(self.root_dir)}")
            except Exception as e:
                results["valid"] = False
                results["errors"].append(f"Invalid JSON format in {json_file.relative_to(self.root_dir)}: {str(e)}")

        if results["errors"]:
            results["valid"] = False

        return results

if __name__ == "__main__":
    validator = RepositoryValidator()
    report = validator.validate_repository()
    print("Repository Validation Report:")
    print(json.dumps(report, indent=2))
