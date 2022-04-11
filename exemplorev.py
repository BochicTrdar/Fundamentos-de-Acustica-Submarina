# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

# Parâmetros:
SL  = 0
phi = 2*pi
tau = 1 # Duração do pulso
freq   = 3000
Dmax   = 1000
zs     = 500.0
cw    = 1500.0

nr = 501
rmin =  100.0
rmax = 1000.0
r = linspace(rmin,rmax,nr)

s1 = 0.016
s2 = 0.002
sigma = linspace(s1,s2,nr) # Idealizado

trev  = ones(nr)
RL    = ones(nr)

for i in range(nr):
    ri = sqrt(r[i]*r[i] + (Dmax-zs)**2.0)
    TL = 10*log10( abs( ri ) )
    A = 0.5*cw*tau*pi*ri
    RLb = 10*log10(A)
    RL[i] = SL - 2*TL + 10*log10( sigma[i] ) + RLb
    trev[i] = 2*ri/cw

figure(1)
plot(trev,RL,'k',linewidth=2)
xlabel('Tempo (s)',fontsize=18)
ylabel('RL (dB)'  ,fontsize=18)
grid(True)

show()
