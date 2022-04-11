# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import integrate
from matplotlib.pyplot import *

Dmax = 5000
Rmaxkm = 100 
Rmax = Rmaxkm*1000

# Posição inicial:
rs = 0
zs = 1500

dtau = 0.1
t = arange(0,67.0+dtau,dtau)

z0 = 1500.0
c0 = 1480.0

# Perfil de Munk:
def munk(z,z0,c0):
   B = 1.3e3
   e = 7.37e-3
   eta = 2*( z - z0 )/B
   c   = c0*( 1 + e*( eta + exp( -eta ) - 1 ) )
   dcdz = ( 2*c0*e/B  )*( 1 - exp( -eta ) )
   return c,dcdz
   
# Derivadas:
def solver(Y,s):
    r  = Y[0]
    z  = Y[1]
    X1 = Y[2]
    X2 = Y[3]
    c,dcdz = munk(z,z0,c0)
    X1t = ( 2.0/c )*dcdz*X1*X2
    X2t = ( 1.0/c )*dcdz*( X2*X2 - X1*X1 )
    return [X1,X2,X1t,X2t]

# Ângulos de lançamento:
nrays = 25
thetas = linspace(-12,12,nrays)

for i in range(nrays):
    vr = c0*cos( -thetas[i]*pi/180 )
    vz = c0*sin( -thetas[i]*pi/180 )
    y0 = [rs, zs, vr, vz]
    # Integração da ODE:
    y = integrate.odeint(solver, y0, t)

    r = squeeze( y[:,0] ); rkm = r/1000.0
    z = squeeze( y[:,1] )

    figure(1)
    plot(rkm,z,'k',linewidth=2)

xlabel(u'Distância (km)',fontsize=18)
ylabel('Profundidade (m)',fontsize=18)
xlim(0,Rmaxkm)
ylim(Dmax,0)
grid(True)

show()
