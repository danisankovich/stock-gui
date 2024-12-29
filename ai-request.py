from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

ai_key = os.getenv("ai_key")

api = OpenAI(api_key=ai_key, base_url='https://api.aimlapi.com')
system_prompt = "You are a Stock Advisor. Please be descriptive and helpful."

def main():
    user_prompt = input('What would you like to ask? ')
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

    print("User:", user_prompt)
    print("AI:", response)

if __name__ == "__main__":
    main()