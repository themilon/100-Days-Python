
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator():
    print(logo)
    num1 = float(input("What's is the first number? :"))
    operator = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide

    }

    for symbol in operator:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an Operator: ")
        num2 = float(input("What's is the next number? :"))
        calculation_function = operator[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit. ") == "y":
            num1 = answer
        else:
            should_continue = False
            print("Program Exit")


calculator()
