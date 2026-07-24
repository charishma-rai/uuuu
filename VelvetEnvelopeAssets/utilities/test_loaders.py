import json
import sys
import os

# Ensure utilities package can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities.validator import RepositoryValidator
from utilities.metadata_loader import MetadataLoader
from utilities.puzzle_loader import PuzzleLoader, CATEGORIES
from utilities.story_loader import StoryLoader
from utilities.random_selector import RandomSelector
from utilities.puzzle_runner import DetectivePuzzleSession

def run_repository_tests():
    print("=== 1. Validating Repository Schema & Puzzle Integrity ===")
    validator = RepositoryValidator()
    report = validator.validate_repository()
    print(f"Validation Status: {'PASSED' if report['valid'] else 'FAILED'}")
    print(f"Checked Files: {report['checked_files']}")
    if report['errors']:
        print("Validation Errors:")
        for err in report['errors']:
            print(f" - {err}")
    assert report['valid'], f"Repository validation failed with {len(report['errors'])} errors!"

    print("\n=== 2. Testing Metadata Loader ===")
    meta = MetadataLoader()
    suspects = meta.load_all_suspects()
    victims = meta.load_all_victims()
    manifest = meta.get_manifest()
    print(f"Loaded {len(suspects)} suspects")
    print(f"Loaded {len(victims)} victims")
    assert len(suspects) >= 20, f"Expected at least 20 suspects, got {len(suspects)}"
    assert len(victims) >= 6, f"Expected at least 6 victims, got {len(victims)}"

    print("\n=== 3. Testing New 8-Category Puzzle System ===")
    puzzles_loader = PuzzleLoader()
    all_puzzles = puzzles_loader.load_all_puzzles()
    print(f"Total Puzzle Count: {len(all_puzzles)} (Expected >= 120)")
    assert len(all_puzzles) >= 120, f"Expected at least 120 puzzles, got {len(all_puzzles)}"

    for cat in CATEGORIES:
        cat_puzzles = puzzles_loader.get_puzzles_by_category(cat)
        print(f" Category '{cat}': {len(cat_puzzles)} puzzles")
        assert len(cat_puzzles) >= 15, f"Category '{cat}' requires at least 15 puzzles, found {len(cat_puzzles)}"
        
        # Verify schema keys & 3 hints on every puzzle
        for p in cat_puzzles:
            assert "id" in p, f"Puzzle missing 'id': {p}"
            assert "title" in p, f"Puzzle {p['id']} missing 'title'"
            assert "category" in p, f"Puzzle {p['id']} missing 'category'"
            assert "difficulty" in p, f"Puzzle {p['id']} missing 'difficulty'"
            assert "description" in p, f"Puzzle {p['id']} missing 'description'"
            assert "question" in p, f"Puzzle {p['id']} missing 'question'"
            assert "answer" in p, f"Puzzle {p['id']} missing 'answer'"
            assert "solution" in p, f"Puzzle {p['id']} missing 'solution'"
            assert "hints" in p and isinstance(p["hints"], list) and len(p["hints"]) == 3, f"Puzzle {p['id']} must have exactly 3 hints"

    print("\n=== 4. Testing Puzzle Answer Validation & Hint Progression ===")
    sample_puzzle = all_puzzles[0]
    print(f"Sample Puzzle: {sample_puzzle['id']} [{sample_puzzle['title']}]")
    
    # Test valid answer
    val_correct = puzzles_loader.validate_answer(sample_puzzle, sample_puzzle["answer"])
    assert val_correct, f"Answer validation failed for correct answer '{sample_puzzle['answer']}'"
    
    # Test invalid answer
    val_incorrect = puzzles_loader.validate_answer(sample_puzzle, "WRONG_ANSWER_123")
    assert not val_incorrect, "Answer validation wrongly accepted incorrect answer"
    
    # Test 3 hints
    h1 = puzzles_loader.get_hint(sample_puzzle, 1)
    h2 = puzzles_loader.get_hint(sample_puzzle, 2)
    h3 = puzzles_loader.get_hint(sample_puzzle, 3)
    assert "Hint 1" in h1, "Hint 1 failed"
    assert "Hint 2" in h2, "Hint 2 failed"
    assert "Hint 3" in h3, "Hint 3 failed"

    print("\n=== 5. Testing Interactive Detective Puzzle Runner ===")
    session = DetectivePuzzleSession()
    intro_text = session.start_random_puzzle(category="cipher")
    assert "VELVET ENVELOPE" in intro_text, "Runner presentation header missing"
    hint_resp = session.request_hint()
    assert "Hint 1" in hint_resp, "Runner hint 1 failed"

    print("\nAll Velvet Envelope Puzzle System Tests Passed Successfully! 🎉")

if __name__ == "__main__":
    run_repository_tests()
