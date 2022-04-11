# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

def bdryr(rho1=None,rho2=None,
          cp1=None,cp2=None,
          cs2=None,alphap=None,
          alphas=None,theta=None):
       
       e = exp(1)
       
       tilap = alphap/( 40.0*pi*log10( e ) )
       tilas = alphas/( 40.0*pi*log10( e ) )

       tilcp2 = cp2*(1.0-1j*tilap)/\
                    (1.0+tilap*tilap)
       tilcs2 = cs2*(1.0-1j*tilas)/\
                    (1.0+tilas*tilas)
 
       a1 = rho2/rho1
       a2 = tilcp2/cp1
       a3 = tilcs2/cp1
       a4 = a3*sin( theta )
       a5 = 2.0*a4*a4
       a6 = a2*sin( theta )
       a7 = 2.0*a5-a5*a5
       
       d = a1*( a2*(1.0-a7)/\
           sqrt(1.0-a6*a6)+a3*a7/sqrt(1.0-0.5*a5) )
       
       R = (d*cos(theta)-1.0)/(d*cos(theta)+1.0)

       return R

# Ângulo de incidência:
theta = linspace(50,70,181)
thetar = theta*pi/180
dtheta = diff( thetar )

f = 150.0
w = 2*pi*f

# Fundo rígido
cw = 1500.0
cp = 1800.0
cs = 0.0
alphap = 0.0
alphas = 0.0
rhow = 1000.0
rhob = 1800.0
k = w/cw
kh = k*sin( thetar )

R = bdryr(rhow,rhob,
cw,cp,cs,alphap,alphas,thetar)

rR = real( R )
iR = imag( R ) 
phi = arctan2( iR, rR )
dphi = diff( phi )
dk = diff( kh )
displacement = -dphi/dk

figure(1)
plot(theta[0:-1],displacement,'k',linewidth=2)
xlabel(r'$\theta$',fontsize=18)
ylabel(r'$\Delta$',fontsize=18)
grid(True)

show()
