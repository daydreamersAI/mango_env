# mango_env
The different environments for the mango bot :

Mango bot(agent based on this environment) will be released soon 
Join discord to help with the agent or directly contribute by sending a pull request
Discord link - https://discord.gg/Cfa7ACqr
# mango bot
A computer bot that can paint and do other stuff on your computer

<img src="original.jpg" alt="Alt text" title="Optional title">


The main idea of this project is to use the power of gpt-4/image models as an observation to control the computer and be able to assist us in firstly simple tasks like opening certain apps and adding notes etc.

Features :
two types of envs are together :
1) Simple rl env based on the pyautogui module - ( in env.py for now )
2) Selenium based rl env that could take web actions - coming soon 
3) Playwright based rl env with action traces - coming soon

Below is some set of example actions being executed using this env which have been fed manually
Try out your set of actions and have fun... :]

# Usage: 

In the terminal

1) git clone https://github.com/daydreamersAI/mango_env.git
2) cd mango_env
3) pip install -r requirements.txt
4) insert your model code inside the model.py
5) export OPENAI_API_KEY='paste your openai vision api key'
6) python main.py


# Todo:
1) Add selenium env
2) make a module once the agent is working
3) release the agent named mango bot on this env
4) add hower option in the environment
5) train a base model on mind2web
6) add decision transformer for oracle grounding of the selected actions 

The examples of the environment workings are below :

1) Pure RL environment with different tool use in paint:

![2023-12-01 03-45-18](https://github.com/daydreamersAI/mango/assets/61907310/55fd7a07-8ad0-4a4b-95ef-71dee3e37918)

2) prompt - Search about Elon musk views on openai on youtube

![2023-12-02-11-28-21_RvFVJSjg](https://github.com/daydreamersAI/mango/assets/61907310/48c1e3ce-c7a7-4171-aff7-68a6dd1a1d88)

