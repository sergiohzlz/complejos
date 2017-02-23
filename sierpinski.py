from random import choice
from matplotlib import pyplot as plt


v1 = (0.,0.)
v2 = (1.,0.)
v3 = (0.5, 1.0)

V = [v1, v2, v3]
p0 = (0.5, 0.)
T = [p0]

pmedio = lambda x,y: ( (x[0]+y[0])/2 , (x[1]+y[1])/2 )

iters = 100000

for i in range(iters):
    idx = choice([0,1,2])
    vact = V[idx]
    pact = T[-1]
    psig = pmedio(pact,vact)
    T.append(psig)

for p in T:
    plt.scatter( p[0], p[1], s=0.2 )

plt.show()
