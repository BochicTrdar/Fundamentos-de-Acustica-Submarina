# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

f1 =  5
f2 = 50
f3 = 75
amostragem = 500 
nyquist = amostragem/2
dt = 1.0/amostragem
t = arange(0,1,dt)
w1 = 2*pi*f1
w2 = 2*pi*f2
w3 = 2*pi*f3
s = cos( w1*t ) + cos( w2*t ) + cos( w3*t )
S = fft(s)
Saux = fft(s)

P = real( S*conj( S ) )
P = P/max( P )
frequencias = linspace(0,amostragem,amostragem)
# Filtro improvisado: 
# remover componentes não desejadas:
f = abs( frequencias - f1 )
inutil,i1 = f.min(0),f.argmin(0)
f = abs( frequencias - amostragem + f1 )
inutil,i2 = f.min(0),f.argmin(0)
Saux[i1+10:i2-10] = 0;
sf = real( ifft(Saux) )

figure(1)
plot(t,s,'k',linewidth=2)
grid(True)
xlabel('Tempo (s)',fontsize=18)
ylabel('Amplitude',fontsize=18)

figure(2)
plot(frequencias,P,'k',linewidth=2)
xlim(0,f3+25)
grid(True)
xlabel(u'Frequência (Hz)',fontsize=18)
ylabel('Amplitude',fontsize=18)

ef,et,Sxx = signal.spectrogram(s,amostragem)

figure(3)
imshow(Sxx, cmap='Greys',
extent=[et[0],et[-1],ef[0],ef[-1]],
aspect='auto',origin='lower')
xlabel('Tempo (s)',fontsize=18)
ylabel(u'Frequência (Hz)',fontsize=18)
ylim(0,150)

figure(4)
plot(t,sf,'k',linewidth=2)
xlabel('Tempo (s)',fontsize=18)
ylabel('Amplitude',fontsize=18)
grid(True)
show()
