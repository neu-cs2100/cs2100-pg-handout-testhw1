"""
Unit tests for the HousingQuestionAsker class.

IMPORTANT: Complete ALL test methods below BEFORE implementing any methods in question_asker.py
"""

import unittest
from unittest.mock import patch
from src.question_asker import HousingQuestionAsker


class TestHousingQuestionAsker(unittest.TestCase):
    """Unit tests for the HousingQuestionAsker class."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.question_asker = HousingQuestionAsker()



    def test_ask_class_year_valid_input(self) -> None:
        """Test ask_class_year with valid input.
        
        This first test is already written for you. 
        
        Use this test as an example to complete the rest of the tests.
        """
        with patch('builtins.input', return_value='3'):
            result = self.question_asker.ask_class_year()
            self.assertEqual(result, 3)

    def test_ask_class_year_freshman(self) -> None:
        """Test ask_class_year returns 1 for freshman."""
        with patch('builtins.input', return_value='1'):
            pass

    def test_ask_class_year_senior(self) -> None:
        """Test ask_class_year returns 4 for senior."""
        with patch('builtins.input', return_value='4'):
            pass

    def test_ask_class_year_invalid_then_valid(self) -> None:
        """Test ask_class_year with invalid input followed by valid input."""
        with patch('builtins.input', side_effect=['-4', '2']):
            pass

    def test_ask_class_year_out_of_range_then_valid(self) -> None:
        """Test ask_class_year with out-of-range inputs (0, 5) then valid input."""
        with patch('builtins.input', side_effect=['0', '5', '2']):
            pass

    def test_ask_graduation_status_yes(self) -> None:
        """Test ask_graduation_status with 'y' input."""
        with patch('builtins.input', return_value='y'):
            pass

    def test_ask_graduation_status_uppercase_yes(self) -> None:
        """Test ask_graduation_status with 'Y' input (uppercase)."""
        with patch('builtins.input', return_value='Y'):
            pass

    def test_ask_graduation_status_no(self) -> None:
        """Test ask_graduation_status with 'n' input."""
        with patch('builtins.input', return_value='n'):
            pass

    def test_ask_graduation_status_uppercase_no(self) -> None:
        """Test ask_graduation_status with 'N' input (uppercase)."""
        with patch('builtins.input', return_value='N'):
            pass

    def test_ask_graduation_status_invalid_then_valid(self) -> None:
        """Test ask_graduation_status with invalid inputs followed by valid input."""
        with patch('builtins.input', side_effect=['maybe', 'yes', 'y']):
            pass

    def test_ask_credits_earned_valid(self) -> None:
        """Test ask_credits_earned with valid input."""
        with patch('builtins.input', return_value='15'):
            pass

    def test_ask_credits_earned_zero(self) -> None:
        """Test ask_credits_earned with zero credits."""
        with patch('builtins.input', return_value='0'):
            pass

    def test_ask_credits_earned_high_number(self) -> None:
        """Test ask_credits_earned with high credit count."""
        with patch('builtins.input', return_value='120'):
            pass

    def test_ask_credits_earned_invalid_then_valid(self) -> None:
        """Test ask_credits_earned with invalid inputs followed by valid input."""
        with patch('builtins.input', side_effect=['-5', '-10', '20']):
            pass

    def test_ask_additional_questions_basic(self) -> None:
        """Test ask_additional_questions with basic y/n responses."""
        with patch('builtins.input', side_effect=['y', 'n']):
            result = self.question_asker.ask_additional_questions()
            # Update these keys based on your actual additional questions:
            # Expected result format: {'question1_key': True, 'question2_key': False}
            # Common examples: 'old23', 'honors', 'athlete', 'work_study', etc.
            # self.assertEqual(result, {'old23': True, 'honors': False})
            pass

    def test_ask_additional_questions_reverse(self) -> None:
        """Test ask_additional_questions with n/y responses."""
        with patch('builtins.input', side_effect=['n', 'y']):
            result = self.question_asker.ask_additional_questions()
            # Test with opposite responses (n first, y second):
            # self.assertEqual(result, {'old23': False, 'honors': True})
            pass

    def test_ask_additional_questions_uppercase(self) -> None:
        """Test ask_additional_questions with uppercase responses."""
        with patch('builtins.input', side_effect=['Y', 'N']):
            result = self.question_asker.ask_additional_questions()
            # Test that uppercase Y/N work correctly:
            # self.assertEqual(result, {'old23': True, 'honors': False})
            pass

    def test_ask_additional_questions_with_invalid_input(self) -> None:
        """Test ask_additional_questions with some invalid inputs."""
        with patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n']):
            result = self.question_asker.ask_additional_questions()
            # Test that the method handles invalid input gracefully for both questions:
            # Expected: should return proper dict after rejecting 'invalid' and 'maybe'
            # self.assertEqual(result, {'old23': True, 'honors': False})
            pass
