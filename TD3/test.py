import requests

separator = ','

def get_data(uri: str, max_lines: int = None) -> list:

    lines = read_lines(uri)

    headers = get_headers(lines)

    transactions = []
    for line in lines:
        transaction = line_to_transaction(line, headers)

        if (transaction != {}):
            transactions.append(transaction)

        if (not max_lines is None and max_lines <= len(transactions)):
            break

    return transactions

def get_headers(lines: list) -> list:
    return lines[0].strip().split(separator)

def line_to_transaction(line: str, headers: list) -> dict:
    converted_line = line.strip().split(separator)

    transaction = {}

    if (len(converted_line) == len(headers)):
        for i in range(len(headers)):
            key = headers[i]
            value = converted_line[i]

            transaction[key] = value
    
    return transaction

def read_lines(uri: str) -> any:
    res = requests.get(uri)

    return (res.text.split('\n'))

annee = 2017
uri = f'https://files.data.gouv.fr/geo-dvf/latest/csv/{annee}/communes/31/31555.csv'
data = get_data(uri, 10)

print(data)