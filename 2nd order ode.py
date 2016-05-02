import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
def model(u,t):
    y=u[0]
    dy=u[1]
    k=30
    udot=[[],[]]
    udot[0]=dy
    udot[1]=-k*y-(.9+.7*t)*dy
    return udot
time=np.linspace(0,2,10)
'''yinit=np.array([0,0])'''
    
z2=odeint(model,[2,-1],time)
'''print y'''
plt.plot(time,z2[:0],'k-')
plt.show()
print z2[:,0]
    
    
    
    