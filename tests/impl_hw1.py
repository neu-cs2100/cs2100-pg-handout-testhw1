"""
Integration tests for the Housing Priority Calculator.
Tests the main calculate_score function that coordinates both classes.
"""

import unittest
from unittest.mock import patch
from src.question_asker import HousingQuestionAsker
from src.hw1 import calculate_score
class TestHousingPriorityIntegration(unittest.TestCase):
    """Integration tests for the Housing Priority Calculator.

    Instructions on using unittest.mock.patch:

    - Each patch context manager replaces the target function with a mock value.
    - Supply return_value to specify what the mock should return.
    - Since we're now using classes in separate files, we patch the class methods.

    e.g.:

        with patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4):
            with patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=16):
                # test code here
    """

    def test_calculate_score_senior_graduating(self) -> None:
        """Test calculate_score for a graduating senior."""
        # Based on mocks:
        #   year=4 → X pts, grad=True → Y pts, credits=16 → Z pts,
        #   additional=['honors'] → W pts
        # Total = X+Y+Z+W (Replace with your actual scoring system)
        #
        # This is just an example
        # You'll need to uncomment and update based on your scoring system:

        #with patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4), \
        #     patch.object(HousingQuestionAsker, 'ask_graduation_status', return_value=True), \
        #     patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=16), \
        #     patch.object(HousingQuestionAsker, 'ask_additional_questions',
        #                              return_value=['honors']):
        #     result = calculate_score()
        #     self.assertEqual(result, expected)
        pass

    def test_calculate_score_freshman(self) -> None:
        """Test calculate_score for a freshman (no graduation question should be asked)."""
        # Note: ask_graduation_status should NOT be called for freshman
        # Based on mocks:
        #   year=1 → X pts, grad=N/A → 0 pts, credits=8 → Y pts, additional=[](all False) → Z pts
        # Total = X+0+Y+Z

        # Uncomment and update this based on your actual point system:

        #with patch.object(HousingQuestionAsker, 'ask_class_year', return_value=1), \
        #     patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=8), \
        #     patch.object(HousingQuestionAsker, 'ask_additional_questions',
        #          return_value=[]):
        #    result = calculate_score()
        #    self.assertEqual(result, expected)
        #    pass

    def test_calculate_score_senior_not_graduating(self) -> None:
        """Test calculate_score for a non-graduating senior."""
        # Uncomment and update this based on your actual point system:

        #with patch.object(HousingQuestionAsker, 'ask_class_year', return_value=4), \
        #     patch.object(HousingQuestionAsker, 'ask_graduation_status', return_value=False), \
        #     patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=20), \
        #     patch.object(HousingQuestionAsker, 'ask_additional_questions',
        #          return_value=['old23']):
        #    result = calculate_score()
        #    self.assertEqual(result, expected)
        #    pass

    def test_calculate_score_junior(self) -> None:
        """Test calculate_score for a junior (no graduation question should be asked)."""
        # Uncomment and update this based on your actual point system:

        #with patch.object(HousingQuestionAsker, 'ask_class_year', return_value=3), \
        #     patch.object(HousingQuestionAsker, 'ask_credits_earned', return_value=12), \
        #     patch.object(HousingQuestionAsker, 'ask_additional_questions',
        #          return_value=['old23', 'honors']):
        #    result = calculate_score()
        #    self.assertEqual(result, expected)
        #    pass
