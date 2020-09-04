import gym
import numpy as np
env = gym.make('SafeUfoReachEnv2-v1')

obs = env.reset()

for i in range(50):

    action = np.array([20]) #env.action_space.sample()

    # print(type(env.ACs))# a tuple
    # print(f"action{action}")
    # print(f"env.ACs{env.ACs}")

    obs, reward, done, info = env.step(action)
    # print(obs)
    # print(reward)
    # print(done)
    # print(info)

    if done:

        # print(f"env.ACs{env.ACs}")\
        print(obs)

        break
print(obs)
print(np.random.randint(50,int(2/0.02)-1))
# print result
#  $ obs = env.reset()
# {'observation': array([0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 9.60000000e+02,
#        7.85398163e-01, 0.00000000e+00, 8.02851456e-01, 0.00000000e+00,
#        0.00000000e+00, 3.14159265e+01, 0.00000000e+00, 0.00000000e+00]),
# 'achieved_goal': array([0., 0., 0.]), 'desired_goal': array([4100., 3800.,    0.])}
#  $ step()
# {'observation': array([ 1.35769618e+00,  1.35739707e+00, -1.50081428e-04,  9.59833118e+02,
#         7.85133757e-01, -1.87622218e-04,  8.02818041e-01, -4.97199329e-08,
#         6.14646156e-02,  2.98044651e+01,  8.28954985e-05, -4.00974522e-02]),
# 'achieved_goal': array([ 1.35769618e+00,  1.35739707e+00, -1.50081428e-04]),
# 'desired_goal': array([4100., 3800.,    0.])}
# -1.0
# False
# {'is_success': 0.0}
