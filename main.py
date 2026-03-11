import csv
from collections import defaultdict
from account import AccountManager
from file_parser import CSVParser

def main():
    accounts = AccountManager()
    transactions = CSVParser.parse_file("Transactions2014.csv")
    accounts.add_transactions(transactions)
    parse_input(accounts)

def parse_input(accounts):
    user_input = input("Please enter List All to output all accounts or List [Account Name] to output transactions for that account: ")
    if user_input.lower() == "list all":
        accounts.list_all()
        return
    if user_input.lower()[:5] == "list ":
        account = user_input[5:]
        accounts.list_account(account)
        return
    print("Unknown command")

def list_all(accounts):
    accounts.list_all()

def list_account(accounts, name):
    accounts.list_account(name)

if __name__ == '__main__':
    main()

