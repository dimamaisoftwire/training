from account import AccountManager
from file_parser import CSVParser

def main():
    accounts = AccountManager()
    csv_parser = CSVParser()
    transactions = csv_parser.parse_file("Transactions2014.csv")
    accounts.process_transactions(transactions)
    parse_input(accounts)

def parse_input(accounts):
    print("Please enter: ")
    print("list all - to list all transactions")
    print("list bogus - to list bogus transactions")
    print("list [name] - to list all transactions with this name")

    user_input = input()
    if user_input.lower() == "list all":
        accounts.list_all()
        return
    if user_input.lower() == "list bogus":
        accounts.list_bogus()
        return
    if user_input.lower()[:5] == "list ":
        account = user_input[5:]
        accounts.list_account(account)
        return
    print("Unknown command")

if __name__ == '__main__':
    main()

