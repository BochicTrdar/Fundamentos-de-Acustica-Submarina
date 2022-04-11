# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

# Médias e variâncias do ruído e do sinal
mun    = 0.0
sigman = 0.6
mus    = 1.0
sigmas = 0.5
xt = 0.2

n = 1000

x = linspace(-2,2,n)
y = (x-mun)/sigman
pdfn = 1/( sqrt(2*pi)*sigman )*exp( -0.5*y*y )
y = (x-mus)/sigmas
pdfs = 1/( sqrt(2*pi)*sigmas )*exp( -0.5*y*y )
yaux = zeros(n)

figure(1)
subplot(211),plot(x,pdfn,'k',linewidth=2)
fill_between(x,pdfn,yaux,where=x>xt,
facecolor='0.9')
text(0.3, 0.2, r'$p(FA)$', fontsize=22)
title(u'PDF do ruído',fontsize=18)
ylim(0,1)
grid(True)
subplot(212),plot(x,pdfs,'k',linewidth=2)
fill_between(x,pdfs,yaux,where=x>xt,
facecolor='0.8')
text(1.0, 0.2, r'$p(D)$', fontsize=22)
title(u'PDF do sinal',fontsize=18)
ylim(0,1)
grid(True)
xlabel('Amplitude do sinal',fontsize=18)

show()
