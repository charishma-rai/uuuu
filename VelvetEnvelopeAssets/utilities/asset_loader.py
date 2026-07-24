import json
import os
from pathlib import Path
from typing import Dict, Any, List

class AssetLoader:
    """Scans UI assets, fonts, music, and crime scene templates."""

    def __init__(self, root_dir: str = None):
        if root_dir is None:
            root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.root_dir = Path(root_dir)
        self.ui_dir = self.root_dir / "assets" / "ui"
        self.crime_scene_dir = self.root_dir / "assets" / "crime_scene"

    def get_ui_manifest(self) -> Dict[str, Any]:
        manifest_path = self.ui_dir / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def load_crime_scene_templates(self) -> Dict[str, Any]:
        """Loads themes, locations, lighting, and weather prompt templates."""
        templates = {}
        for key in ["themes", "locations", "lighting", "weather"]:
            file_path = self.crime_scene_dir / f"{key}.json"
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    templates[key] = json.load(f).get(key, [])
        return templates
