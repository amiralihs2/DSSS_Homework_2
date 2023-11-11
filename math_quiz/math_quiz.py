import random

def generate_random_integer(minimum, maximum):
    """
    Generate a random integer between the specified minimum and maximum values.
    """
    return random.randint(minimum, maximum)

def generate_random_operator():
    """
    Generate a random arithmetic operator (+, -, *).
    """
    operators = ['+', '-', '*']
    return random.choice(operators)

def calculate_result(num1, num2, operator):
    """
    Calculate the result of the arithmetic operation based on the given numbers and operator.
    """
    if operator == '+':
        return f"{num1} + {num2}", num1 + num2
    elif operator == '-':
        return f"{num1} - {num2}", num1 - num2
    elif operator == '*':
        return f"{num1} * {num2}", num1 * num2

def math_quiz():
    """
    Conduct a math quiz game with the user.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_result(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = None

        if user_answer is not None:
            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")

    if score == total_questions:
        print("Congratulations! You answered all questions correctly.")
    elif score == 0:
        print("Better luck next time! You didn't answer any questions correctly.")
    else:
        print(f"Good effort! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
