import json
import os
from pathlib import Path
from typing import List, Dict, Any

class EvidenceLoader:
    """Loads central evidence catalogs from assets/evidence/."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.evidence_dir = self.root_dir / "assets" / "evidence"

    def load_all_evidence_categories(self) -> Dict[str, List[Dict[str, Any]]]:
        catalog = {}
        if not self.evidence_dir.exists():
            return catalog

        for file in sorted(self.evidence_dir.glob("*.json")):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                category = data.get("category", file.stem)
                catalog[category] = data.get("items", [])
        return catalog
