from account import AccountManager
from user_input import parse_input


def main():
    accounts = AccountManager()
    parse_input(accounts)

if __name__ == '__main__':
    main()

