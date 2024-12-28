from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("api_key")

def get_quote(symbol):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            quote = response.json()
            data = {
                "previous_close": quote["pc"],
                "current_price": quote["c"],
                "high": quote["h"],
                "low": quote["l"],
                "open": quote["o"],
                "timestamp": quote["t"],
                "percent_change": quote["dp"],
                "change": quote["d"],
            }
            return data
        else:
            print('Error: ', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error: ', e)
        return None

result = get_quote('ALLY')
print(result)