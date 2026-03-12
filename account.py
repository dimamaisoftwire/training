from dataclasses import dataclass
from typing import List
import logging
import re

@dataclass
class Transaction:
    date: str
    from_name: str
    to_name: str
    narrative: str
    amount: float

class Account:
    def __init__(self, name: str):
        self.balance = 0
        self.transactions = []
        self.name = name

    def add_transaction(self, transaction: Transaction):
        if self.name == transaction.from_name:
            self.balance -= transaction.amount
        elif self.name == transaction.to_name:
            self.balance += transaction.amount
        else:
            raise ValueError("Invalid transaction name")

        self.transactions.append(transaction)

    def get_info(self):
        output = self.name
        if self.balance > 0:
            output += f": owed £{self.balance:.2f}"
        else:
            output += f": owe £{self.balance:.2f}"
        return output

    def get_transactions(self):
        return self.transactions

class AccountManager:
    def __init__(self):
        self.accounts = {}
        self.transactions = []
        self.bogus_transactions = []

    def add_account(self, name: str):
        self.accounts[name] = Account(name)

    def add_transaction(self, transaction: Transaction):
        if transaction.from_name not in self.accounts:
            self.add_account(transaction.from_name)
        if transaction.to_name not in self.accounts:
            self.add_account(transaction.to_name)

        account_from, account_to = self.accounts[transaction.from_name], self.accounts[transaction.to_name]
        account_from.add_transaction(transaction)
        account_to.add_transaction(transaction)

        self.transactions.append(transaction)

    def process_transaction(self, transaction: List[str], index: int):
        if len(transaction) != 5:
            raise ValueError(f"Invalid transaction format in row {index}")
        date, from_person, to_person, narrative, amount = transaction

        if not AccountManager.validate_date(date):
            logging.error(f"Invalid date format in row {index}")
            raise ValueError(f"Invalid date format in row {index}")

        amount = float(amount)
        if amount < 0:
            logging.error(f"Invalid amount {amount} in row {index}")
            raise ValueError(f"Invalid amount {amount}")
        self.add_transaction(Transaction(date, from_person, to_person, narrative, amount))


    @staticmethod
    def validate_date(date: str):
        reg = re.compile("^[0-9]{2}/[0-9]{2}/[0-9]{4}$")
        return reg.match(date)

    def process_transactions(self, transactions: List[List[str]]):
        for index, row in enumerate(transactions):
            try:
                self.process_transaction(row, index)
            except ValueError:
                self.bogus_transactions.append(row)
                logging.error(f"{ValueError} in row {index}")
                continue

            date, from_person, to_person, narrative, amount = row
            amount = float(amount)

            self.add_transaction(Transaction(date, from_person, to_person, narrative, amount))

    def list_all(self):
        for account in self.accounts.values():
            print(account.get_info())

    def list_account(self, name: str):
        if name not in self.accounts:
            print("Invalid account name")
            return

        transactions = self.accounts[name].get_transactions()
        print(f"Name: {name} transactions: {len(transactions)}")
        for transaction in transactions:
            print(f"date: {transaction.date} from: {transaction.from_name} to: {transaction.to_name} narrative: {transaction.narrative}  amount: £{transaction.amount:.2f} ")

    def list_bogus(self):
        print(f"List of bogus transactions. Total count: {len(self.bogus_transactions)}")
        for transaction in self.bogus_transactions:
            print(transaction)

