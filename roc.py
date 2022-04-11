# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

# Médias e variâncias do ruí­do e do sinal
mun    = 0.0
sigman = 0.5
mus    = 1.0
sigmas = 0.5

n = 1000

# Índice de detecção:
a = mus - mun
b = sigmas**2 + sigman**2
d = a**2/( 0.5*b )
print(d)

x = linspace(-2,2,n)
y = (x-mun)/sigman
pdfn = 1/( sqrt(2*pi)*sigman )*exp( -0.5*y*y )
y = (x-mus)/sigmas
pdfs = 1/( sqrt(2*pi)*sigmas )*exp( -0.5*y*y )

dx = x[1]-x[0]
pFA = zeros( n )
pD  = zeros( n )

for i in range(n):
    pFA[i] = sum( pdfn[i:n] )
    pD[ i] = sum( pdfs[i:n] )

pFA = dx*pFA 
pD  = dx*pD

figure(1)
plot(pFA,pD,'k',linewidth=2)
title(u'ROC do sistema de detecção',fontsize=18)
xlabel(r'$p(FA)$',fontsize=18)
ylabel(r'$p(D)$',fontsize=18)
xlim(0,1)
ylim(0,1)
grid(True)

show()
