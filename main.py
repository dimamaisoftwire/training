import csv
from collections import defaultdict
from account import AccountManager
from file_parser import CSVParser

def main():
    accounts = AccountManager()
    transactions = CSVParser.parse_file("Transactions2014.csv")
    accounts.add_transactions(transactions)
    list_all(accounts)
    list_account(accounts, "Gergana I")

def list_all(accounts):
    accounts.list_all()

def list_account(accounts, name):
    accounts.list_account(name)

if __name__ == '__main__':
    main()

