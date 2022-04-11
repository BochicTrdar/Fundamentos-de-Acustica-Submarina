# coding=utf-8
from numpy import * 
from scipy import *
from scipy.signal import correlate
from matplotlib.pyplot import *

a = -1.0
b =  1.0
amostragem = 1000 
n = 2*random.uniform(a,b,amostragem) # Ruído
dt = 1.0/amostragem
t = arange(0,1,dt)
freq = 50
w = 2*pi*freq
s = cos( w*t ) + n # Ruído no sinal
# Autocorrelação:
R = correlate( s, s, mode='full')
L = R.size
tR = dt*( arange(L) - L/2 )
figure(1)
subplot(211),plot(t,s,'k')
ylabel(r'$s(t)$')
grid(True)
subplot(212),plot(tR,R,'k',linewidth=2)
ylabel(r'$R(\tau)$')
xlabel('Tempo (s)',fontsize=18)
xlim(-0.5,0.5)
grid(True)
show()
