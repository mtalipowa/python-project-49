from brain_games.cli import welcome_user
import prompt
from random import randint


def parity_check(number):
    if number % 2 == 0:
        return "yes"
    return "no"


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0

    while i < 3:
        rand_number = randint(1, 500)
        print(f"Question: {rand_number}")

        answer = prompt.string('Your answer: ')
        is_even = parity_check(rand_number)

        if is_even != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even}'")
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
        i += 1
    if i == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main
