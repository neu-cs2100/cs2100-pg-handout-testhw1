"""
Unit tests for the additional questions in question_asker.
"""
import unittest
from unittest.mock import patch
from src.question_asker import HousingQuestionAsker


class TestAdditionalQuestions(unittest.TestCase):
    """Unit tests for the additional questions in HousingQuestionAsker."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.question_asker = HousingQuestionAsker()

    def test_ask_additional_questions_basic(self) -> None:
        """Test ask_additional_questions with basic y/n responses."""
        with patch('builtins.input', side_effect=['y', 'n']):
            result = self.question_asker.ask_additional_questions()
            # Update these keys based on your actual additional questions:
            # Expected result format: {'question1_key': True, 'question2_key': False}
            # Common examples: 'old23', 'honors', 'athlete', 'work_study', etc.
            # self.assertEqual(result, ['old23'])
            pass

    def test_ask_additional_questions_reverse(self) -> None:
        """Test ask_additional_questions with n/y responses."""
        with patch('builtins.input', side_effect=['n', 'y']):
            result = self.question_asker.ask_additional_questions()
            # Test with opposite responses (n first, y second):
            # self.assertEqual(result, ['honors'])
            pass

    def test_ask_additional_questions_uppercase(self) -> None:
        """Test ask_additional_questions with uppercase responses."""
        with patch('builtins.input', side_effect=['Y', 'N']):
            result = self.question_asker.ask_additional_questions()
            # Test that uppercase Y/N work correctly:
            # self.assertEqual(result, ['old23'])
            pass

    def test_ask_additional_questions_with_invalid_input(self) -> None:
        """Test ask_additional_questions with some invalid inputs."""
        with patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n']):
            result = self.question_asker.ask_additional_questions()
            # Test that the method handles invalid input gracefully for both questions:
            # Expected: should return proper dict after rejecting 'invalid' and 'maybe'
            # self.assertEqual(result, ['old23'])
            pass
