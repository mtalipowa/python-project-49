import random
from random import randint

rules = 'What is the result of the expression?'


def calculation(symbol, first_number, second_number):
    match symbol:
        case '*': return first_number * second_number
        case '+': return first_number + second_number
        case '-': return first_number - second_number


def main():
    symbols = ["+", "-", "*"]
    symbol = random.choice(symbols)
    first_number = randint(1, 15)
    second_number = randint(1, 15)
    question = str(first_number) + symbol + str(second_number)
    result = calculation(symbol, first_number, second_number)
    return [question, str(result)]
