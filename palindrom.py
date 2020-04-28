def is_palindrom(given_string):
    """
    Checks if given string is palindrom
    :param given_string:
    :return: value of bool, if param is palindrom --> True, if not --> False
    """
    reverse_stirng = given_string[::-1]
    outcome = given_string == reverse_stirng
    return outcome


def main():
    help(is_palindrom)
    given_string = input("Check if palindrom: ").lower().strip()
    print(is_palindrom(given_string))




if __name__ == '__main__':
    main()
