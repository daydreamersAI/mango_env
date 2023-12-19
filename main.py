print('this is the repo for environment for mango bot')

from model import Decision_Model
from env import Env
# Lets run it here

if __name__ == "__main__":
    print('lets go')
    # task = input("Enter the prompt: ")
    task = "Draw a circle with diameter 10 starting from 20 units above the current location"
    rl_env = Env(task)

    
    model = Decision_Model()