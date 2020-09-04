import numpy as np
import math

from gym.envs.safethunder_index import rotations, robot_env, utils #####TODO


def goal_distance(goal_a, goal_b):

    assert goal_a.shape == goal_b.shape
    return np.linalg.norm(goal_a - goal_b, axis=-1)


 
class UfoEnv(robot_env.RobotEnv):   
    """Superclass for all UFO environments.
    """
  

(private code)