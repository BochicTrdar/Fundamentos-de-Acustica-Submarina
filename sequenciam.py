# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

tmin     = 0.0
tmax     = 1.4
amostragem = 10000
nyquist = amostragem/2
dt       = 1.0/amostragem
freq     = 40
w        = 2*pi*freq; T = 1.0/freq
duracao_bit  = 0.2
t = arange(0,duracao_bit,dt) 
nbits    = int( round(tmax/duracao_bit) )
sr = rand( nbits )
sequencia = around( rand(nbits) )
asequencia = str( sequencia )

um = sin( w*t )
s = [] 
for i in range( nbits ):
    if sequencia[i] == 1:
      s = hstack((s,um)) 
    else:
      s = hstack((s,-um))

t = arange(0,tmax,dt)
frequencias, PSD = signal.periodogram(s, 
amostragem,nfft=2018) # periodograma

figure(1)
plot(t,s,'k',linewidth=2)
grid(True)
xlabel("Tempo (s)",fontsize=18)
ylabel("Amplitude",fontsize=18) 
title( asequencia )

figure(2)
plot(frequencias,PSD,'k',linewidth=2)
xlim(0,2*freq)
grid(True)
xlabel(u"Frequência (Hz)",fontsize=18)
ylabel("Amplitude",fontsize=18)

ef,et,Sxx = signal.spectrogram(s,amostragem)

figure(3)
imshow(Sxx, cmap='Greys',
extent=[et[0],et[-1],ef[0],ef[-1]],aspect='auto',origin='lower')
ylim(0,10*freq)
xlabel("Tempo (s)",fontsize=18)
ylabel(u"Frequência (Hz)",fontsize=18)

show()
