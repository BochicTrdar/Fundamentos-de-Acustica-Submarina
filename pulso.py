# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

nfreqs = 101
fmin =  20
fmax = 100
f = linspace(fmin,fmax,nfreqs)
amostragem = 1000 
nyquist = amostragem/2
dt = 1.0/amostragem
t = arange(0,1,dt)
w = 2*pi*f
s = zeros(amostragem)
for i in range(nfreqs):
    s = s + cos( w[i]*(t-0.5) )

s = s/max( abs( s ) )

figure(1)
plot(t,s,'k',linewidth=2)
grid(True)
xlabel('Tempo (s)',fontsize=18)
ylabel('Amplitude',fontsize=18)

ef,et,Sxx = signal.spectrogram(s,
amostragem,noverlap=250)

figure(3)
pcolormesh(et,ef,Sxx,cmap='Greys')
xlabel('Tempo (s)',fontsize=18)
ylabel(u'Frequência (Hz)',fontsize=18)
ylim(0,150)

show()
