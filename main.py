from account import AccountManager
from file_parser import CSVParser, JSONParser
from user_input import parse_input


def main():
    accounts = AccountManager()
    parse_input(accounts)

if __name__ == '__main__':
    main()

