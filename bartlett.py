# coding=utf-8
from numpy import * 
from scipy import * 
from scipy.interpolate import interp1d
from matplotlib.pyplot import *

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

zs =  50.0
rs = array([1000.0])

nr   = 201
rmin =  500.0
rmax = 1500.0
rb = linspace(rmin,rmax,nr); rkm = rb/1000.0
nz   = 101
D    = 100.0
z    = linspace(0.0,D,nz)
nzb = 81
zb = linspace(10,90,nzb)
c = 1500.0
freq = 50.0; w = 2*pi*freq
k = w/c; kxk = k*k
M = int( w*D/(pi*c) - 0.5 )
nh = 51
zh = linspace(25,75,nh)
km = ( arange(0,M) + 0.5 )*pi/D
kmsq = km*km
kh = sqrt( kxk - kmsq )

Z = zeros((nz,M))

for i in range(M):
    Zs = sin( km[i]*zs )
    Z[:,i]  = sin( km[i]*z )

Z = 2.0/D*Z

d = pmodos(z,Z,kh,zs,zh,rs,M)
n = linalg.norm( d )
dn = conj( d/n )

B = zeros((nzb,nr))

for j in range(nzb):
    zj = zb[j]
    e = pmodos(z,Z,kh,zj,zh,rb,M)
    for i in range(nr):
        ei = e[:,i]
        n = linalg.norm(ei)
        en = ei/n
        prod = inner( en, dn )
        B[j,i] = abs( prod*conj( prod ) )

figure(1)
imshow(B, cmap='Greys',
extent=[rkm[0],rkm[-1],zb[-1],zb[0]],
aspect='auto',origin='lower')
colorbar()
xlabel(u'Distância (km)',fontsize=18)
ylabel('Profundidade (m)',fontsize=18)

show()
