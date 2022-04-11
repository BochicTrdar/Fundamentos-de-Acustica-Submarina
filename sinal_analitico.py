# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

amostragem = 1000
nyquist = amostragem/2
dt = 1.0/amostragem
t = arange(0,1,dt)
x = 4*( t - 0.5 )
freq = 10
w = 2*pi*freq
s = exp( -x*x )*cos( w*t )
sinal_analitico = signal.hilbert(s)
envelope = abs(sinal_analitico)
fase     = angle(sinal_analitico)
wi = diff( unwrap(fase) )/diff( t )
fi = wi/( 2*pi )

figure(1)
subplot(211)
plot(t,s,'k',linewidth=2)
plot(t,envelope,'k--',linewidth=2)
ylim(-1.1,1.1)
grid(True)
subplot(212)
plot(t[0:-1],fi,'k',linewidth=2)
xlabel(r'$t$ (s)',fontsize=18)
ylabel(r'$f$ (Hz)',fontsize=18)
ylim(5,11)
grid(True)

show()
