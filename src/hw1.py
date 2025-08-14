"""
HW 1: Housing Priority Calculator - Main Module

This is the main module that orchestrates the housing priority calculation
by using both the HousingQuestionAsker and HousingPriorityCalculator classes.
"""
from src.question_asker import HousingQuestionAsker
from src.priority_calculator import HousingPriorityCalculator

def calculate_score() -> int:
    """Orchestrate all steps using both classes:
      1) Create instances of HousingQuestionAsker and HousingPriorityCalculator
      2) Use HousingQuestionAsker to gather all information
      3) Use HousingPriorityCalculator to compute the final score
      4) Handle the logic for only asking graduation status if student is a senior
      Return total score.
      5) Implement the main calculation flow using both classes
    """
    pass

def main() -> None:
    """Entry point: print header, compute score, print footer. (For easier readability)"""
    pass

if __name__ == "__main__":
    main()
