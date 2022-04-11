# coding=utf-8
from numpy import * 
from numpy.linalg import *
from scipy import * 
from scipy.interpolate import interp1d
from matplotlib.pyplot import *

def modos( z=None, c=None, f=None, 
           tbc=None, bbc=None):

    themodes    = []
    wavenumbers = []

    h = abs( z[1] - z[0] )
    hh = h*h

    alpha1 = tbc[0]  
    beta1  = tbc[1] 
    alpha2 = bbc[0]  
    beta2  = bbc[1]

    w = 2*pi*f 
    k = w/c
    kk = k*k  

    lengthz = z.size  
    lengthA = lengthz - 2
    y  = zeros( (lengthz,lengthz) )  
    A  = zeros( (lengthA,lengthA) )   
    Au = zeros( (lengthA,lengthA) )
    Al = zeros( (lengthA,lengthA) )

    ncdiag =  1.0/hh * ones( lengthA-1 )  
    cdiag  = -2.0/hh * ones( lengthA   ) + kk[1:-1]

    fill_diagonal( A, cdiag  )

    for i in range(lengthA-1):
        Au[i,i+1] = ncdiag[i]
        Al[i+1,i] = ncdiag[i]

    A = A + Au + Al
    A[ 0, 0] =  1/hh * ( hh*kk[ 1] + \
    ( -beta1/h )/( alpha1 - beta1/h ) - 2 )  
    A[-1,-1] =  1/hh * ( hh*kk[-2] + \
    (  beta2/h )/( alpha2 + beta2/h ) - 2 )  

    rankA = linalg.matrix_rank( A )  

    if rankA < lengthA:
       print( u'Não há solução numérica \
                para estas CFs...' )
       return themodes, wavenumbers

    eigenvalues,modese = linalg.eig( A )  

    modes_at_top    = modese[ 0,:]*( -beta1/h )/\
                      ( alpha1 - beta1/h )   
    modes_at_bottom = modese[-1,:]*(  beta2/h )/\
                      ( alpha2 + beta2/h )    
    modes = zeros((lengthz,lengthA))
    modes[ 0,:] = modes_at_top
    modes[-1,:] = modes_at_bottom
    modes[1:-1,:] = modese  

    indexes =  argsort( eigenvalues ) 

    eigenvalues = eigenvalues[ indexes ]
    eigenvalues = eigenvalues[::-1]
    modes       = modes[:,indexes]
    modes       = modes[:,::-1]

    poseigen = eigenvalues[eigenvalues > 0]
    wavenumbers = sqrt( poseigen )
    themodes = modes[:,0:poseigen.size]
    
    for i in range(poseigen.size):
        phi = themodes[:,i]
        if phi[1] < 0:
           phi = -phi
        themodes[:,i] = phi/linalg.norm(phi)
              
    return themodes, wavenumbers

def pmodos(z=None,Z=None,k=None,
           zs=None,zh=None,rh=None,M=None):

    p = []   
    nr = rh.size
    nz = zh.size

    p  = zeros((nz,nr)) + 1j*zeros((nz,nr))
    pm = zeros((nz,nr)) + 1j*zeros((nz,nr))

    e0 = 1j*exp( -1j*pi/4.0 )/sqrt( 8*pi )
   
    dz = abs( z[1] -z[0] )

    for i in range(M):
        Zm = Z[:,i]
        interpolator = interp1d(z, Zm)
        Zms = interpolator( zs )
        Zmh = interpolator( zh )        
        Zsh = Zms*Zmh
        Rm  = exp( 1j*k[i]*rh )/sqrt( k[i]*rh )
        [RM,ZM] = meshgrid(Rm,Zsh)
        pm  = RM*ZM
        p = p + pm

    p = e0*p
    p = squeeze( p )

    return p

def munk(z,z0,c0):

   B = 1.3e3
   e = 7.37e-3
   eta = 2*( z - z0 )/B
   c   = c0*( 1 + e*( eta + exp( -eta ) - 1 ) )

   return c

D = 5000
nz = 101
z = linspace(0,D,nz)
dz = abs( z[1] - z[0] )
rmaxkm = 100
rmax = rmaxkm*1000
nr = 101
r = linspace(0,rmax,nr) 
r[0] = 1.0 
rkm = r/1000.0
freq = 50
z0 = 1500.0
c0 = 1480.0
c = munk(z,z0,c0)
p0 = 1.0/( 4*pi )
Z,kh = modos( z, c, freq, [1,0], [1,0])

m = kh.size

for i in range(m):
    Zi = Z[:,i]
    Im = sqrt( dz*sum( Zi*Zi ) )
    Z[:,i] = Zi/Im

p = pmodos(z,Z,kh,z0,z,r,m)
p = p/p0
tl = -20*log10( abs( p ) )

figure(1)
imshow(tl, cmap='Greys_r',
extent=[rkm[0],rkm[-1],z[-1],z[0]],
aspect='auto',origin='upper',vmin=60,vmax=120)
colorbar()
xlabel(u'Distância (km)',fontsize=18)
ylabel('Profundidade (m)',fontsize=18)

show()

