# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

nthetas = 360
thetas = linspace(0,2*pi,nthetas)

N = 4
dol = 8.0/3.0
a1 = N*pi*dol*sin( thetas )
a2 =   pi*dol*sin( thetas )
s1 =  sin( a1 ); s1[0] = 1.0
s2 = N*sin(a2 ); s2[0] = 1.0
b = ( s1/s2 )**2

figure(1)
polar(thetas+pi/2,b,'k',linewidth=2)
polar(-pi,0.5,'ko')
polar(-pi,1.0/6.0,'ko')
polar(  0,1.0/6.0,'ko')
polar(  0,0.5,'ko')
grid(True)

show()
