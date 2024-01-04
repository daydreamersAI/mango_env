print('this is the repo for environment for mango bot')

from model import Decision_Model
from model import Chat_Model
from env import Env
import os 
from openai import OpenAI
DEBUG = False

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")
# Lets run it here
# now the prompts for gpt4 are coming 
system_prompt = '''
You are a web interaction agent. You are going to help the actor by coming up with a high level strategy for performing the task in hand.
You will be given screenshot image as the current observation and a high level task. Your job is to come up with actions which are in this form :
action = {'class': 'Double Click', 'coords': coordinates['chrome_icon']}
The actions available are Type, Drag, Click, Double Click, Move and Scroll. 
The environment takes one action at each step and returns the new observation and reward and done state.
You can also use the coordinates dictionary to get the coordinates of the icons etc. 
Below is an example action plan executed :
task = 'open youtube and play video of elon musk on openai'
    action = {'class': 'Double Click', 'coords': coordinates['chrome_icon']}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Double Click', 'coords': coordinates['chrome_profile_vivek']}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Double Click', 'coords': coordinates['youtube']}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Click', 'coords': coordinates['youtube_search_bar']}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Type', 'content': "elon musk on openai"}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Click', 'coords': coordinates['youtube_search_button']}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
The coordinates to use are :
coordinates = { 'start_loc' : (500,500),
                "pensil" : (320,125),
                "fill" : (375,115),
                "brush" : (500,130),
                "eraser" : (325,175),
                "line" : (580,110),
                "rectangle" : (665,117),
                "circle" : (50,50),
                "triangle" : (60,60),
                "centre" : (500,500),
                "A" : (400,400),
                "B" : (600,400),
                "text" : (425,120),
                "youtube" : (1091,586),
                "chrome_icon" : (1096,385),
                "chrome_search_bar" : (508,75),
                "youtube_search_bar" : (730,131),
                "youtube_search_button" : (1229,129), 
                "chrome_profile_vivek" : (1300,472),
    }     
'''
actor_prompt ='''Now please return only the action dictionary for current state. The non perfect action sequence is provided and you don't have to strictly follow it.
You may change the course if you feel so according to the state in the screenshot of the image, its just for high level direction of working. The action sequence is : 
'''  
actor_prompt_task = '''\nYou need to return only the action dictionary of type given below:
$ {'class': 'Double Click', 'coords': coordinates['youtube']} $
The task is : 
'''
policy_prompt = ''' Now please give a high level action policy and nothing else to reach the target for the task:
'''
coordinates = { 'start_loc' : (500,500),
                "pensil" : (320,125),
                "fill" : (375,115),
                "brush" : (500,130),
                "eraser" : (325,175),
                "line" : (580,110),
                "rectangle" : (665,117),
                "circle" : (50,50),
                "triangle" : (60,60),
                "centre" : (500,500),
                "A" : (400,400),
                "B" : (600,400),
                "text" : (425,120),
                "youtube" : (1091,586),
                "chrome_icon" : (1096,385),
                "chrome_search_bar" : (508,75),
                "youtube_search_bar" : (730,131),
                "youtube_search_button" : (1229,129), 
                "chrome_profile_vivek" : (1300,472),
    }
prompt1a = "send a mail to john about the meeting with the team at 3pm"
prompt1b = "watch the latest youtube video from the channel 1littlecoder"
prompt1c = "create a todo list inside notes app adding the following tasks : 1)buy milk 2)buy eggs 3)buy bread"
prompt1d = "type this specific text in the third searchbar on the google chrome app : 'how to make a mango shake'"
prompt1e = "Draw a thick circle of diameter 3 in the middle of the screen in the paint app"

prompt2 = "Can you do it using basic actions like click, drag, scroll, type etc."
prompt3 = "also dont assume you are in the mail app from the start, you always start from the home screen of the computer.\n"
# below is the prompt of the current state prompt 4 creator
# model_state_predictor(observation) = state this model may be a multimodal llm or a graph cosine similarity node matcher
prompt_4 = "This is the current state : home screen of the computer\n"

action_sequence_prompt = "create a sequence of actions to reach the goal state from the start state from the prompt given below. Please describe it step by step and dont include the steps which need not be performed while performing the specific action.\nThis is the example output: \nSend a message to Tom on instagram inviting him for birthday party.\nThe steps are :\n1)open the instagram app\n2)click on the chats section\n3)type Tom in the scroll bar\n4)type the birthday message in the text box.\n5)click on the send button.\nNow the new prompt is :\n" \
    + prompt1a + '\n' + prompt2 + "\n" + prompt3 + prompt_4 + "Now only provide the action sequence an nothing else for the task :"

import time
import json

def parse_action(action_str = '{"class": "Double Click", "coords": coordinates["chrome_icon"]}'):
    
    # # Extract the dictionary from the string
    # start_index = action_str.find("{")
    # end_index = action_str.rfind("}")
    # action_dict_str = action_str[start_index:end_index + 1]

    # Using ast.literal_eval to safely evaluate the string as a Python literal
    action_dict = json.loads(action_str)
    return action_dict
    # print(action_dict)



if __name__ == "__main__":
    k = parse_action()
    print(k)
    input('proceed?')
    print('lets go')
    # task = input("Enter the prompt: ")
    # task = "Draw a circle with diameter 10 starting from 20 units above the current location"
    task = "click on search box"
    task = "play a cartoon video on youtube"
    env = Env(task)

    model = Decision_Model(task)
    # so this should take in image and task from the environment 
    msg = system_prompt + task
    # action = model.generate_action(env.img_path,msg = msg)

    # obs,rew,done,info = env.step(action)
    # time.sleep(2)

    # now testing the looping function :
    # firstly get the decision policy with high level actions 
    chat_model = Chat_Model(task)
    # action_sequence = chat_model.generate_completion(user_message = action_sequence_prompt + task,system_message = "You are a helpful assistant designed to output high level tasks " )
    action_sequence = chat_model.generate_completion(user_message = policy_prompt + task,system_message = "You are a helpful assistant designed to output high level tasks " + system_prompt )
    actions_list = action_sequence.strip().split('\n')

    # Find the length of the list of actions
    actions_length = len(actions_list)

    #action_sequence = chat_model.generate_completion()
    print('This is the action sequence : ')
    print(action_sequence)
    input('proceed to taking the actions? ')

    

    for i in range(actions_length):
        final_prompt = msg + actor_prompt + action_sequence + actor_prompt_task + task
        action = model.generate_action(env.img_path,msg = final_prompt)
        print('below is the action produced : ')
        print(action)
        print('action type is :', {type(action)})
        input('this was the type of action, proceed?')
        action = action[:9]
        action = parse_action(action)
        
        obs,rew,done,info = env.step(action)
        time.sleep(2)
        print(obs,rew,done,info)
        input('action taken, proceed?')


