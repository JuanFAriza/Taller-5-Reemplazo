import numpy as np
import matplotlib.pyplot as plt
sigma = 0.1
v = 5.0

x = np.array([3,3,4,4,5,5],dtype='float')
y = np.array([15,16,15,16,15,16],dtype='float')
tini = np.array([3.12,3.26,2.98,3.12,2.84,2.98],dtype='float')

N = 10**5
delta = 0.1

x0 = 14.0
y0 = 0.0

def t_mod(posx,posy):
    t = np.zeros(6,dtype='float')
    dis = np.sqrt((x - posx)**2 + (y - posy)**2)
    t = dis/v
    return t

def prob_obs_log(posx,posy):
    p = -np.sum((tini - t_mod(posx,posy))**2)/(2*sigma**2)
    return p

posx = np.array([x0],dtype='float')
posy = np.array([y0],dtype='float')

for i in range(N):
    xnew = posx[i] + np.random.rand()*2*delta - delta
    ynew = posy[i] + np.random.rand()*2*delta - delta

    alpha = min(1,np.exp(prob_obs_log(xnew,ynew) - prob_obs_log(posx[i],posy[i])))
    u = np.random.rand()
    if (u < alpha):
        posx = np.append(posx,xnew)
        posy = np.append(posy,ynew)
    else:
        posx = np.append(posx,posx[i])
        posy = np.append(posy,posy[i])

plt.scatter(posx,posy)
plt.scatter(x,y)
plt.show()
print np.median(posx)
print np.median(posy)
