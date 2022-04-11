# coding=utf-8
from numpy import * 
from scipy import *
from scipy.signal import correlate, freqz, lfilter
from matplotlib.pyplot import *

amostragem = 10000
nyquist    = amostragem/2
nbranco = random.randn(amostragem)
dt = 1.0/amostragem
t = arange(0,1,dt)
B = [0.049922035, -0.095993537, 
0.050612699, -0.004408786]
A = [1.0        , -2.494956002, 
2.017265875, -0.522189400]
w,h = freqz(B,A)
frequencias = w/pi*nyquist
nrosa = lfilter(B, A, nbranco)
Rbranco = correlate(nbranco,nbranco,mode='full')
Rrosa   = correlate(nrosa  , nrosa ,mode='full')
l = Rbranco.size
tR = linspace(-1.0,1.0,l)
Rbranconor = abs( Rbranco )/max( abs( Rbranco ) )
Rrosanor   = abs( Rrosa   )/max( abs( Rrosa   ) )
figure(1)
subplot(211)
plot(frequencias,abs(h),'k',linewidth=2)
xlabel(u'Frequência (Hz)')
ylabel(r'$H(f)$',fontsize=18)
xlim(0,0.1*nyquist)
grid(True)
subplot(212)
plot(t,nrosa,'k')
xlabel('Tempo (s)')
ylabel(r'$n(t)$',fontsize=18)
grid(True)
figure(2)
plot(tR,Rbranconor,'k'  ,linewidth=2,label='Branco')
plot(tR,Rrosanor  ,'k--',linewidth=2,label='Rosa'  )
xlabel('Tempo (s)')
title(r'$|R(\tau)|$',fontsize=18)
xlim(-0.1,0.1)
legend(loc='best')
grid(True)
show()
