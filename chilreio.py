# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

amostragem = 1000
nyquist = amostragem/2 
dt = 1.0/amostragem
t = arange(0,1,dt) # tmax = 1 s
s  = zeros( amostragem )
f0 =  5.0
f1 =  5.0
f2 = 50.0
k = (f2-f1) # dividir por tmax se tmax ~= 1
freq = k*t + f0
w = 2.0*pi*freq
fase = cumsum( w )*dt # Fase = integral de w(t) 
s = cos( fase )
S = fft( s )
PSD = real( S*conj( S ) )
PSD = PSD/max( PSD )
frequencias = linspace(0,amostragem,amostragem)

figure(1)
plot(t,s,'k',linewidth=2)
grid(True)
xlabel('Tempo (s)',fontsize=18)
ylabel('Amplitude',fontsize=18)

figure(2)
plot(frequencias,PSD,'k',linewidth=2)
xlim(0,2*f2)
grid(True)
xlabel(u'Frequência (Hz)',fontsize=18)
ylabel('Amplitude',fontsize=18) 

ef,et,Sxx = signal.spectrogram(s,
amostragem,nperseg=64,nfft=256)

figure(3)
imshow(Sxx, cmap='Greys',
extent=[et[0],et[-1],ef[0],ef[-1]],
aspect='auto',origin='lower')
ylim(0,2*f2)
xlabel('Tempo (s)',fontsize=18)
ylabel(u'Frequência (Hz)',fontsize=18)

show()
