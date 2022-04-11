# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

amostragem = 1000
nyquist = amostragem/2
dt = 1.0/amostragem
t = arange(0,1,dt)
freq = 55 
w = 2*pi*freq
s = cos(w*t)
stau = zeros( amostragem )
tau = 0.19
a = 0.5
n = int( fix( tau/dt) )
stau[n:] = s[0:amostragem-n] # sinal atrasado
p = s + a*stau # sinal mais eco
P = fft( p )
Cc = ifft( log( P ) ) # Cepstrum complexo
#Cr = ifft( log( abs( P ) ) ) # Cepstrum "real"

figure(1)
subplot(211)
plot(t,p,'k',linewidth=2)
xlabel('Tempo (s)')
ylabel(r'$p(t)$')
grid(True)
subplot(212)
plot(t,abs(Cc),'k',linewidth=2)
xlabel(u'Quefrência (s)')
ylabel(r'$|C_c|$')
grid(True)
#subplot(212)
#plot(t,real(Cr),'k',linewidth=2)
#xlabel(u'Quefrência (s)')
#ylabel(r'Re$(C_r)$')
#grid(True)
show()

