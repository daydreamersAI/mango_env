# Agent Alphonso
# this is the first model that I'll be testing on this environment 

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
    def __init__(self, observation, task, chat_model):
        self.obs = observation # pil object/numpy array
        self.task = task
        self.model = chat_model

    def generate_action():
        # add logic here
        return {'class': 'Scroll', 'direction': "down"}    


#testing the gpt4 vision api
    
if __name__ == "__main__":
    gpt4_chat_model = GPT4VisionChatModel(api_key=client.api_key)
    # User's message and image path
    user_message = "What’s in this image?"
    image_path = "screenshots/screenshot0.jpg"

    completion = gpt4_chat_model.generate_completion(user_message, image_path)
    print(completion)  