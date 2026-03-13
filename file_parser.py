import json
from abc import ABC, abstractmethod
import csv
import logging
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

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

class JSONParser(FileParser):
    def parse_file(self, file_path: str):
        transactions = []
        logging.info(f"Reading file {file_path}")
        with open(file_path, "r") as file:
            logging.info(f"Parsing file {file_path}")
            reader = json.load(file)
            for index, row in enumerate(reader):
                date = row.get("Date")
                if date:
                    date_obj = datetime.fromisoformat(date)
                    date = date_obj.strftime("%d/%m/%Y")
                from_account = row.get("FromAccount")
                to_account = row.get("ToAccount")
                narrative = row.get("Narrative")
                amount = row.get("Amount")
                transactions.append([date, from_account, to_account, narrative, amount])
        return transactions

class XMLParser(FileParser):
    @staticmethod
    def excel_to_date_string(serial):
        return (datetime(1899, 12, 30) + timedelta(days=int(serial))).strftime("%d/%m/%Y")

    def parse_file(self, file_path: str):
        transactions = []
        logging.info(f"Reading file {file_path}")
        reader = ET.parse(file_path)
        logging.info(f"Parsing file {file_path}")
        root = reader.getroot()
        for index, row in enumerate(root):
            date = self.excel_to_date_string(row.get("Date"))
            narrative = row.findtext("Description")
            amount = row.findtext("Value")
            from_account = row.find("Parties").findtext("From")
            to_account = row.find("Parties").findtext("To")
            transactions.append([date, from_account, to_account, narrative, amount])
        return transactions

