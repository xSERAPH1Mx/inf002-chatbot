import os
from openai import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    user_prompt = input("Ask me anything!\n")

    messages: list[dict] = [{'role': 'user', 'content': user_prompt}]

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages
    )

    print(response.choices[0].message.content)

if __name__ == '__main__':
    main()