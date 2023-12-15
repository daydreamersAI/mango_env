'''
Here we use prompt to create an environment that executes actions and takes in screenshots beofre deciding on the next action
'''

import pyautogui 
from PIL import Image
import numpy as np
import networkx as nx
import json
import matplotlib.pyplot as plt
import time
import platform

USER_QUESTION = "Hello, I can help you with anything. What would you like done?"

class Env():
    def __init__(self, prompt):
        self.prompt = prompt
        self.observation = None
        
        self.time_step = 0
        
    def step(self, action=dict()):
        input('about to take another step, proceed ?')
        self.state = self.get_state()
        self.reward = self.get_reward()
        
        if self.state == "Goal Achieved" and self.reward == 1:
            self.done = True

        if action['class'] == "Type":
            self.keyboard_type(action['content'])


        elif action['class'] == "Drag":
            self.drag(action['start_coords'], action['end_coords'])    
            
        elif action['class'] == "Click":
            self.click(action['coords'])

        elif action['class'] == "Move":
            self.move_mouse(action['coords'])  

        elif action['class'] == "Double Click":
            self.double_click(action['coords']) 

        elif action['class'] == "Scroll":
            self.scroll(action['direction'])
            
            
        self.state = self.get_state()
        self.reward = self.get_reward()
        self.done = self.get_done()
        self.info = self.get_info()
        self.observation = self.get_observation()
        self.time_step += 1
        return self.observation, self.reward, self.done, self.info

    def reset(self):
        import os
        self.time_step = 0
        # Get user input using the prompt function

        print(f'[Self-Operating Computer]\n{USER_QUESTION}')
        print(f"[User]")
        user_input = input('Enter a command: ')

        # Display the user's input
        print('You entered:', user_input)

        input('proceed?')
        
        return self.observation

    def load_graph(self, graph_file):
        # Read the graph from the JSON file
        with open(graph_file, 'r') as file:
            graph_data = json.load(file)

        # Create a networkx graph from the loaded data
        self.graph = nx.node_link_graph(graph_data)

    def render(self):
        image_pil = Image.fromarray(self.observation)
        image_pil.show()
        

    def close(self):
        pass

    def seed(self):
        pass
    
    def double_click(self, coords):
        x,y = coords
        pyautogui.doubleClick(x=x, y=y)

    def move_mouse(self, coords):
        x,y = coords
        pyautogui.moveTo(x=x, y=y)

    def click(self, coords):
        x,y = coords
        pyautogui.click(x=x, y=y)
        
    def drag(self, start_coords, end_coords):
        start_x, start_y = start_coords
        end_x, end_y = end_coords
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y, button='left')  

    def scroll(self, direction):
        if direction == "up":
            pyautogui.scroll(100)
        elif direction == "down":
            pyautogui.scroll(-100)
        # time.sleep(1)          

    def get_observation(self):
        # Capture the current screenshot using pyautogui
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a format compatible with RL (e.g., numpy array)
        observation = self.process_screenshot(screenshot)
        self.observation = observation # added by vivek
        k = self.time_step
        path = 'screenshots/screenshot' + str(k) + '.jpg'
        screenshot.save(path)

        return observation
    
    def process_screenshot(self, screenshot):
        # Example: Convert the screenshot to a numpy array
        observation = np.array(screenshot)
        return observation

    def keyboard_type(self,text):
        # text = text.replace("\\n", "\n")
        # for char in text:
        #     pyautogui.write(char)
        pyautogui.typewrite(text)
        # pyautogui.press("enter")
        return "Type: " + text


    def get_state(self):
        prompt = self.prompt
        observation = self.observation

    def get_reward(self):
        
        pass

    def get_done(self):
        pass

    def get_info(self):
        pass

    def get_action(self):
        pass

    def get_action_space(self):
        pass


if __name__ == "__main__":
    # task = input("Enter the prompt: ")
    task = "Draw a circle with diameter 10 starting from 20 units above the current location"
    E = Env(task)
    
    E.reset()
    time.sleep(2)
    # E.get_observation()
    #E.render()
    
    
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

####################
    '''
    Replace this with your model .....
    action = Model(E.prompt,E.get_observation)

    '''
####################
    
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
    time.sleep(1)
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
    time.sleep(1)
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
    time.sleep(1)
    
    # E.render()

'''
example usage of actions 
# open youtube and play video of elon musk on openai
    action = {'class': 'Double Click', 'coords': coordinates['chrome_icon']}
    obs,rew,done,info = E.step(action)
    time.sleep(3)
    action = {'class': 'Double Click', 'coords': coordinates['chrome_profile_vivek']}
    obs,rew,done,info = E.step(action)
    time.sleep(3)
    action = {'class': 'Double Click', 'coords': coordinates['youtube']}
    obs,rew,done,info = E.step(action)
    time.sleep(3)
    action = {'class': 'Click', 'coords': coordinates['youtube_search_bar']}
    obs,rew,done,info = E.step(action)
    time.sleep(3)
    action = {'class': 'Type', 'content': "elon musk on openai"}
    obs,rew,done,info = E.step(action)
    time.sleep(3)
    action = {'class': 'Click', 'coords': coordinates['youtube_search_button']}
    obs,rew,done,info = E.step(action)
    time.sleep(2)
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
    time.sleep(1)
    action = {'class': 'Scroll', 'direction': "down"}
    obs,rew,done,info = E.step(action)
    time.sleep(1)
    
'''