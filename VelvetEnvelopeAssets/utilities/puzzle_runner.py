import random
from typing import Dict, Any, Optional
from .puzzle_loader import PuzzleLoader, CATEGORIES

class DetectivePuzzleSession:
    """Interactive Python / Google Colab session for solving Velvet Envelope detective puzzles."""

    def __init__(self, root_dir: str = None):
        self.loader = PuzzleLoader(root_dir)
        self.current_puzzle: Optional[Dict[str, Any]] = None
        self.hints_used = 0

    def start_random_puzzle(self, category: Optional[str] = None, difficulty: Optional[str] = None) -> str:
        """Starts a puzzle session and returns formatted evidence discovery text."""
        puzzles = self.loader.load_all_puzzles()
        if category:
            puzzles = [p for p in puzzles if p.get("category", "").lower() == category.lower()]
        if difficulty:
            puzzles = [p for p in puzzles if p.get("difficulty", "").lower() == difficulty.lower()]

        if not puzzles:
            return "No matching puzzle found in repository."

        self.current_puzzle = random.choice(puzzles)
        self.hints_used = 0
        return self.loader.format_puzzle_presentation(self.current_puzzle)

    def request_hint(self) -> str:
        """Progressively reveals Hint 1, Hint 2, or Hint 3."""
        if not self.current_puzzle:
            return "No active puzzle. Call start_random_puzzle() first."

        if self.hints_used >= 3:
            return "⚠️ All 3 hints have already been revealed!"

        self.hints_used += 1
        return self.loader.get_hint(self.current_puzzle, self.hints_used)

    def submit_answer(self, player_answer: str) -> str:
        """Validates player answer and reveals evidence and full solution breakdown."""
        if not self.current_puzzle:
            return "No active puzzle. Call start_random_puzzle() first."

        is_correct = self.loader.validate_answer(self.current_puzzle, player_answer)
        if is_correct:
            res = (
                f"\n✨ EVIDENTIAL BREAKTHROUGH — CORRECT ANSWER! ✨\n"
                f"Your Answer: '{player_answer}'\n"
                f"---------------------------------------------------------------\n"
                f"🔍 DETECTIVE SOLUTION & EVIDENCE REVEALED:\n"
                f"{self.current_puzzle.get('solution', '')}\n"
                f"===============================================================\n"
            )
            return res
        else:
            return (
                f"❌ INCORRECT DEDUCTION.\n"
                f"Your input '{player_answer}' does not match the recovered evidence.\n"
                f"Type request_hint() for guidance or try another answer!"
            )
