from dataclasses import dataclass
from typing import List

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

    def add_transactions(self, transactions: List[Transaction]):
        for transaction in transactions:
            self.add_transaction(transaction)

    def list_all(self):
        for account in self.accounts.values():
            print(account.get_info())

    def list_account(self, name: str):
        if name not in self.accounts:
            raise ValueError("Invalid account name")

        transactions = self.accounts[name].get_transactions()
        print(f"Name: {name} transactions: {len(transactions)}")
        for transaction in transactions:
            print(f"date: {transaction.date} from: {transaction.from_name} to: {transaction.to_name} narrative: {transaction.narrative}  amount: £{transaction.amount:.2f} ")
