print('this is the repo for environment for mango bot')

from model import Decision_Model
from env import Env
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
Now please return only the action dictionary for current state, with task:    

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

if __name__ == "__main__":
    print('lets go')
    # task = input("Enter the prompt: ")
    # task = "Draw a circle with diameter 10 starting from 20 units above the current location"
    task = "click on search box"
    env = Env(task)

    model = Decision_Model(task)
    # so this should take in image and task from the environment 
    msg = system_prompt + task
    action = model.generate_action(env.img_path,msg = msg)

    obs,rew,done,info = env.step(action)




