# coding=utf-8
from numpy import * 
from scipy import * 
from scipy import signal
from matplotlib.pyplot import *

amostragem = 2048
h = zeros( amostragem )
nyquist = int( amostragem/2 )
freqs = arange(0,amostragem,1)
dt = 1.0/amostragem
t = arange(0,1,dt)
D = 100.0
Rkm = 20.0
R = Rkm*1000.0
c  = 1500.0
cxc = c*c
# Atraso temporal para não começar em t = 0:
t0 = R/c
t0 = ( int( t0/dt ) - 50 )*dt
for m in range(1,6):
    H  = ones(amostragem) + 1j*zeros(amostragem)
    w  = 2*pi*freqs
    # Frequência de corte:
    f0m = (m - 0.5)*c/(2*D)
    w0m = 2*pi*f0m
    # Quadrado do número de onda:
    kxk = ( w**2 - w0m**2 )/cxc
    # Procurar modos evanescentes:
    indexes = argwhere( kxk < 0 )
    L = indexes.size
    # Eliminar modos evanescentes: 
    kxk[ indexes ] = 0.0
    w[   indexes ] = 0.0
    k = sqrt( kxk )
    H[ indexes ] = 0.0
    H[ amostragem-indexes-1 ] = 0.0
    # Resposta impulsiva:
    fase = R*k - w*t0
    H = H*exp( -1j*fase )
    h = h + real( ifft( H ) )
fe, te, Shh = signal.spectrogram(h, 
amostragem, nfft=128, nperseg=128, noverlap=100)
figure(1)
plot(t,h)
xlabel('Tempo (s)',fontsize=18)
title(r'Resposta Impulsiva do canal $h(t)$',
fontsize=18)
grid(True)
figure(2)
imshow(log10(abs(Shh)), cmap='Greys', 
extent=[te[0],te[-1],fe[0],fe[-1]],
aspect='auto',origin='lower')
xlabel('Tempo (s)',fontsize=18)
ylabel(u'Frequência (Hz)',fontsize=18)
colorbar()
show()
