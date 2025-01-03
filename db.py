import json
# temporarily using json in places of sqlite

def read_watchlist():
    with open('watchlist.json', 'r') as f:
        data = json.load(f)
        return data

def add_symbol(s):
    symbol = s.upper()
    data = read_watchlist()
    if (symbol not in data):
        data.append(symbol)
        with open('watchlist.json', 'w') as f:
            json.dump(data, f)

def remove_symbol(s):
    symbol = s.upper()
    data = read_watchlist()
    if (symbol in data):
        data.remove(symbol)
        with open('watchlist.json', 'w') as f:
            json.dump(data, f)
