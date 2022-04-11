# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

freq       =   8 # Frequência do sinal
amostragem = 500 # Frequência de amostragem
nyquist    = amostragem/2 # Frequência de Nyquist
dt = 1.0/amostragem 
t = arange(0,1,dt)
w = 2*pi*freq
s = cos( w*t ) # Tom

# Estimar o SNR com um conjunto 
# de sinais contaminados:

nsinais = 101
r = zeros((nsinais,amostragem))
for i in range(nsinais):
   r[i,:] = s + random.randn( t.size )

se = mean( r, axis=0 ) # Sinal estimado
ne = r[-1,] - se       # Ruído estimado
Ps = se.var()
Pn = ne.var()
SNR   = abs( Ps/Pn ) 
SNRdB = 10*log10( SNR )
osnr = "SNR estimado = " + str(SNRdB) + " dB"
print( osnr )
