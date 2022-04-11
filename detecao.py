# coding=utf-8
from numpy import * 
from matplotlib.pyplot import *

mu    = 0.0
sigma = 1.0
amostragem = 1000 
n = sigma*random.randn(amostragem) + mu
x = linspace(-10,10,amostragem)
t = x + 10 
s = 1.5*exp( -x*x )
spn = s + 0.5*n

figure(1)
subplot(211),plot(t,s,'k',linewidth=2)
ylabel('Amplitude',fontsize=18)
title('Sinal a detectar',fontsize=18)
ylim(-1,2)
grid(True)
subplot(212),plot(t,spn,'k')
xlabel('Tempo (s)',fontsize=18)
ylabel('Amplitude',fontsize=18)
title('Sinal detectado',fontsize=18)
ylim(-2,2)
grid(True)
show()
