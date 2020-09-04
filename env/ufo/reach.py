import os
from gym import utils
from gym.envs.safethunder_index import ufo_env   ### TODO
import numpy as np


# Ensure we get the path separator correct on windows
# MODEL_XML_PATH = os.path.join('fetch', 'reach.xml')
# features=[x,y,z,v,theta_a,psi_2,phi_a,gamma,n_xi,eta,zeta]

class SafeUfoReachEnv2(ufo_env.UfoEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_xpos = {
            'ufo_x': 3.35092767e+03,
            'ufo_y': 3.19440395e+03,
            'ufo_z': -4.87754035e-01,
            'ufo_v': 6.27730353e+02,
            'ufo_theta_a': 7.29144198e-01,
            'ufo_psi_2': -2.46488171e-04,
            'ufo_phi_a': 7.31044100e-01,
            'ufo_phi_2': 1.09273751e-03,
            'ufo_gamma': 1.00322659e+02,
            'ufo_n_xi': 1.35870296e+01,
            'ufo_eta': -4.28115913e-02,
            'ufo_zeta': 2.59461837e-02
        }
        # initial state is the state in time 6.0.
        # set value
        ufo_env.UfoEnv.__init__(self,

             n_features=12,
             target_x=4100, target_y=3800, target_z=0, target_range=5,
............(private code)
             initial_xpos=initial_xpos,
             reward_type=reward_type))
        # save policy including neuralnetwork
        utils.EzPickle.__init__(self)
