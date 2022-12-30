import unittest
from my_project.basic.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # The prefix be required beginning with `test_` for unittest spec.
        # Setup
        calculator = Calculator()
        expected_result = 10

        # Action
        actual_result = calculator.add(1, 2, 3, 4)

        # Assert
        self.assertEqual(expected_result, actual_result)
