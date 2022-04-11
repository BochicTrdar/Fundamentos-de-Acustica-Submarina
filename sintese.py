# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

fmin =  20
fmax = 100
amostragem = 1000 
nyquist = int( amostragem/2 )
frequencias = arange(0,amostragem,1)
w = 2*pi*frequencias
S = zeros(amostragem) + 1j*zeros(amostragem)
dt = 1.0/amostragem
t = arange(0,1,dt)
t0 = 0.5
t0 = dt*int( t0/dt )

fpulse = arange(fmin,fmax+1,1)
L = fpulse.size

for i in range(L):
    fi = int( fpulse[i] )
    S[fi]            = ( 1.0 + 1j*0 )*nyquist/L
    S[amostragem-fi] = ( 1.0 + 1j*0 )*nyquist/L

S = S*exp( -1j*w*t0 )
s = real( ifft( S ) )

figure(1)
plot(frequencias,abs(S),'k',linewidth=2)
xlabel(u'Frequência (Hz)',fontsize=18)
ylabel('Amplitude',fontsize=18)
ylim(0,1.1)
grid(True)

figure(2)
plot(t,s,'k',linewidth=2)
xlabel('Tempo (s)',fontsize=18)
ylabel('Amplitude',fontsize=18)
grid(True)

show()
