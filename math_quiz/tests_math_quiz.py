import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of '+', '-', or '*'
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_calculate_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (3, 4, '-', '3 - 4', -1),
            (6, 8, '*', '6 * 8', 48),
            (10, 5, '+', '10 + 5', 15),  # Additional test case
            (2, 3, '*', '2 * 3', 6),    # Additional test case
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                problem, answer = calculate_result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
