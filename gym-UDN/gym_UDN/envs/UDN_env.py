import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import torch
import random
import sys
import os

class UDNEnv(gym.Env):
    metadata = {}
    
    def __init__(self):
        self.BSposition = np.loadtxt('BSposition.csv', delimiter=',')
        self.BSnum = len(self.BSposition[0])
        self.InterferenceBSposition = np.loadtxt('InterferenceBSposition.csv', delimiter=',')
        self.InterferenceBSnum = len(self.InterferenceBSposition[0])
        self.Area = 10 ** 2
        self.usernum = 100
        self.BSstate = np.ones(self.BSnum, dtype = bool)
        self.InterferenceBSstate = np.random.randint(2, size = self.InterferenceBSnum)
        self.user_Xposition = np.random.uniform(0,self.Area,self.usernum)
        self.user_Yposition = np.random.uniform(0,self.Area,self.usernum)
        self.action_space = spaces.Discrete(2**self.BSnum)
        self.movedistance = None
        self.state = np.r_[self.user_Xposition,self.user_Yposition,self.Hexchange(self.InterferenceBSstate)]
        self.bandwidth = 10**7
        self.threshold = 120 * 10 ** 6 #bit/s
        
    
    def step(self, action):
        #
        #return state action pair reward 
        self.take_action(action)
        
        Datarate_weightvalue = 1
        Energyconsumption_weightvalue = 0.5
        
        signal = self.BS_User_S()
        Interference = self.Interference_User_I()
        #SIR = signal / Interference
        SIR = signal - Interference
        #Datarate = self.bandwidth * np.log2(1+SIR)
        Datarate = self.bandwidth * np.log2(1+10**(SIR/10))
        #coverage_prob = np.sum(Datarate > self.threshold) / self.usernum
        #print(coverage_prob)
        Energyconsumption = np.sum(self.BSstate.astype(float))
        if Energyconsumption == 0:
            reward = -1000
            is_done = True
        else:
            reward = Datarate_weightvalue * np.sum(Datarate) / (10 ** 6) - (Energyconsumption_weightvalue * Energyconsumption)
            #reward = 1.0
            is_done =False
        #if coverage_prob < 0.7:
            #reward = -10
            #is_done = True
        #else:
            #is_done = False
        #reward = Datarate_weightvalue * np.sum(Datarate) / (10 ** 6) - (Energyconsumption_weightvalue * Energyconsumption)
        #is_done = False
        info = self.BSstate.astype(float)
        self.InterferenceBSstate = np.random.randint(2, size = self.InterferenceBSnum)
        self.state[2 * self.usernum] = self.Hexchange(self.InterferenceBSstate)
        return self.state, reward, is_done, info#for visualizing
    
    def reset(self):
        self.BSstate = np.ones(self.BSnum,dtype = bool)
        self.user_Xposition = np.random.uniform(0,self.Area,self.usernum)
        self.user_Yposition = np.random.uniform(0,self.Area,self.usernum)
        self.InterferenceBSstate = np.random.randint(2, size = self.InterferenceBSnum)
        self.state = np.r_[self.user_Xposition,self.user_Yposition,self.Hexchange(self.InterferenceBSstate)]
        
        return self.state
    
    def take_action(self, action):
        #do action for change state
        self.BSstate = self.Binarychange(action,self.BSnum)
        self.movedistance = self.usermovedistance()
        
        
        for j in range(2*self.usernum):
            self.state[j] = self.state[j] + self.movedistance[j]
            if self.state[j] > self.Area:
                self.state[j] = self.state[j] - self.Area
            if self.state[j] < 0:
                self.state[j] = self.state[j] + self.Area
            
    
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

    def usermovedistance(self):
        #human walking speed 1.3m/s = 4.68km/h
        theta = np.random.uniform(0,2*np.pi,self.usernum) #random angle for each user
        d = np.random.uniform(0,1.3,self.usernum)#random distance for each user
        sin = np.sin(theta)
        cos = np.cos(theta)
        x_dis = d*cos
        y_dis = d*sin
        state_dis = np.r_[x_dis,y_dis] #form for state
        return state_dis
    
    def BS_User_S(self):
        #calculate Signal power consist path loss for each user
        #return 1 by usernum matrix include signal power for each user
        BS_User_position = np.zeros((2,self.usernum,self.BSnum))
        BS_User_distance = np.zeros((self.usernum,self.BSnum),dtype = float)
        user_signal_power = np.zeros(self.usernum,dtype = float)
        # axis x = 0, axis y = 1
        for i in range(self.usernum):
            for j in range(self.BSnum):
                BS_User_position[0][i][j] = self.state[i] - self.BSposition[0][j]
                BS_User_position[1][i][j] = self.state[self.usernum + i] - self.BSposition[1][j]
        BS_User_distance = np.linalg.norm(BS_User_position, ord = 2, axis = 0)
        for i in range(self.BSnum):
            if self.BSstate[i]:
                pass
            else:
                BS_User_distance[:,i] = np.inf
        #BS_User_distance = BS_User_distance[:,self.BSstate]
        assosiation_matrix = self.assosiation(BS_User_distance)
        #user_signal_power = np.power(BS_User_distance[assosiation_matrix],-2)
        user_signal_power = 10 * 4 * np.log10(BS_User_distance[assosiation_matrix]) + 20 * np.log10(3.5 * 10 ** 9) - 147.55
        return user_signal_power
    
    def Interference_User_I(self):
        #calculate Interference power consist path loss for each user
        #return 1 by usernum matrix include interference power for each user
        InterferenceBS_User_position = np.zeros((2,self.usernum,self.InterferenceBSnum))
        InterferenceBS_User_distance = np.zeros((self.usernum,self.BSnum), dtype = float)
        InterferenceBSstate_bool = self.InterferenceBSstate.astype(bool)
        user_interference_power = np.zeros(self.usernum,dtype = float)
        user_interference_path_loss = np.zeros(self.usernum,dtype = float)
        #axis x = 0, axis y = 1
        for i in range(self.usernum):
            for j in range(self.InterferenceBSnum):
                InterferenceBS_User_position[0][i][j] = self.state[i] - self.InterferenceBSposition[0][j]
                InterferenceBS_User_position[1][i][j] = self.state[self.usernum + i] - self.InterferenceBSposition[1][j]
        Interference_User_distance = np.linalg.norm(InterferenceBS_User_position, ord = 2, axis = 0)

        if np.sum(self.InterferenceBSstate) == 0:
            #user_interference_path_loss =  np.power(np.mean(Interference_User_distance,axis = 1),-2)
            user_interference_path_loss = 10 * 4 * np.log10(np.mean(Interference_User_distance,axis = 1)) + 20 * np.log10(3.5 * 10 ** 9) - 147.55

        else:
            Interference_User_distance = Interference_User_distance[:,InterferenceBSstate_bool]
            inter_bandwidth_num = self.InterferenceBSposition[2,InterferenceBSstate_bool]
            for i in range(self.usernum):
                for j in range(len(inter_bandwidth_num)):
                    if inter_bandwidth_num[j] == self.user_BS_shortest[i]:
                        user_interference_power[i] = user_interference_power[i] + Interference_User_distance[i,j]

            for i in range(self.usernum):
                if user_interference_power[i] == 0:
                    user_interference_power[i] = np.mean(Interference_User_distance[i])

            #user_interference_path_loss =  np.power(user_interference_power,-2)
            user_interference_path_loss = 10 * 4 * np.log10(user_interference_power) + 20 * np.log10(3.5 * 10 ** 9) - 147.55
        return user_interference_path_loss
    

    def assosiation(self, distance):
        #calculate user-BS assosiation follow shortest distance assosiation rule
        #return usernum by BSnum matrix dtype boolean
        BS_user_assosiation = np.zeros((self.usernum,self.BSnum),dtype = bool)
        #BS_user_assosiation = BS_user_assosiation[:,self.BSstate]
        self.user_BS_shortest = np.argmin(distance,axis = 1)
        for i in range(self.usernum):
            BS_user_assosiation[i][self.user_BS_shortest[i]] = True
        #print(BS_user_assosiation)
        return BS_user_assosiation

'''
if __name__ == "__main__":
    env = UDNEnv()
    env.reset()
    action = 1
    _, R, _, I = env.step(action)
    print(R)
    print(I)
'''