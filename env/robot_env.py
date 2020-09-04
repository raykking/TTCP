import os
import copy
import pandas
import numpy as np

import gym
from gym import error, spaces
from gym.utils import seeding

from gym.envs.safethunder_index.engine import RK34Engine

# try:
#     import mujoco_py
# except ImportError as e:
#     raise error.DependencyNotInstalled("{}. (HINT: you need to install mujoco_py, and also perform the setup instructions here: https://github.com/openai/mujoco-py/.)".format(e))

DEFAULT_SIZE = 500

class RobotEnv(gym.GoalEnv):
 


(private code)