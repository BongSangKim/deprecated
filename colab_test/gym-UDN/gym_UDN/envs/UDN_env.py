import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import torch
import random
import sys
import os
import time

class UDNEnv(gym.Env):
    metadata = {}
    
    def __init__(self):
        self.BSposition = np.loadtxt('BSposition.csv', delimiter=',')
        self.BSnum = len(self.BSposition[0])
        self.InterferenceBSposition = np.loadtxt('InterferenceBSposition.csv', delimiter=',')
        self.InterferenceBSnum = len(self.InterferenceBSposition[0])
        self.Area = 10 ** 2
        self.usernum = 64
        self.BSstate = np.ones(self.BSnum, dtype = bool)
        self.InterferenceBSstate = np.ones(self.InterferenceBSnum, dtype = bool)
        self.user_Xposition = np.random.uniform(0,self.Area,self.usernum)
        self.user_Yposition = np.random.uniform(0,self.Area,self.usernum)
        self.action_space = spaces.Discrete(2**self.BSnum)
        self.movedistance = None
        self.state = self.state_change()
        self.bandwidth = 10**7
        self.theta = 1
        self.threshold = 120 * 10 ** 6 #bit/s
    
    def step(self, action):

        if action == 0:
            reward = -100
            is_done = True
            info = np.zeros(self.BSnum)
            info2 = np.array([0,0])
            return self.state, reward, is_done, info, info2

        #return state action pair reward 
        self.take_action(action)

        Datarate_weightvalue = 1
        Energyconsumption_weightvalue = 1
        info = self.BSstate.astype(float)
        
        signal = self.BS_User_S()

        Interference = self.Interference_User_I()

        SIR = signal / Interference

        Datarate = self.bandwidth * np.log2(1+SIR)

        avg_Pcov=np.sum(SIR>self.theta)/self.usernum

        Energyconsumption = np.sum(self.BSstate.astype(float)) * 17 + self.BSnum * 39 #+ self.usernum * 2.6

        if Energyconsumption == 0:
            reward = -1
            is_done = True
        else:
            is_done =False

            if avg_Pcov < 0.7:
                reward = -1
                is_done = True
            else:
                is_done = False

        reward = Datarate_weightvalue * np.sum(Datarate) / (10 ** 6) / (Energyconsumption_weightvalue * Energyconsumption)
        is_done = False
        info = self.BSstate.astype(float)
        info2 = np.array([np.sum(Datarate),Energyconsumption])
        self.state = self.state_change()
        return self.state, reward, is_done, info, info2#for visualizing
    
    def reset(self):
        self.BSstate = np.ones(self.BSnum,dtype = bool)
        self.state = self.state_change()
        
        return self.state
    
    def take_action(self, action):
        #do action for change state
        self.BSstate = self.Binarychange(action,self.BSnum)

        InterferenceBS_on_probability = action / self.BSnum
        while np.sum(self.InterferenceBSstate) == 0:
            self.InterferenceBSstate = InterferenceBS_on_probability > np.random.rand(*self.InterferenceBSstate.shape)

    def state_change(self):
        self.user_Xposition = np.random.uniform(0,self.Area,self.usernum)
        self.user_Yposition = np.random.uniform(0,self.Area,self.usernum)

        user_Xposition_persent = self.user_Xposition / self.Area
        user_Yposition_persent = self.user_Yposition / self.Area

        user_in_area = np.zeros(10)

        for i in range(self.usernum):
            if user_Yposition_persent[i] < 0.3:
                if user_Xposition_persent[i] < 0.3:
                    user_in_area[0] += 1
                elif user_Xposition_persent[i] > 0.6:
                    user_in_area[2] += 1
                else:
                    user_in_area[1] += 1
            elif user_Yposition_persent[i] > 0.6:
                if user_Xposition_persent[i] < 0.3:
                    user_in_area[6] += 1
                elif user_Xposition_persent[i] > 0.6:
                    user_in_area[8] += 1
                else:
                    user_in_area[7] += 1
            else:
                if user_Xposition_persent[i] < 0.3:
                    user_in_area[3] += 1
                elif user_Xposition_persent[i] > 0.6:
                    user_in_area[5] += 1
                else:
                    user_in_area[4] += 1

        user_in_area[9] = np.sum(self.InterferenceBSstate)

        return user_in_area

    
    def Binarychange(self,num,tnum):
        #hex number to binary matrix
        hnum = num
        bmatrix = np.zeros(tnum)
        index = 0
        while True:
            if index == tnum:
                break
            else:
                bmatrix[index] = hnum % 2
                hnum = hnum // 2
                index += 1
        bmatrix = bmatrix.astype(bool)
        return bmatrix
    
    def Hexchange(self,mat):
        #binary matrix to hex number
        size = len(mat)
        hxnum = 0
        for i in range(size):
            hxnum += mat[i] * 2 ** (size - i - 1)
        return hxnum
    
    def BS_User_S(self):
        #calculate Signal power consist path loss for each user
        #return 1 by usernum matrix include signal power for each user
        BS_xposition = self.BSposition[0,:]
        BS_xposition = BS_xposition.reshape(1, self.BSnum)

        BS_yposition = self.BSposition[1,:]
        BS_yposition = BS_yposition.reshape(1, self.BSnum)

        user_xposition = self.user_Xposition.reshape(1, self.usernum)
        user_yposition = self.user_Yposition.reshape(1, self.usernum)

        BS_user_distance = np.sqrt((BS_xposition - user_xposition.T)**2+(BS_yposition - user_yposition.T)**2)

        signal_channel = self.channel_calculate(BS_user_distance, self.BSstate)

        BS_user_distance_on = BS_user_distance[:,self.BSstate]
        idx_near = np.argmin(BS_user_distance_on, axis=1)
        idx_main = idx_near

        user_signal_power = signal_channel[range(self.usernum), idx_main]

        return user_signal_power
    
    def Interference_User_I(self):
        #calculate Interference power consist path loss for each user
        #return 1 by usernum matrix include interference power for each user
        sigma = 0

        InterferenceBS_xposition = self.InterferenceBSposition[0,:]
        InterferenceBS_xposition = InterferenceBS_xposition.reshape(1, self.InterferenceBSnum)
        
        InterferenceBS_yposition = self.InterferenceBSposition[1,:]
        InterferenceBS_yposition = InterferenceBS_yposition.reshape(1, self.InterferenceBSnum)

        user_xposition = self.user_Xposition.reshape(1, self.usernum)
        user_yposition = self.user_Yposition.reshape(1, self.usernum)

        InterferenceBS_user_distance = np.sqrt((InterferenceBS_xposition - user_xposition.T)**2+(InterferenceBS_yposition - user_yposition.T)**2)

        interference_channel = self.channel_calculate(InterferenceBS_user_distance, self.InterferenceBSstate)

        Interference_power = np.sum(interference_channel, axis=1) + sigma

        return Interference_power
    
    def channel_calculate(self, distance, BS_on):

        aL = 2.5; aN = 4;a_diff = aN-aL; # pathloss exponent for the LoS, NLoS
        mL = 10; mN = 1;m_diff = mL-mN; #Nakagami-m fading parameters for the LoS, NLoS channel
        hij = 25-1.5# height difference = 25-1.5

        NLoS = self.LoS_probability(distance)
        LoS=1-NLoS

        PL=(distance**2+hij**2)**(-(aL+NLoS*a_diff))*BS_on
        CH=PL*np.random.gamma(mN+m_diff*LoS, 1/(mN+m_diff*LoS))

        return CH

    def LoS_probability(self, dist):
        #return NLoS state

        NLoS = np.zeros((len(dist), len(dist[0])))
        LoSP=lambda d : min(18/d, 1)*(1-np.exp(-d/63))+np.exp(-d/63)

        for i in range(len(dist)):
            for j in range(len(dist[0])):
                NLoS[i,j] = LoSP(dist[i, j]) < np.random.rand()

        return NLoS


'''
if __name__ == "__main__":
    start_time = time.time()
    env = UDNEnv()
    env.reset()
    action = 255
    _, R, _, I = env.step(action)
    print(R)
    print(I)
    end_time = time.time()
    print("Runningtime: {} sec".format(end_time - start_time))
'''