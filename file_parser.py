from abc import ABC, abstractmethod
import csv
import logging
import re

from account import Transaction

logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

class FileParser(ABC):
    @abstractmethod
    def parse_file(self, file_path: str):
        pass

class CSVParser(FileParser):
    def parse_file(self, file_path: str):
        transactions = []
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                date, from_person, to_person, narrative, amount = row
                amount = float(amount)

                transactions.append(Transaction(date, from_person, to_person, narrative, amount))
        return transactions
