# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

SNRdB = 10
SNR   = 10**( SNRdB/10.0 )

otitulo = '$s(t) + n(t)$, SNR = '
otitulo = otitulo + str(SNRdB) + ' dB'
freq       =    8 # Frequência do sinal
amostragem = 1000 # Frequência de amostragem
nyquist    = amostragem/2 # Frequência de Nyquist
frequencias = linspace(0,amostragem,amostragem)
dt = 1.0/amostragem
t = arange(0,1,dt)
w = 2*pi*freq
s = cos( w*t ) # Tom

Ps = s.var( )

sigma = sqrt( Ps/SNR )
# Contaminação do sinal:
r = s + random.normal(0,sigma,amostragem)

figure(1)
subplot(211)
plot(t,s,'k',linewidth=2)
ylim(-1.5,1.5)
grid(True)
title(r'$s(t)$',fontsize=18)
subplot(212)
plot(t,r,'k')
#ylim(-1.5,1.5)
grid(True)
title(otitulo,fontsize=18)
xlabel('Tempo (s)',fontsize=18)

show()
