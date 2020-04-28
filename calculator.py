import sys
import logging
from functools import reduce

logging.basicConfig(level=logging.INFO)


def get_action():
    choice = [x for x in range(1, 5)]
    action_choice = int(
        input("Which operation should I perform? 1 --> Addition 2 --> Subtraction 3 --> Multiplication  4 "
              "--> Division: "))
    good_choice = action_choice in choice

    if good_choice:
        return int(action_choice)
    else:
        return None


def sum_two(first_digit, second_digit):
    return first_digit + second_digit


def sub(first_digit, second_digit):
    return first_digit + second_digit


def mul_two(first_digit, second_digit):
    return first_digit * second_digit


def div(first_digit, second_digit):
    try:
        result = first_digit / second_digit
    except ZeroDivisionError:
        print("Division by zero!")
        return None
    else:
        return result


def get_info_and_result(action, x, y):
    if action == 1:
        decision = input("Do you want add more digits? [y/n]: ").strip().lower()

        if decision == 'n':
            logging.info(f"Adding: {x} and {y}")
            print(f"Result: {sum_two(x, y)}")
        else:
            more_digits = input("input digits to add: ")
            list_of_digits_str = more_digits.split()
            list_of_digits = [float(d) for d in list_of_digits_str]
            list_of_digits.extend([x, y])
            logging.info(f"Adding: {list_of_digits}")
            print(f"Result: {sum(list_of_digits)}")

    elif action == 2:
        logging.info(f"Subtracting {x} and {y}")
        print(f"Result: {sub(x, y)}")
    elif action == 3:
        decision = input("Do you want multiply more digits [y/n]: ").strip().lower()
        if decision == 'n:':
            logging.info(f"Multiplying {x} and {y}")
            print(f"Result: {mul_two(x, y)}")
        else:
            more_digits = input("input more digits to multiply: ")
            more_digits_str = more_digits.split()
            list_of_digits = [float(d) for d in more_digits_str]
            list_of_digits.extend([x, y])
            result = reduce((lambda i, j: i * j), list_of_digits)
            logging.info(f"Multiplying {list_of_digits}")
            print(f"Result: {result}")

    else:
        logging.info(f"Divide {x} and {y}")
        print(f"Result: {div(x, y)}")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        first_digit = float(input('Input first digit: '))
        second_digit = float(input('Input second digit: '))

    elif 3 > len(sys.argv) >= 2:
        first_digit = float(sys.argv[1])
        second_digit = float(input('Input second digit: '))
    else:
        first_digit = float(sys.argv[1])
        second_digit = float(sys.argv[2])

    action = get_action()

    if action is not None:
        action = int(action)
        get_info_and_result(action, first_digit, second_digit)
    else:
        print("Unable to do operation")
