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

    @staticmethod
    def validate_date(date: str):
        reg = re.compile("^[0-9]{2}/[0-9]{2}/[0-9]{4}$")
        return reg.match(date)

class CSVParser(FileParser):
    def parse_file(self, file_path: str):
        transactions = []
        logging.info(f"Reading file {file_path}")
        with open(file_path, "r") as file:
            logging.info(f"Parsing file {file_path}")
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                transactions.append(row)
        return transactions
