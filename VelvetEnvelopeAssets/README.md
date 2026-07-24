# Velvet Envelope Assets & Content Pack (`VelvetEnvelopeAssets`)

![Velvet Envelope Asset Library](https://img.shields.io/badge/VelvetEnvelope-AssetPack%20v1.0.0-gold) ![Plug & Play](https://img.shields.io/badge/Architecture-Plug--and--Play-blue) ![Data Driven](https://img.shields.io/badge/Engine-Data--Driven-green)

`VelvetEnvelopeAssets` is the official modular content library and puzzle engine for **Velvet Envelope**, an AI-driven detective mystery game.

This repository serves as a **plug-and-play asset pack**. External game engines, Python notebooks, or LLM narrative pipelines can dynamically scan this repository at runtime to load suspect portraits, physical metadata, victims, sample cases, context-mapped puzzles, dialogue styles, and UI elements **without requiring code changes**.

---

## 🏛️ Repository Architecture

```
VelvetEnvelopeAssets/
├── game_schema.json               # Root repository schema validation rules
├── README.md                      # Primary documentation
├── assets/
│   ├── manifest.json              # Repository manifest & asset counts
│   ├── suspects/                  # Flat directory: suspect_001.json .. suspect_020.json
│   ├── victims/                   # victim_001.json .. victim_006.json
│   ├── crime_scene/               # Prompt templates (themes, locations, lighting, weather)
│   ├── evidence/                  # Shared evidence catalogs (weapons, documents, etc.)
│   ├── dialogue/                  # NPC dialogue behavioral style prompt templates
│   ├── ui/                        # UI categories, manifests, and resolution guides
│   │   ├── manifest.json
│   │   ├── backgrounds/
│   │   ├── folders/
│   │   ├── paper/
│   │   ├── wax_seals/
│   │   ├── buttons/
│   │   ├── icons/
│   │   ├── textures/
│   │   ├── bookmarks/
│   │   ├── pins/
│   │   ├── coffee_stains/
│   │   └── stamps/
│   ├── music/                     # Audio track specifications (intro.mp3, investigation.mp3)
│   └── fonts/                     # Typography guide (Playfair Display, Cinzel, Special Elite)
├── stories/                       # Predefined sample mystery cases (story_001.json .. story_006.json)
├── puzzles/                       # Modular puzzle engine (8 category directories with 40+ templates)
│   ├── riddles/
│   ├── logic/
│   ├── cipher/
│   ├── memory/
│   ├── observation/
│   ├── timeline/
│   ├── matching/
│   └── sorting/
└── utilities/                     # Modular Python loaders & schema validator
    ├── __init__.py
    ├── validator.py               # Validates whole repository against game_schema.json
    ├── metadata_loader.py         # Dynamic suspect & victim metadata scanner
    ├── asset_loader.py            # UI, crime scene, music, and font scanner
    ├── puzzle_loader.py           # Context-aware puzzle loader & filter
    ├── story_loader.py            # Case story loader
    ├── evidence_loader.py         # Shared evidence catalog loader
    ├── dialogue_loader.py         # Dialogue style loader
    ├── random_selector.py         # Random sampling helper for LLM narrative pipeline
    └── test_loaders.py            # Automated loader test runner
```

---

## 🤖 Metadata-Driven Story Generation Workflow

The repository is designed to support **metadata-driven narrative generation**:

```
[Repository Assets]
       │
       ▼ (Scan folder dynamically)
[RandomSelector.select_random_suspects(3-4)]
       │
       ▼ (Pass Suspect Metadata to LLM)
   { Gender, Age, Appearance, Allowed Occupations, Personality, Voice, Relationships }
       │
       ▼ (LLM generates customized mystery story)
[Custom Case Story matching artwork & metadata with zero hallucinations]
```

### Why metadata comes *first*:
1. **Zero Conflict**: The story automatically adapts to the visual artwork instead of trying to generate images for a pre-written story.
2. **Believable Cast**: Suspect occupations, clothing, voice, and age align with artwork.
3. **Rich Dialogue**: Voice, accent, and physical traits enhance LLM NPC roleplay.

---

## 📖 How to Add Content (Plug & Play Guide)

No notebook or engine code needs to be modified when adding new assets. Simply drop files into their respective directories!

### 1. How to Add a New Suspect
1. Place your suspect image in `assets/suspects/` (e.g. `suspect_021.png`).
2. Create a matching JSON file in `assets/suspects/suspect_021.json`:

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
    "hair": "black_bob",
    "eye_color": "green",
    "facial_hair": "none",
    "clothing_style": "victorian_riding_habit",
    "accessories": ["leather_riding_crop", "silver_spurs"]
  },
  "appearance_description": "An athletic equestrian clad in a dark velvet riding habit.",
  "height": "5 ft 8 in",
  "body_type": "athletic",
  "dominant_hand": "right",
  "walking_style": "confident, brisk steps",
  "voice": "clear, ringing soprano",
  "accent": "English Country Aristocrat",
  "allowed_occupations": ["Equestrian", "Stable Master", "Heiress"],
  "personality_tags": ["bold", "headstrong", "impatient"],
  "story_tags": ["stables", "manor", "equestrian"],
  "possible_relationships": ["Niece", "Rival", "Neighbor"]
}
```

### 2. How to Add a New Victim
1. Create `assets/victims/victim_007.json`:
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

### 3. How to Add a New Puzzle
1. Choose the appropriate category directory in `puzzles/` (e.g. `puzzles/cipher/`).
2. Create a new JSON file (e.g. `cipher_006.json`):

```json
{
  "schema_version": "1.0",
  "id": "cipher_006",
  "category": "cipher",
  "puzzle_type": "Caesar Cipher",
  "difficulty": "medium",
  "title": "The Conspirator's Cipher",
  "question": "Decode shift +4: 'EXPI'",
  "answer": "ATLE",
  "solution": "ATLE",
  "hint": "Shift each letter back by 4.",
  "time_limit": 60,
  "reward_points": 80,
  "recommended_for": ["Telegram", "Coded Note", "Diary"]
}
```

### 4. How to Add UI Assets, Music, or Fonts
- **UI Assets**: Drop transparent `.png` graphics into the corresponding category folder in `assets/ui/` (e.g. `assets/ui/buttons/button_green.png`).
- **Music**: Place `.mp3` files in `assets/music/` following recommendations in `assets/music/README.md`.
- **Fonts**: Place `.ttf` or `.woff2` font files in `assets/fonts/` per `assets/fonts/README.md`.

---

## 🛠️ Python Helper Utilities Usage

The `utilities/` package allows easy scanning and random sampling:

```python
from utilities import MetadataLoader, PuzzleLoader, RandomSelector, RepositoryValidator

# 1. Validate repository integrity
validator = RepositoryValidator()
report = validator.validate_repository()
print("Repository Valid:", report["valid"])

# 2. Select 4 random suspects for LLM narrative prompt
selector = RandomSelector()
selected_suspects = selector.select_random_suspects(count=4)

# 3. Load a puzzle matching evidence context (e.g. "Diary")
puzzle_loader = PuzzleLoader()
diary_puzzles = puzzle_loader.get_puzzles_for_evidence("Diary")
```

To run the automated test suite for all loaders:
```bash
python utilities/test_loaders.py
```

---

## 📜 License
This asset repository is created for the *Velvet Envelope* AI Detective Game. All schemas and utilities are open for extension.
