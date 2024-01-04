import requests
import json

'''
models tested :
1) LLM - gpt4 vision
'''
import base64
import requests
# from dotenv import load_dotenv
import os 
# OpenAI API Key
# load_dotenv()

from openai import OpenAI
DEBUG = False

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

class GPT3_Chat_Model():

    def __init__(self, api_key):
        self.api_key = api_key

    def generate_completion(self, user_message = "Who won the world series in 2020?",system_message = "You are a helpful assistant designed to output JSON." ):    
        response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        # response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        )
        output = response.choices[0].message.content
        return output

if __name__ == "__main__":
    
    model = GPT3_Chat_Model(api_key=client.api_key)
    output = model.generate_completion()
    print(output)