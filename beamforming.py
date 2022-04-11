# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

ntheta = 181
theta = linspace(-90,90,ntheta)
thetar = theta*pi/180
nphi = 361
phi = linspace(-180,180,nphi)
phir = phi*pi/180

thetas  = 40 
thetasr = thetas*pi/180;
phis    = 20
phisr   = phis*pi/180;

nsensors = 11
c    = 1500
freq =  500; w0 = 2*pi*freq
d = array([0, 0, 1]) # Antena vertical

yp = zeros(nsensors) + 1j
ep = zeros(nsensors) + 1j
B  = zeros((ntheta,nphi))

kx = cos(phisr)*cos(thetasr) 
ky = sin(phisr)*cos(thetasr) 
kz =            sin(thetasr)
ks = w0/c*array([kx,ky,kz])

for l in range(nsensors):
    rl = l*d
    yp[l] = exp( -1j*dot(ks,rl) )

yp = yp/linalg.norm( yp )

for j in range(nphi):

    phij = phir[j]

    for i in range(ntheta):

         thetai = thetar[i]
         kx = cos(phij)*cos(thetai) 
         ky = sin(phij)*cos(thetai) 
         kz =           sin(thetai)
         k  = w0/c*array([kx,ky,kz])

 	 for l in range(nsensors):

 	     rl = l*d
 	     ep[l] = exp( 1j*dot(k,rl) )
	
	 ep = ep/linalg.norm( ep )
	
	 B[i,j] = abs( dot(yp,ep) )

figure(1)
pcolor(phi,theta,B,cmap='Greys')
colorbar()
xlim(-180,180)
ylim(-90,90)
xlabel(r'$\phi$ (graus)',fontsize=18)
ylabel(r'$\theta$ (graus)'  ,fontsize=18)

show()
