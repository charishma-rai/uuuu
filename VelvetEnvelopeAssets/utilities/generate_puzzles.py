import json
import os
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PUZZLES_DIR = BASE_DIR / "puzzles"

NEW_CATEGORIES = [
    "cipher",
    "riddles",
    "logic",
    "timeline",
    "hidden_messages",
    "code_breaking",
    "witness_statements",
    "evidence_analysis"
]

def clean_old_puzzles():
    print("Deleting old puzzle categories and files...")
    if PUZZLES_DIR.exists():
        for item in PUZZLES_DIR.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    
    for cat in NEW_CATEGORIES:
        (PUZZLES_DIR / cat).mkdir(parents=True, exist_ok=True)
    print("Clean puzzle directory structure created.")

def create_puzzle_file(puzzle):
    cat = puzzle["category"]
    pid = puzzle["id"]
    filepath = PUZZLES_DIR / cat / f"{pid}.json"
    data = {
        "schema_version": "1.0",
        "id": puzzle["id"],
        "title": puzzle["title"],
        "category": puzzle["category"],
        "difficulty": puzzle["difficulty"],
        "description": puzzle["description"],
        "question": puzzle["question"],
        "answer": puzzle["answer"],
        "hints": puzzle["hints"],
        "solution": puzzle["solution"]
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

print("Helper definitions loaded.")
