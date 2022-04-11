# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import integrate
from matplotlib.pyplot import *

dr = 100 # Passo em distância horizontal

Dmax = 5000
Rmaxkm = 100 
Rmax = Rmaxkm*1000

# Posição da fonte:
rs = 0
zs = 1500

r = arange(rs,Rmax+dr,dr); rkm = r/1000.0

def solver(Y,r):
    p = Y[0]
    z = Y[1]
    B = 1.3e3
    epsilon = 7.37e-3
    z1 = 1500.0
    c1 = 1480.0
    eta = 2*( z - z1 )/B
    c   = c1*( 1 + epsilon*( eta + exp( -eta ) - 1 ) ) 
    dcdz = ( 2*c1*epsilon/B  )*( 1 - exp( -eta ) )
    ccc = c**3
    dHdz = c1*c1/ccc*dcdz
    dHdp = p
    return [-dHdz,dHdp]

# Definir ângulos de lançamento:

nrays = 25
thetas = linspace(-12,12,nrays)

for i in range(nrays):
    p0 = tan( -thetas[i]*pi/180 )
    z0 = zs
    y0 = [p0,z0]
    # Integrar a ODE:
    y = integrate.odeint(solver, y0, r)
    z = squeeze( y[:,1] )

    figure(1)
    plot(rkm,z,'k',linewidth=2)

xlabel(u'Distância (km)',fontsize=18)
ylabel('Profundidade (m)',fontsize=18)
xlim(0,Rmaxkm)
ylim(Dmax,0)
grid(True)

show()

