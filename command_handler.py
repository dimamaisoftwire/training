import os
from account import AccountManager
from file_parser import CSVParser, JSONParser, XMLParser

class CommandHandler:
    def __init__(self, account_manager : AccountManager):
        self.account_manager = account_manager

    @staticmethod
    def show_command_info():
        print("Please enter: ")
        print("import [filename] - to import transaction data. Supported formats are: .csv, .json, .xml")
        print("list all - to list all transactions")
        print("list bogus - to list bogus transactions")
        print("list [name] - to list all transactions with this name")

    def parse_command(self, user_input: str):
        user_input = user_input.strip()
        if user_input.lower().startswith("list all"):
            self.account_manager.list_all()
        elif user_input.lower().startswith("list bogus"):
            self.account_manager.list_bogus()
        elif user_input.lower().startswith("list"):
            if len(user_input) > 5:
                self.account_manager.list_account(user_input[5:].strip())
        elif user_input.lower().startswith("import "):
            self.import_file(user_input[7:].strip())
        elif user_input.lower() == "exit":
            quit()
        else:
            print("Unknown command")

    def import_file(self, filename: str):
        try:
            parser = self.get_parser(filename)
            transactions = parser.parse_file(filename)
            self.account_manager.process_transactions(transactions)
        except FileNotFoundError:
            print("File not found")

    @staticmethod
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
