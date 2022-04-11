# coding=utf-8
from numpy import * 
from scipy import *
from matplotlib.pyplot import *

cw   = 1500.0
freq = 150.0
Tx   = 25.0
Rx   = 200.0
rmin =    0.0 
rmax = 2000.0
nr = 501
r = linspace(rmin,rmax,nr)
r[0] = 1.0
rkm = r/1000
l = cw/freq
k = 2*pi/l
R1 = sqrt( r*r + ( Tx - Rx )*( Tx - Rx ) )
R2 = sqrt( r*r + ( Tx + Rx )*( Tx + Rx ) )

p = exp( 1j*k*R1 )/R1 - exp( 1j*k*R2 )/R2

TL  = -20*log10( abs( p ) ) # TL dos raios
TLg =  20*log10( r ) # TL decaimento geométrico

figure(1)
plot(rkm,TL ,'k'  ,linewidth=2,
label='Exacto')
plot(rkm,TLg,'k--',linewidth=2,
label=u'Decaimento geométrico')
xlabel(u'Distância (km)',fontsize=18)
ylabel('TL (dB)',fontsize=18)
ylim(90,40)
legend(loc=1)
grid(True)

show()

