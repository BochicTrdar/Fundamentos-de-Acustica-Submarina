# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

def francoisgarrison(freq=None,
    T=None,S=None,pH=None,z=None):
    
    c   = 1412.0 + 3.21*T + 1.19*S + 0.0167*z
    theta = 273.0 + T
    fxf = freq**2
    f1 = 2.8*sqrt(S/35.0)*10**(4.0-1245.0/theta)
    f2 = 8.17*10**(8.0-1990.0/theta)/ \
        ( 1.0 + 0.0018*(S-35.0) )
    A1 = 8.86/c*10**(0.78*pH-5)
    A2 = 21.44*S/c*( 1.0 + 0.025*T )
    if T <= 20:    
       A3 = 4.937e-4 - 2.59e-5*T + \
            9.11e-7*T**2 - 1.50e-8*T**3
    else:
       A3 = 3.964e-4 - 1.146e-5*T + \
            1.45e-7*T**2 - 6.5e-10*T**3
    P2 = 1 - 1.35e-4*z + 6.2e-9*z**2
    P3 = 1 - 3.83e-5*z + 4.9e-10*z**2

    a = A1*f1*fxf/( f1**2 + fxf ) + \
        A2*P2*f2*fxf/( f2**2 + fxf ) + \
        A3*P3*fxf
    
    return a

nfreqs = 101
fmin =     1
fmax =  1000
n = linspace(0,3,101)
freqs = 10**n # kHz!
S  = 35.0
T  = 20.0
pH =  8.0
Z  =  0.0
fxf = freqs**2

aT = 3.3e-3 + 0.11*fxf/( 1.0 + fxf ) + \
     44.0*fxf/( 4100.0 + fxf ) + \
     3.0e-4*fxf
aFG = francoisgarrison(freqs,T,S,pH,Z)

figure(1)
plot(freqs,aT ,'k'  ,linewidth=2,
label='Thorp')
plot(freqs,aFG,'k--',linewidth=2,
label='Francois-Garrison')
xlabel(u'Frequência (kHz)',fontsize=18)
ylabel(r'$\alpha$ (dB/km)',fontsize=18)
xlim(1,1000)
legend(loc=2)
grid(True)

show()

