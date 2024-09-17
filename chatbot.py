from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(".env")
api_key = os.getenv('API_KEY')


conversation = []

def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    conversation.append(message)
    
    response = openai.chat.completions.create(
        messages = conversation,
        model  =  "gpt-4o-mini"
    )

    conversation.append(response.choices[0].message)
    
    return response.choices[0].message.content

def chat():
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")

if  __name__ == "__main__":
    chat()

