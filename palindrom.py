def palindrom(given_string):
    reverse_stirng = given_string[::-1]
    outcome = given_string == reverse_stirng
    print(outcome)


def main():
    given_string = input("Check if palindrom: ").lower().strip()
    palindrom(given_string)



if __name__ == '__main__':
    main()
