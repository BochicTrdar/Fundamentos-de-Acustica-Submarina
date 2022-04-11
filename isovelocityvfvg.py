# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

M = 5
m = range(M)
n = 101
fmin = 100.0
fmax = 200.0
freqs = linspace(fmin,fmax,n)
w = 2*pi*freqs
wxw = w*w
c = 1500.0; cxc = c*c
D = 100.0

khm = zeros(n)

figure(1)
for i in range(M):
    km = ( m[i] + 0.5 )*pi/D
    kmxkm = km*km
    khm = sqrt( wxw/cxc - kmxkm )
    vf = w/khm
    vg = cxc*khm/w
    them = str( i+1 )
    text(freqs[21],vf[21]+1.0,them,fontsize=16)
    text(freqs[21],vg[21]-7.0,them,fontsize=16)
    plot(freqs,vf,'k',linewidth=2)
    plot(freqs,vg,'k--',linewidth=2)

xlabel(u'Frequência (Hz)',fontsize=18)
ylabel('Velocidade (m/s)',fontsize=18)
grid(True)

show()

