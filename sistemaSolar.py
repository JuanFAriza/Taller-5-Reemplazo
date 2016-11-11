import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

x_0 = np.array([0.324190175,-0.701534590,-0.982564148,1.104185888,3.266443877,-9.218802228,19.930781147,24.323085642])
y_0 = np.array([0.090955208,-0.168809218,-0.191145980,-0.826097003,-3.888055863,1.788299816,-2.555241579,-17.606227355])
z_0 = np.array([-0.022920510,0.037947785,-0.000014724,-0.044595990,-0.057015321,0.335737817,-0.267710968,-0.197974999])
vx = np.array([-4.627851589,1.725066954,1.126784520,3.260215854,2.076140727,-0.496457364,0.172224285,0.664855006])
vy = np.array([10.390063716,-7.205747212,-6.187988860,4.524583075,1.904040630,-2.005021061,1.357933443,0.935497207])
vz = np.array([1.273504997,-0.198268558,0.000330572,0.014760239,-0.054374153,0.054667082,0.002836325,-0.034716967])

x = np.log(np.sqrt(x_0**2 + y_0**2 + z_0**2))
y = np.log(np.sqrt(vx**2 + vy**2 + vz**2))

N = 10**4

delta_m = 0.1
delta_b = 0.1

m0 = -0.5
b0 = 2

m = np.array([m0],dtype='float')
b = np.array([b0],dtype='float')

def prob_obs_mb(x,y,m,b):
    dif = y - m*x - b
    dif2 = dif*dif
    return np.exp(-0.5*dif2.sum())

for i in range(N):
    mnew = m[i] + np.random.rand()*2*delta_m - delta_m
    bnew = b[i] + np.random.rand()*2*delta_b - delta_b
    if (prob_obs_mb(x,y,m[i],b[i]) == 0):
        alpha = 1
    else:
        alpha = min(1,prob_obs_mb(x,y,mnew,bnew)/(prob_obs_mb(x,y,m[i],b[i])))
    u = np.random.rand()
    if (u < alpha):
        m = np.append(m,mnew)
        b = np.append(b,bnew)
    else:
        m = np.append(m,m[i])
        b = np.append(b,b[i])

plt.scatter(x,y)
x_list = np.linspace(x.min(),x.max(),100)
plt.plot(x_list,np.median(m)*x_list+np.median(b))
plt.show()
