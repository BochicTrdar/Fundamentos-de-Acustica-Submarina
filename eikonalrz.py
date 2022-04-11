# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import integrate
from matplotlib.pyplot import *

ds = 100 # Passo do raio

Dmax = 5000
Rmaxkm = 100 
Rmax = Rmaxkm*1000

# Posição da fonte:
rs = 0
zs = 1500

s = arange(rs,Rmax+ds,ds) # comprimento do raio

# Função para o perfil de Munk:

z0 = 1500.0
c0 = 1480.0

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
    sr = Y[2]
    sz = Y[3]
    c,dcdz = munk(z,z0,c0)
    cc = c*c
    dcdr = 0.0
    drds = c*sr
    dzds = c*sz
    dsrds = -dcdr/cc
    dszds = -dcdz/cc
    return [drds,dzds,dsrds,dszds]

# Definir ângulos de lançamento:

nrays = 25
thetas = linspace(-12,12,nrays)

for i in range(nrays):
    sr0 = cos( -thetas[i]*pi/180 )/c0
    sz0 = sin( -thetas[i]*pi/180 )/c0
    y0 = [rs, zs, sr0, sz0]
    # Integrar a ODE:
    y = integrate.odeint(solver, y0, s)

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

