import numpy as np
import gym

# import pandas as pd
time = 8 #20.0

X_his = []
Y_his = []
Z_his = []
VEL_his = []
THETA_A_his = []
PSI_2_his = []
PHI_A_his = []
PHI_2_his = []
GAMMA_his = []
OMEGA_XI_his = []
OMEGA_ETA_his = []
OMEGA_ZETA_his = []
time_steps =  (time-6) // 0.02  # 4000 steps
# env = gym.make('UfoReach-v1')
env = gym.make('SafeUfoReachEnv2-v1')
# env.reset()
# for i in range(1000):
#     action = env.action_space.sample()
#     print(action)


for i in range(100):
    env.reset()
    n = 0
    done = False
    while not done:
        action = env.action_space.sample()
        # print(action)
        obs, reward, done, info = env.step(action)
        # print(action,reward)

        # print(done)
        n = n+1
        if done:
            print(n)
            print(reward)
            # print('achieved_goal {}'.format(obs[0:3]))
            # print('desired_goal {}'.format(obs[12:]))
            print(np.linalg.norm(obs[0:3]-obs[12:]))

#     X_his.append(env.sim.X)
#     Y_his.append(env.sim.Y)
#     Z_his.append(env.sim.Z)
#     VEL_his.append(env.sim.VEL)
#     THETA_A_his.append(env.sim.THETA_A)
#     PSI_2_his.append(env.sim.PSI_2)
#     PHI_A_his.append(env.sim.PHI_A)
#     PHI_2_his.append(env.sim.PHI_2)
#     GAMMA_his.append(env.sim.GAMMA)
#     OMEGA_XI_his.append(env.sim.OMEGA_XI)
#     OMEGA_ETA_his.append(env.sim.OMEGA_ETA)
#     OMEGA_ZETA_his.append(env.sim.OMEGA_ZETA)


# # print(X_his)


# # np.savetxt('dataY.txt',Y_his,delimiter=',')
# # np.savetxt('dataZ.txt',Z_his,delimiter=',')
# # np.savetxt('dataVEL.txt',VEL_his,delimiter=',')
# # np.savetxt('dataTHETA_A.txt',THETA_A_his,delimiter=',')
# # np.savetxt('dataPSI_2.txt',PSI_2_his,delimiter=',')
# # np.savetxt('dataPHI_A.txt',PHI_A_his,delimiter=',')
# # np.savetxt('dataPHI_2.txt',PHI_2_his,delimiter=',')
# # np.savetxt('dataGAMMA.txt',GAMMA_his,delimiter=',')
# # np.savetxt('dataOMEGA_XI.txt',OMEGA_XI_his,delimiter=',')
# # np.savetxt('dataOMEGA_ETA.txt',OMEGA_ETA_his,delimiter=',')
# # np.savetxt('dataOMEGA_ZETA.txt',OMEGA_ZETA_his,delimiter=',')
