import csv
from collections import defaultdict


def main():
    list_all()

def parse_transaction():
    accounts = defaultdict(float)
    with open("Transactions2014.csv", "r") as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if index == 0:
                continue
            _, from_person, to_person, _, amount = row
            accounts[from_person] -= float(amount)
            accounts[to_person] += float(amount)
    return accounts


def list_all():
    accounts = parse_transaction()
    for account in accounts.values():
        print(account)

if __name__ == '__main__':
    main()

