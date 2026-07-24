import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

class MetadataLoader:
    """Loads suspect and victim metadata dynamically without hardcoded paths."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.suspects_dir = self.root_dir / "assets" / "suspects"
        self.victims_dir = self.root_dir / "assets" / "victims"
        self.manifest_path = self.root_dir / "assets" / "manifest.json"

    def get_manifest(self) -> Dict[str, Any]:
        """Loads assets/manifest.json."""
        if not self.manifest_path.exists():
            return {}
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def load_all_suspects(self) -> List[Dict[str, Any]]:
        """Scans all suspect metadata JSON files in assets/suspects/."""
        suspects = []
        if not self.suspects_dir.exists():
            return suspects
        
        for file in sorted(self.suspects_dir.glob("*.json")):
            with open(file, "r", encoding="utf-8") as f:
                suspects.append(json.load(f))
        return suspects

    def load_all_victims(self) -> List[Dict[str, Any]]:
        """Scans all victim metadata JSON files in assets/victims/."""
        victims = []
        if not self.victims_dir.exists():
            return victims

        for file in sorted(self.victims_dir.glob("*.json")):
            with open(file, "r", encoding="utf-8") as f:
                victims.append(json.load(f))
        return victims

    def get_suspect_by_id(self, suspect_id: str) -> Optional[Dict[str, Any]]:
        for suspect in self.load_all_suspects():
            if suspect.get("id") == suspect_id:
                return suspect
        return None

    def get_victim_by_id(self, victim_id: str) -> Optional[Dict[str, Any]]:
        for victim in self.load_all_victims():
            if victim.get("id") == victim_id:
                return victim
        return None
