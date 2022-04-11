# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

amostragem = 1000
dt = 1.0/amostragem
t = arange(0,1,dt)

s = zeros(amostragem)
s[100:199] =  1 
s[200:299] = -1
h = exp( -((t-0.2)/0.02)**2 ) + \
0.75*exp( -((t-0.36)/0.02)**2 )

S = fft( s )
H = fft( h )
P = H*S
p = real( ifft(P) )
p = p/max( abs( p ) )

figure(1)
subplot(311)
plot(t,s,'k',linewidth=2)
title(r'$s(t)$',fontsize=18)
ylim(-1.1,1.1)
grid(True)
subplot(312)
plot(t,h,'k',linewidth=2)
title(r'$h(t)$',fontsize=18)
ylim(0,1.1)
grid(True)
subplot(313)
plot(t,p,'k',linewidth=2)
title(r'$p(t)$',fontsize=18)
ylim(-1.1,1.1), 
grid(True)
xlabel('Tempo (s)',fontsize=18)

show()
