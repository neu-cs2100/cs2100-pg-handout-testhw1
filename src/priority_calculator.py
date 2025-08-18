"""
HW 1: Housing Priority Calculator - Priority Calculator Module

This module contains the HousingPriorityCalculator class 
responsible for calculating priority scores.

Implement each method as described in the handout.
"""

class HousingPriorityCalculator:
    """Class responsible for calculating priority scores based on student information."""

    def points_for_class_year(self, year: int) -> int:
        """
        Given an integer `year`, return points based on your scoring system.

        Here, you may assume year is an integer from 1 to 4, since we already 
        validated input in the question asker. 

        IMPORTANT: Write your tests in test_priority_calculator.py FIRST!
        Then implement this method to make those tests pass.

        Example scoring systems:
        - Linear: Freshman=1, Sophomore=2, Junior=3, Senior=4
        - Exponential: Freshman=2, Sophomore=4, Junior=8, Senior=16
        - Custom: Design your own fair system

        Document your chosen system in SUMMARY.md!
        
        Implement logic to calculate points based on class year
        
        DON'T IMPLEMENT UNTIL YOU'VE WRITTEN YOUR TESTS!
        """
        pass

    def points_for_graduation(self, is_graduating: bool) -> int:
        """ 
        Return points based on graduation status.

        IMPORTANT: Write your tests FIRST!

        Typical approach: graduating students get bonus points (e.g., 5),
        non-graduating students get 0. But you can design your own system.
        
        Implement logic for calculating points for a graduating student
        
        DON'T IMPLEMENT UNTIL YOU'VE WRITTEN YOUR TESTS!
        """
        pass

    def points_for_credits(self, num_credits: int) -> int:
        """
        Compute points based on credits earned.

        IMPORTANT: Write your tests FIRST!

        Example systems:
        - 1 point per credit
        - 0.5 points per credit
        - Tiered system: 0-30 credits = 1pt each, 31+ = 2pts each
        - Maximum cap: up to 50 credits count

        Here, you may assume num_credits is a non-negative integer,
        since we already validated input in the question asker.

        Document your system in SUMMARY.md!
        
        Implement points system for credits.
        
        DON'T IMPLEMENT UNTIL YOU'VE WRITTEN YOUR TESTS!
        """
        pass

    def points_for_additional_questions(self, responses: dict[str, bool]) -> int:
        """
        Given the dict from ask_additional_questions(), assign points.

        IMPORTANT: Write your tests FIRST!

        Example:
        - 'old23': True → 2 points, False → 0 points
        - 'honors': True → 3 points, False → 0 points
        - Total for {'old23': True, 'honors': False} = 2 + 0 = 2 points

        Design your own questions and point values!
        
        Implement scoring logic.
        
        DON'T IMPLEMENT UNTIL YOU'VE WRITTEN YOUR TESTS!
        """
        pass

    def calculate_total_score(
        self,
        year: int,
        is_graduating: bool,
        num_credits: int,
        additional_responses: dict[str, bool],
    ) -> int:
        """
        Calculate the total priority score based on all inputs.

        IMPORTANT: Write your tests FIRST!

        This method should use all your other methods:
        total = (
            self.points_for_class_year(year)
            + self.points_for_graduation(is_graduating)
            + self.points_for_credits(num_credits)
            + self.points_for_additional_questions(additional_responses)
        )

        Here, you may assume that the responses dict contains valid keys
        corresponding to the questions you designed in ask_additional_questions().
        
        Args:
            year (int): Class year (1-4)
            is_graduating (bool): Whether student is graduating this semester
            credits (int): Number of credits earned
            additional_responses (dict): Dictionary of additional question responses
        Returns:
            int: Total priority score
            
        Use the other methods you implemented to calculate total score
        DON'T IMPLEMENT UNTIL YOU'VE WRITTEN YOUR TESTS!
        """
        pass
