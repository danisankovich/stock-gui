from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

ai_key = os.getenv("ai_key")

api = OpenAI(api_key=ai_key, base_url='https://api.aimlapi.com')
system_prompt = "You are a Stock Advisor. Please be descriptive and helpful."

def ask(symbol):
    user_prompt = f"As a stock advisor giving market advice to a client, what can you tell me about the short-term and long-term prospects of the company with the symbol {symbol}?"
    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    response = completion.choices[0].message.content

    # print("User:", user_prompt)
    return response
