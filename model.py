# # Agent Alphonso
# # this is the first model that I'll be testing on this environment 

import requests
import json
import base64
import os
from gpt4_experiments import GPT4VisionChatModel
from gpt3_experiments import GPT3_Chat_Model
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
        return completion   

class Chat_Model():

    def __init__(self, task, model= "gpt-3.5-turbo-1106"):
        # self.obs = observation # pil object/numpy array
        self.api_key = client.api_key
        self.task = task
        self.model = model

    def generate_completion(self, user_message = "Who won the world series in 2020?",system_message = "You are a helpful assistant designed to output JSON." ):    
        model = GPT3_Chat_Model(api_key=client.api_key)
        output = model.generate_completion(user_message,system_message)
        return output    

#testing the gpt4 vision api

    
if __name__ == "__main__":
    gpt4_chat_model = GPT4VisionChatModel(api_key=client.api_key)
    # User's message and image path
    user_message = "What’s in this image?"
    image_path = "screenshots/screenshot0.jpg"

    completion = gpt4_chat_model.generate_completion(user_message, image_path)
    print(completion)  
    # print(system_prompt)