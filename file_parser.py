from abc import ABC, abstractmethod
import csv
import logging

logging.basicConfig(filename='SupportBank.log', filemode='w', level=logging.DEBUG)

class FileParser(ABC):
    @abstractmethod
    def parse_file(self, file_path: str):
        pass

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
