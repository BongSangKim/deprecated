import numpy as np; #NumPy package for arrays, random number generation, etc
import matplotlib.pyplot as plt #for plotting
import pandas as pd

#Simulation window parameters
startpoint = [[-100,-1000],[-100,0],[-100,1000],[0,-100],[0,100],[100,-100],[100,0],[100,100]]
xx = np.array([])
yy = np.array([])
hz = np.array([])
xDelta=100;yDelta=100; #rectangle dimensions
areaTotal=xDelta*yDelta;

#Point process parameters
lambda0=1*10**-3 #intensity (ie mean density) of the Poisson process

#Simulate a Poisson point process
for i,j in startpoint:
    numbPoints = np.random.poisson(lambda0*areaTotal);#Poisson number of points
    xx = np.r_[xx,xDelta*np.random.uniform(0,1,numbPoints)+i];#x coordinates of Poisson points
    yy = np.r_[yy,yDelta*np.random.uniform(0,1,numbPoints)+j];#y coordinates of Poisson points
    hz = np.r_[hz,range(numbPoints)]

df = pd.DataFrame(data = (xx,yy,hz))
df.to_csv("./InterferenceBSposition.csv", index = False, header = False)

