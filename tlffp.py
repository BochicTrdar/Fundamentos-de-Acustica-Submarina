# coding=utf-8
from numpy import * 
from numpy.linalg import *
from scipy import * 
from matplotlib.pyplot import *

def ffpA( z=None, c=None, freq=None, k=None):

    A = []

    h = abs( z[1] - z[0] )
    hh = h*h
  
    w = 2*pi*freq
    ww = w*w
    cc = c*c
    lengthA = z.size  
    A  = zeros( (lengthA,lengthA) )

    cdiag  = -2.0/hh + ww/cc

    fill_diagonal( A,  cdiag  )

    for i in range(lengthA-1):
        A[i,i+1] = 1.0/hh
        A[i+1,i] = 1.0/hh

    A = A - k*k*eye( lengthA )

    return A

def munk(z,z0,c0):

   B = 1.3e3
   e = 7.37e-3
   eta = 2*( z - z0 )/B
   c   = c0*( 1 + e*( eta + exp( -eta ) - 1 ) )

   return c

D = 5000
nz = 500
z = linspace(0,D,nz); dz = z[1] - z[0]
freq = 50; w = 2*pi*freq
z0 = 1500.0
zs = z0
c0 = 1480.0
c = munk(z,z0,c0)
k = w/c
kmin = min( k )
kmax = max( k )
nk = 501
k = linspace(kmin,kmax,nk)
dk = k[1] - k[0]
k = k - 1j*dk
nr     = 501
rmaxkm = 100
rmax = rmaxkm*1000
dr = rmax/nr
r = linspace(dr,rmax,nr); rkm = r/1000.0
p = zeros((nz,nk)) + 1j*zeros((nz,nk))
d = zeros( nz )
index = int( zs/dz )
d[ index ] = 1.0 # Dirac numérico

G = zeros((nz,nk)) + 1j*zeros((nz,nk))

for i in range(nk):
    A = ffpA( z, c, freq, k[i])
    G[:,i] = linalg.solve(A,d)

for i in range(nr):
     kr = k*r[i]
     for j in range(nz):
         I = G[j,:]*sqrt( k )*exp( 1j*kr )
         p[j,i] = dk*sum( I )/r[i]

p = 4*pi*p*exp( 1j*pi/4 )/sqrt( 2*pi )

tl = -20*log10( abs( p ) )

figure(1)
imshow(tl, cmap='Greys_r',
extent=[rkm[0],rkm[-1],z[-1],z[0]],
aspect='auto',origin='upper',vmin=60,vmax=120)
colorbar() 
xlabel(u'Distância (km)',fontsize=18)
ylabel('Profundidade (m)',fontsize=18)

show()

