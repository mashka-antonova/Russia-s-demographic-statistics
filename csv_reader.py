import csv

def read_csv(filepath):
    with open(filepath, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data