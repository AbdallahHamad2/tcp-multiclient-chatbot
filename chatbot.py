import requests
import os
import socket
import json

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable not set")
MODEL = 'gemini-2.5-flash'
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

system_prompt = {
    "role": "system",
    "parts": [{'text': "You are a helpful assistant."}]
}

chat_history = {}

def initialize_chat(client_addr = ('default', 5051)):
    chat_history[client_addr] = []
    return 0
initialize_chat()

def send_chat_message(user_message, client_addr = ('default', 5051)):

    chat_history[client_addr].append({
        'role': 'user',
        'parts':[{'text': user_message}]
    })

    payload = {
        "system_instruction": system_prompt,
        "contents": chat_history[client_addr]
    }

    response = requests.post(URL, json=payload)
    if response.status_code == 200:
        model_message = response.json()['candidates'][0]['content']['parts'][0]['text']
        chat_history[client_addr].append({
            'role': 'model',
            'parts': [{'text': model_message}]
        })
        return model_message
    else:
        return response.status_code

if __name__ == "__main__":
        
    print("Chatbot is ready. Type your messages below (type exit or quit to finish).")
    while True:
        print("-"*40)
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat.")
            break
        
        reply = send_chat_message(user_input)
        print(f"\nChatbot: {reply}")
