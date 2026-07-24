# Velvet Envelope Assets & Content Pack (`VelvetEnvelopeAssets`)

`VelvetEnvelopeAssets` is the lightweight, data-driven content library and puzzle pack for **Velvet Envelope**, an AI detective game.

The notebook/game engine loads all UI, graphics, and interactive interfaces dynamically at runtime. This repository stores only game metadata, suspect/victim profiles, predefined case stories, and puzzle engine templates.

No decorative UI graphics or placeholder images are included. All image filenames referenced in JSON files (`suspect_001.png`, `victim_001.png`) will be added manually to their respective folders.

---

## 📂 Repository Structure

```
VelvetEnvelopeAssets/
├── game_schema.json           # Repository schema specification
├── README.md                  # Master documentation
├── assets/
│   ├── manifest.json          # Repository manifest (counts & versioning)
│   ├── suspects/              # Suspect metadata JSON files (suspect_001.json .. suspect_020.json)
│   └── victims/               # Victim metadata JSON files (victim_001.json .. victim_006.json)
├── stories/                   # Predefined case stories (story_001.json .. story_006.json)
├── puzzles/                   # Modular puzzle engine (8 category folders)
│   ├── riddles/
│   ├── logic/
│   ├── cipher/
│   ├── memory/
│   ├── observation/
│   ├── timeline/
│   ├── matching/
│   └── sorting/
└── utilities/                 # Python loader scripts
    ├── __init__.py
    ├── asset_loader.py
    ├── metadata_loader.py
    ├── puzzle_loader.py
    ├── story_loader.py
    └── random_selector.py
```

---

## 📖 Content Management & Extension Guide

Everything is fully modular. Adding new content requires dropping files into their respective folders—no notebook or engine code changes are required.

### 1. How to Add a New Suspect
1. Place the suspect metadata JSON file in `assets/suspects/` (e.g. `suspect_021.json`):
```json
{
  "schema_version": "1.0",
  "id": "suspect_021",
  "image_filename": "suspect_021.png",
  "gender": "female",
  "age_group": "young_adult",
  "approximate_age": 26,
  "ethnicity": "caucasian",
  "appearance": {
    "hair": "dark_updo",
    "eye_color": "green",
    "facial_hair": "none",
    "clothing_style": "victorian_riding_habit",
    "accessories": ["leather_gloves"]
  },
  "appearance_description": "An athletic equestrian in a dark velvet riding habit.",
  "height": "5 ft 8 in",
  "body_type": "athletic",
  "dominant_hand": "right",
  "walking_style": "brisk pace",
  "voice": "clear soprano",
  "accent": "English Country",
  "allowed_occupations": ["Equestrian", "Stable Master"],
  "personality_tags": ["bold", "headstrong"],
  "story_tags": ["stables", "manor"],
  "possible_relationships": ["Niece", "Rival"]
}
```
2. Manually add `suspect_021.png` artwork into `assets/suspects/`.

### 2. How to Add a New Victim
1. Place the victim metadata JSON file in `assets/victims/` (e.g. `victim_007.json`):
```json
{
  "schema_version": "1.0",
  "id": "victim_007",
  "image_filename": "victim_007.png",
  "name": "Sir Charles Vance",
  "occupation": "Railroad Baron",
  "short_backstory": "Discovered dead in his private locomotive lounge car.",
  "recommended_story_title": "The Iron Express Tragedy",
  "recommended_location": "Vance Rail Parlor Car",
  "recommended_theme": "Orient Express Parlor Car"
}
```
2. Manually add `victim_007.png` artwork into `assets/victims/`.

### 3. How to Add a New Story
Place a new case story JSON file in `stories/` (e.g. `story_007.json`):
```json
{
  "schema_version": "1.0",
  "id": "story_007",
  "title": "The Iron Express Tragedy",
  "difficulty": "Medium",
  "victim_id": "victim_007",
  "victim_image_filename": "victim_007.png",
  "suspect_ids": ["suspect_008", "suspect_010", "suspect_014"],
  "location": "Vance Rail Parlor Car",
  "weapon": "Poisoned Cigar",
  "motive": "Contested railroad expansion contracts",
  "timeline": [
    { "time": "09:00 PM", "event": "Train departs station." },
    { "time": "10:30 PM", "event": "Vance retires to his private car." },
    { "time": "11:00 PM", "event": "Conductor finds Vance unresponsive." }
  ],
  "evidence_list": [
    {
      "id": "ev_08",
      "name": "Cigar Band",
      "puzzle_type": "Pattern Recognition",
      "puzzle_id": "logic_003"
    }
  ],
  "dialogue_placeholders": {
    "suspect_008": "I was in the dining car discussing stocks.",
    "suspect_010": "Vance cut off funding for our expedition."
  }
}
```

### 4. How to Add a New Puzzle
Create a new puzzle JSON file in the appropriate category directory under `puzzles/` (e.g., `puzzles/riddles/riddle_006.json`):
```json
{
  "schema_version": "1.0",
  "id": "riddle_006",
  "category": "riddles",
  "puzzle_type": "Riddles",
  "difficulty": "easy",
  "title": "The Broken Pocket Watch",
  "question": "What has hands but cannot grip?",
  "answer": "A clock",
  "solution": "clock",
  "hint": "Check the victim's vest pocket.",
  "time_limit": 45,
  "reward_points": 50,
  "recommended_for": ["Pocket Watch", "Timepiece"]
}
```

---

## 🛠️ Python Utilities

Load content programmatically using the `utilities/` package:

```python
from utilities import MetadataLoader, PuzzleLoader, StoryLoader, RandomSelector

# Load metadata
meta = MetadataLoader()
suspects = meta.load_all_suspects()
victims = meta.load_all_victims()

# Select 4 random suspects for LLM narrative generation
selector = RandomSelector()
sampled = selector.select_random_suspects(count=4)

# Load stories and puzzles
story_loader = StoryLoader()
puzzles_loader = PuzzleLoader()
```
