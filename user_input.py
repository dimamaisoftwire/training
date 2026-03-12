import os
from account import AccountManager
from file_parser import CSVParser, JSONParser, XMLParser

def parse_input(accounts : AccountManager):
    while True:
        print("Please enter 'import [filename]'. Supported formats are: .csv, .json, .xml")
        user_input = input().strip()
        if not user_input.lower().startswith("import "):
            print("Unknown command")
            continue
        filename = user_input[7:].strip()

        try:
            parser = get_parser(filename)
            transactions = parser.parse_file(filename)
            accounts.process_transactions(transactions)
            break
        except FileNotFoundError:
            print("File not found")
            return

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
    if user_input.lower().startswith("list "):
        account = user_input[5:]
        accounts.list_account(account)
        return
    print("Unknown command")

def get_parser(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".csv":
        return CSVParser()
    elif ext == ".json":
        return JSONParser()
    elif ext == ".xml":
        return XMLParser()
    else:
        raise Exception("Unsupported format")