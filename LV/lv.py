from pylab import *
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D

def lv(r, t, alfa=0.4, beta=0.018, gamma=0.8, delta=0.023):
    (x, y) = r
    # Sistema de lorenz
    dp_dt = alfa*x - beta*x*y
    dd_dt = -gamma*y + delta*x*y
    
    return [dp_dt, dd_dt]

def euler(f, r0, h):
    N = len(t)
    P = zeros((N,2))
    P[0] = r0
    for i in range(1,N):
        pa = P[i-1]
        P[i] = P[i-1] + h*array(f(pa,1))
    return P



# Posicion inicial
r0 = [30, 4]

#Intervalo de tiempo
tf = 100.0
h = 0.0001
t=arange(0,tf,0.0001)


#solucion del sistema
#pos = odeint(f, r0, t)
pos = euler(lv, r0, h)
x = pos[:, 0]
y = pos[:, 1]



fig1 = figure(1)
plot(x, y)
title('Lotka - Volterra')
savefig('lv1.pdf')

#
fig2 = figure(2)
plot(t,x,t,y)

savefig('serieslv.pdf')



show()
