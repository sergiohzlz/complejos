from pylab import *
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D

def lv(r, alfa=0.4, beta=0.018, gamma=0.8, delta=0.023):
    (x, y) = r
    dp_dt = alfa*x - beta*x*y
    dd_dt = -gamma*y + delta*x*y

    return [dp_dt, dd_dt]

def euler(f, r0, h, N):
    k = len(r0)
    P = zeros((N,k))
    P[0] = r0
    for i in range(1,N):
        pa = P[i-1]
        P[i] = pa + h*array(f(pa))
    return P



# Posicion inicial
r0 = [30, 1]

#Intervalo de tiempo
tf = 100.0
h = 0.0001
t=arange(0,tf,0.0001)


#solucion del sistema
#pos = odeint(f, r0, t)
pos = euler(lv, r0, h, len(t))
x = pos[:, 0]
y = pos[:, 1]



fig1 = figure(1)
plot(x, y)
title('Lotka - Volterra')
xlabel('presa')
ylabel('depredador')

savefig('lv1.pdf')

#
fig2 = figure(2)
plot(t,x,t,y)
#label(['presa','depredador'],[x[0],y[0]])

savefig('serieslv.pdf')


show()
