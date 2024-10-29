import numpy as np
from matplotlib import pyplot as pp

def f(x):
    return 2 + 0.75*(np.tanh(2*x))
def deriv(x):
    return 1.5*(((1/np.cosh(2*x))**2))

step1=[]
step0_5=[]
step0_1=[]
h1=-1
h2=-1.5
h3=-1.9
x1=[]
x2=[]
x3=[]
derivative=[]
for i in range(40):
    step0_1.append((f(h3-0.1)+f(h3+0.1))/(2*0.1))
    x1.append(h3)
    h3+=0.1
for i in range(7):
    step0_5.append((f(h2-0.5)+f(h2+0.5))/(2*0.5))
    x2.append(h2)
    h2+=0.5
for i in range(3):
    step1.append((f(h1-1)+f(h1+1))/2)
    x3.append(h1)
    h1+=1
    
step=-2
x4=[]
for i in range(39):
    derivative.append(deriv(step))
    x4.append(step)
    step+=0.1

print(step0_1)
   
pp.plot(x1,step0_1)
pp.plot(x2,step0_5)
pp.plot(x3,step1)
pp.plot(x4,derivative,'--')
pp.show()