# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

nthetas = 360
thetas = linspace(0,2*pi,nthetas)
dol = 2.0

c = cos( pi*dol*sin(thetas) )
b = c*c

figure(1)
polar(thetas+pi/2,b,'k',linewidth=2)
plot(pi,0.5,'ko')
plot(0,0.5,'ko')
grid(True)

show()
