import json
import os
from pathlib import Path
from typing import Dict, Any, List

class AssetLoader:
    """Helper class to load top-level asset manifests and file listings."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.assets_dir = self.root_dir / "assets"

    def get_manifest(self) -> Dict[str, Any]:
        """Loads assets/manifest.json."""
        manifest_path = self.assets_dir / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def list_suspect_files(self) -> List[str]:
        """Returns filenames of suspect metadata files."""
        suspects_dir = self.assets_dir / "suspects"
        if not suspects_dir.exists():
            return []
        return [f.name for f in sorted(suspects_dir.glob("*.json"))]

    def list_victim_files(self) -> List[str]:
        """Returns filenames of victim metadata files."""
        victims_dir = self.assets_dir / "victims"
        if not victims_dir.exists():
            return []
        return [f.name for f in sorted(victims_dir.glob("*.json"))]
