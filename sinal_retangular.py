# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

amostragem = 1000
tmax = 10.0
nyquist = amostragem/2
w1 = 2*pi*nyquist/50
dt = 1.0/amostragem
t = arange(0,tmax,dt)
s = zeros( t.size )
s[0:nyquist] = 1.0
sn =  s[::-1]
tn = -t[::-1]
f = linspace(-amostragem,amostragem,2*t.size)
w = 2*pi*f
S = real( fft(s) )
Sn =  S[::-1]
snp = hstack((sn,s))
tnp = hstack((tn,t))
Snp = hstack((Sn,S))
Snp = Snp/max( abs( Snp ) )

figure(1)
subplot(211),plot(tnp,snp,'k',linewidth=2)
xlabel('$t$ (s)')
ylabel(r'$\Pi(t)$')
xlim(-1,1)
ylim(-0.1,1.1)
grid(True)
subplot(212),plot(w,Snp,'k',linewidth=2)
xlabel(r'$\omega$ (rad/s)')
ylabel(r'FT[$\Pi(t)$]')
xlim(-w1,w1)
ylim(-0.25,1.1)
grid(True)
show()
