import json
import sys
import os

# Ensure utilities package can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities.validator import RepositoryValidator
from utilities.metadata_loader import MetadataLoader
from utilities.asset_loader import AssetLoader
from utilities.puzzle_loader import PuzzleLoader
from utilities.story_loader import StoryLoader
from utilities.evidence_loader import EvidenceLoader
from utilities.dialogue_loader import DialogueLoader
from utilities.random_selector import RandomSelector

def run_repository_tests():
    print("=== 1. Validating Repository Schema ===")
    validator = RepositoryValidator()
    report = validator.validate_repository()
    print(f"Validation Status: {'PASSED' if report['valid'] else 'FAILED'}")
    print(f"Checked Files: {report['checked_files']}")
    if report['errors']:
        print("Validation Errors:")
        for err in report['errors']:
            print(f" - {err}")
    assert report['valid'], "Repository validation failed!"

    print("\n=== 2. Testing Metadata Loader ===")
    meta = MetadataLoader()
    suspects = meta.load_all_suspects()
    victims = meta.load_all_victims()
    manifest = meta.get_manifest()
    print(f"Loaded {len(suspects)} suspects (Expected 20)")
    print(f"Loaded {len(victims)} victims (Expected 6)")
    print(f"Manifest Version: {manifest.get('version')}")
    assert len(suspects) == 20, f"Expected 20 suspects, got {len(suspects)}"
    assert len(victims) == 6, f"Expected 6 victims, got {len(victims)}"

    print("\n=== 3. Testing Puzzle Loader ===")
    puzzles_loader = PuzzleLoader()
    all_puzzles = puzzles_loader.load_all_puzzles()
    print(f"Loaded {len(all_puzzles)} puzzle templates")
    assert len(all_puzzles) >= 40, f"Expected at least 40 puzzles, got {len(all_puzzles)}"

    print("\n=== 4. Testing Story Loader ===")
    story_loader = StoryLoader()
    stories = story_loader.load_all_stories()
    print(f"Loaded {len(stories)} sample case stories")
    assert len(stories) == 6, f"Expected 6 stories, got {len(stories)}"

    print("\n=== 5. Testing Evidence and Dialogue Loaders ===")
    ev_loader = EvidenceLoader()
    evidence = ev_loader.load_all_evidence_categories()
    print(f"Loaded evidence categories: {list(evidence.keys())}")

    diag_loader = DialogueLoader()
    dialogues = diag_loader.load_all_dialogue_styles()
    print(f"Loaded dialogue styles: {list(dialogues.keys())}")

    print("\n=== 6. Testing Random Selector ===")
    selector = RandomSelector()
    sampled_suspects = selector.select_random_suspects(count=4)
    print(f"Randomly sampled {len(sampled_suspects)} suspects for LLM generation:")
    for s in sampled_suspects:
        print(f" - [{s['id']}] {s['gender']}, Age {s['approximate_age']}, Occupations: {s['allowed_occupations']}")

    print("\nAll Repository Loader Tests Passed Successfully!")

if __name__ == "__main__":
    run_repository_tests()
