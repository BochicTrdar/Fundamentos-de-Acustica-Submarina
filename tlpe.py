# coding=utf-8
from numpy import * 
from numpy.linalg import *
from scipy import * 
from matplotlib.pyplot import *

def peBC( z=None, n=None, k0=None, dr=None):

    B = []
    C = []

    h = abs( z[1] - z[0] )
    hh = h*h
  
    lengthA = z.size  
    A  = zeros( (lengthA,lengthA) )
    B  = zeros( (lengthA,lengthA) ) + \
      1j*zeros( (lengthA,lengthA) )
    C  = zeros( (lengthA,lengthA) ) + \
      1j*zeros( (lengthA,lengthA) )

    cdiag  = -2.0/hh + k0*k0*( n*n - 1 )

    fill_diagonal( A,  cdiag  )
    fill_diagonal( B, -cdiag*0.5 + 2*1j*k0/dr  )
    fill_diagonal( C,  cdiag*0.5 + 2*1j*k0/dr  )

    for i in range(lengthA-1):
        A[i,i+1] = 1.0/hh
        A[i+1,i] = 1.0/hh
        B[i,i+1] = 2*1j*k0/dr - 0.5/hh
        B[i+1,i] = 2*1j*k0/dr - 0.5/hh
        C[i,i+1] = 2*1j*k0/dr + 0.5/hh
        C[i+1,i] = 2*1j*k0/dr + 0.5/hh

    return B,C

def munk(z,z0,c0):

   B = 1.3e3
   e = 7.37e-3
   eta = 2*( z - z0 )/B
   c   = c0*( 1 + e*( eta + exp( -eta ) - 1 ) )

   return c

D = 5000
nz = 201
z = linspace(0,D,nz)
rmaxkm = 100; rmax = rmaxkm*1000
nr = 501
r = linspace(0,rmax,nr)
dr = r[1] - r[0] 
r[0] = 1.0
rkm = r/1000.0
freq = 50; w = 2*pi*freq
z0 = 1500.0
c0 = 1480.0
c = munk(z,z0,c0)
k0 = w/c0
n  = c0/c
p = zeros((nz,nr)) + 1j*zeros((nz,nr))
U = zeros((nz,nr)) + 1j*zeros((nz,nr))
ks = k0/15
U[:,0] = sqrt( ks )*exp( -0.5*ks*ks*( z - z0 )**2 )

B,C = peBC(z, n, k0, dr)

for i in range(nr-1):
    y = B.dot(U[:,i])
    U[:,i+1] = linalg.solve(C,y)

for i in range(nr):
    H0 = sqrt( 2/(pi*k0*r[i]) )*\
         exp( 1j*( k0*r[i] - pi/4  ) )
    p[:,i] = U[:,i]*H0

tl = -20*log10( abs( p ) )

figure(1)
imshow(tl, cmap='Greys_r',
extent=[rkm[0],rkm[-1],z[-1],z[0]],
aspect='auto',origin='upper',vmin=60,vmax=120)
colorbar() 
xlabel(u'Distância (km)',fontsize=18)
ylabel('Profundidade (m)',fontsize=18)

show()

