# coding=utf-8
from numpy import * 
from scipy import *
from scipy.signal import butter, lfilter
from matplotlib.pyplot import *

a = -1.0
b =  1.0
amostragem = 1000
nyquist    = amostragem/2 
n = random.uniform(a,b,amostragem) # ruído branco
dt = 1.0/amostragem
t = arange(0,1,dt)
freq = 50
f1   = 20.0 
f2   = 80.0 
w = 2*pi*freq
s = cos( w*t ) + n # sinal e ruído
low  = f1/nyquist
high = f2/nyquist
# H = B/A:
B, A = butter(4, [low, high], btype='band')
sf = lfilter(B, A, s)

figure(1)
subplot(211),plot(t,s,'k')
ylabel(r'$s(t)$',fontsize=18)
grid(True)
subplot(212),plot(t,sf,'k',linewidth=2)
ylabel(r'$s_f(t)$',fontsize=18)
xlabel('Tempo (s)',fontsize=18)
grid(True)
show()
