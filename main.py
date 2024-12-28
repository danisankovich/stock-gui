from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("api_key")

def get_posts(symbol):
    url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error: ', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error: ', e)
        return None

result = get_posts('ALLY')
print(result)