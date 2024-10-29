import numpy as np
from matplotlib import pyplot as pp

def r(x,xp,y):
    return np.sqrt((x-xp)**2+y**2)

def derx(x,xp,y):
    return (x/np.sqrt((x-xp)**2+y**2))

def dery(x,xp,y):
    return (y/np.sqrt((x-xp)**2+y**2))


x=np.arange(-10,10,0.1)
y=np.arange(-10,10,0.1)
X,Y=np.meshgrid(x,y)
Voltage = (1/(4*np.pi*8.55e-12*r(X,-0.05,Y))) + (1/(4*np.pi*8.55e-12*r(X,0.05,Y)))


fig, (ax1) = pp.subplots(1)
cont1 = ax1.contourf(X,Y,Voltage,levels=20)
fig.colorbar(cont1,ax=ax1,label='Voltage (V)')
ax1.set_xlabel('X (cm)')
ax1.set_ylabel('Y (cm)')

Ex=-((1/(4*np.pi*8.55e-12*derx(X,-0.05,Y))) + (1/(4*np.pi*8.55e-12*derx(X,0.05,Y))))
Ey=-((1/(4*np.pi*8.55e-12*dery(X,-0.05,Y))) + (1/(4*np.pi*8.55e-12*dery(X,0.05,Y))))


pp.quiver(X,Y,Ex,Ey)

pp.savefig('potential.png')