# Agent Alphonso
# this is the first model that I'll be testing on this environment 


Prompt = '''You are a coordinate finder agent whose job is to predict the coordinates of the icons and buttons present on the screen using the grid as reference and given the resolution of the computer as :
'''

import requests
import json

'''
models tested :
1) LLM - gpt4 vision
'''

print('this will use gpt4 vision')
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


import requests
import base64

class GPT4VisionChatModel:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/chat/completions"

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def generate_completion(self, user_message, image_path):
        base64_image = self.encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_message
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        output = response.json()['choices'][0]['message']['content']
        # output = response.choices[0].message.content
        #output = response.json()
        # return response.json() #, output
        # return response.json(), output
        return output

# # Example usage:
if __name__ == "__main__":
    # Initialize the GPT-4 vision chat model
    gpt4_chat_model = GPT4VisionChatModel(api_key=client.api_key)

    # User's message and image path
    # user_message = "What’s in this image?"
    # user_message = Prompt + '1920x1080' + "Can you describe the image ?"
    user_message = "Can you see the cursor in the image and describe its location ?"
    # image_path = "screenshots/screenshot_1920x1080.jpg"
    image_path = "screenshot_with_cursor.png"
    # Generate completion
    # jsn, completion = gpt4_chat_model.generate_completion(user_message, image_path)
    completion = gpt4_chat_model.generate_completion(user_message, image_path)
    # print(jsn)
    print(completion)    