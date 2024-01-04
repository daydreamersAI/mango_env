import requests
import json

'''
models tested :
1) LLM - gpt4 vision
'''

#print('this will use gpt4 vision')
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

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
output = print(response.choices[0].message.content)

print(output)