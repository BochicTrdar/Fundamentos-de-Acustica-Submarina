# coding=utf-8
from numpy import * 
from scipy import * 
from scipy.interpolate import interp1d
from matplotlib.pyplot import *

def kpekeris(c1=None,rho1=None,
             c2=None,rho2=None,
             D=None,freq=None):
    
    kp = []

    w = 2*pi*freq
    k1 = w/c1
    k2 = w/c2

    nk = 1001
    k = linspace(k1,k2,nk)
    kxk = k*k

    r1 = sqrt( k1*k1 - kxk ) 
    r2 = sqrt( kxk - k2*k2 )
    s1 = sin( r1*D )
    c1 = cos( r1*D )

    f = s1*r2/rho2 + c1*r1/rho1

    for i in range(nk-1): 
   
        x1 = k[ i ]
        x2 = k[i+1]
        y1 = f[ i ]
        y2 = f[i+1]
        p = y1*y2
        x3  = (x1*y2-x2*y1)/(y2-y1)
     
        if p < 0:

           kp = append(kp,x3)

    return kp

def pmodes(z=None,Z=None,k=None,
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

nfreqs = 11
fmin   = 21.5
fmax   = 26.0 
freqs  = linspace(fmin,fmax,nfreqs)
D      =  100.0
c1     = 1500.0; rho1 = 1.0
c2     = 1800.0; rho2 = 1.8
rmax   = 3000.0
rh     = linspace(0,rmax,101)
rh[0]  = 1.0
rhkm   = rh/1000.0
z      = linspace(0,D,101); dz = abs( z[1] - z[0] )
zs     = 36.0
zh     = array([36.0])
p0     = 1/( 4*pi )

for i in range(nfreqs):
    wi = 2*pi*freqs[i]
    kh = kpekeris(c1,rho1,c2,rho2,D,freqs[i])
    M = kh.size
    Z = zeros((101,M))
    kz = sqrt( (wi/c1)**2 - kh*kh )
    for j in range(M):
        Zj = sin( kz[j]*z )
        N = sqrt( dz*sum( Zj*Zj ) )
        Z[:,j] = Zj/N

    p = pmodes(z,Z,kh,zs,zh,rh,M)
    p = p/p0
    tl = -20*log10( abs( p ) ) + i*2.0
    figure(1)
    plot(rhkm,tl,'k',linewidth=2)

xlabel(u'Distância (km)',fontsize=18)
ylabel('TL (dB)',fontsize=18)
ylim(80,20)
grid(True)

show()

