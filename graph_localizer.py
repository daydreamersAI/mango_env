'''
This is the file which helps the model to localize the state it feels it is in for any task as such.

Firstly we will try to use gpt-4v and check if we are able to localize properly 

'''
import pyautogui
import numpy as np
import time 

def process_screenshot( screenshot):
        # Example: Convert the screenshot to a numpy array
        observation = np.array(screenshot)
        return observation

if __name__ == "__main__":
        print('hi')
        time.sleep(2)
        screenshot = pyautogui.screenshot()
        observation = process_screenshot(screenshot)
        path = 'graph_images/screenshot' + '.jpg' # for one path 
        screenshot.save(path)
        image_path = path