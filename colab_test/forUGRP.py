import numpy as np

# bs_x, bs_y : BS coordinates, N dimensional vector(number of BSs)
# ue_x, ue_y : UE coordinates, M dimensional vector(number of UEs)
# bs_on : one-hot vector that represent whether BSs are on/off
# Dist : N x M matrix, component for the distance between BS and user

### test values
bs_x=np.array([-1, 3, 10]);bs_y=np.array([-33, 10, 0]); # BS locations
ue_x=np.random.rand(4)*10-5;ue_y=np.random.rand(4)*10-5; # UE locations
aL=2.5; aN=4;a_diff=aN-aL; # pathloss exponent for the LoS, NLoS
mL=10; mN=1;m_diff=mL-mN; #Nakagami-m fading parameters for the LoS, NLoS channel
hij=25-1.5# height difference = 25-1.5
bs_on=[1, 0, 1]

Dist = np.sqrt((bs_x-ue_x.T)**2+(bs_y-ue_y.T)**2) # BS-UE distance pairs
LoSP=lambda d : min(18/d, 1)(1-np.exp(-d/63))+np.exp(-d/63)

NLoS=np.array(list(map(LoSP, Dist)))>np.random.rand(*Dist.shape); LoS=1-NLoS;

PL=(Dist**2+hij**2)**(-(aL+NLoS*a_diff))*bs_on
CH=PL*np.random.gamma(mN+m_diff*LoS, 1/(mN+m_diff*LoS))
# nearest BS association
idx_near = np.argmin(Dist, axis=1)
# strongest BS association
idx_str = np.argmax(CH, axis=1)
idx_main=idx_near

sigma=0;theta=1;
S=CH[range(len(ue_x)), idx_main];
I=np.sum(CH, axis=1)-S+sigma;

rate=np.sum(np.log2(1+S/I));
avg_Pcov=np.sum(S/I>theta)/len(ue_x)

energy=np.sum(BS_on)*e_act + nU*t_base + nB*e_base



