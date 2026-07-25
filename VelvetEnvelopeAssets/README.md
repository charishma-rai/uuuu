# Velvet Envelope Assets & Content Pack (`VelvetEnvelopeAssets`)

`VelvetEnvelopeAssets` is the lightweight, data-driven content library and detective puzzle system for **Velvet Envelope**, an AI murder mystery game.

All puzzles are data-driven JSON files designed to run in plain Python and Google Colab without external dependencies, images, timers, or web requests.

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
├── puzzles/                   # Brand-New Modular Detective Puzzle System (8 Categories)
│   ├── cipher/                # 15 Cipher Puzzles (Caesar, ROT13, Morse, Vigenère, Atbash, etc.)
│   ├── riddles/               # 15 Detective Riddles (Locked rooms, physical anomalies, crime scene logic)
│   ├── logic/                 # 15 Logic Deduction Puzzles (Truth/Liar, room grids, alibi matrices)
│   ├── timeline/              # 15 Timeline Reconstruction Puzzles (Event ordering, schedules, decay)
│   ├── hidden_messages/       # 15 Hidden Messages Puzzles (Acrostics, Nth-letter shifts, word grids)
│   ├── code_breaking/         # 15 Code Breaking Puzzles (Safe combos, PINs, number sequences, dials)
│   ├── witness_statements/    # 15 Witness Statements Puzzles (Spotting testimony contradictions)
│   └── evidence_analysis/     # 15 Evidence Analysis Puzzles (Blood type, footprints, forensics)
└── utilities/                 # Python loader scripts & interactive puzzle engine
    ├── __init__.py
    ├── asset_loader.py
    ├── metadata_loader.py
    ├── puzzle_loader.py       # Core puzzle loader with discovery formatting & answer validation
    ├── puzzle_runner.py       # Interactive DetectivePuzzleSession runner for Google Colab / Python
    ├── random_selector.py     # Random sampler for suspects, victims, stories, and puzzles
    ├── story_loader.py
    └── validator.py           # Repository schema & 120-puzzle integrity validator
```

---

## 🧩 The Velvet Envelope Puzzle System

Every puzzle is stored as an individual JSON file matching the strict schema:

```json
{
  "id": "cipher_001",
  "title": "The Cipher of Lord Blackwood",
  "category": "cipher",
  "difficulty": "easy",
  "description": "A coded page was recovered from Lord Blackwood's study desk.\nThe message appears encrypted using a Caesar shift of +3.",
  "question": "Decrypt the message:\n\nPHHW PH DW PLGQLJKW",
  "acceptable_answer_format": "Type the decoded sentence exactly.\n\nExample:\nTHE KEY IS SAFE",
  "accepted_answers": [
    "MEET ME AT MIDNIGHT",
    "meet me at midnight",
    "Meet Me At Midnight"
  ],
  "hints": [
    "The letters appear consistently shifted by the same alphabet offset.",
    "Try moving each letter backward by 3 positions in the alphabet.",
    "P minus 3 positions is M, H minus 3 is E, W minus 3 is T."
  ],
  "solution_explanation": "Shift each letter backward by 3 positions in the alphabet (P->M, H->E, H->E, W->T). Decoded phrase: MEET ME AT MIDNIGHT.",
  "time_limit": 180,
  "reward_points": 100
}
```

### 💡 3-Tiered Hint System
Every puzzle contains exactly three progressive hints:
1. **Hint 1**: Very subtle clue.
2. **Hint 2**: Points the player in the correct solving direction.
3. **Hint 3**: Almost reveals the solving strategy without directly giving the answer.

### 🗝️ Investigation Discovery Headers
Puzzles are presented as discovered evidence:
- 🗝️ Recovered Notebook Page
- 📜 Anonymous Letter
- 🧩 Locked Filing Cabinet
- 🔐 Encrypted USB Drive
- 📝 Witness Deposition
- 📂 Evidence Folder #7
- 📻 Decoded Radio Transmission
- 📄 Forensic Report

---

## 🛠️ Python / Google Colab Interactive Usage

Load and play puzzles interactively in Google Colab or Python using `utilities`:

```python
from utilities import PuzzleLoader, DetectivePuzzleSession, RandomSelector

# 1. Start an interactive detective puzzle session
session = DetectivePuzzleSession()

# 2. Start a random puzzle from any category (e.g. 'cipher', 'logic', 'riddles', etc.)
evidence_text = session.start_random_puzzle(category="cipher")
print(evidence_text)

# 3. Request progressive hints when stuck
print(session.request_hint()) # Reveals Hint 1
print(session.request_hint()) # Reveals Hint 2
print(session.request_hint()) # Reveals Hint 3

# 4. Submit deduction answer
result = session.submit_answer("MEET ME AT MIDNIGHT")
print(result)
```

---

## 📖 Extension Guide

Adding future puzzles requires **zero code modifications**:
Simply create a new JSON file in the appropriate category folder under `puzzles/<category>/<category>_016.json` following the JSON schema!
