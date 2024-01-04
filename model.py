# # Agent Alphonso
# # this is the first model that I'll be testing on this environment 

import requests
import json
import base64
import os
from gpt4_experiments import GPT4VisionChatModel
from openai import OpenAI
DEBUG = False

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")



class Decision_Model():
    def __init__(self, task):
        # self.obs = observation # pil object/numpy array
        self.task = task
        # self.chat_model = chat_model
        self.image_path = "screenshots/screenshot0.jpg"

    def generate_action(self, img_path, msg):
        # add logic here
        self.image_path = img_path
        gpt4v_chat_model = GPT4VisionChatModel(api_key=client.api_key)
        # User's message and image path
        # user_message = "What’s in this image?"
        user_message = msg 
        image_path = self.image_path

        completion = gpt4v_chat_model.generate_completion(user_message, image_path)
        print(completion)
        input('this was the output, proceed ?')
        return {'class': 'Scroll', 'direction': "down"}    


#testing the gpt4 vision api

    
if __name__ == "__main__":
    gpt4_chat_model = GPT4VisionChatModel(api_key=client.api_key)
    # User's message and image path
    user_message = "What’s in this image?"
    image_path = "screenshots/screenshot0.jpg"

    completion = gpt4_chat_model.generate_completion(user_message, image_path)
    print(completion)  
    # print(system_prompt)