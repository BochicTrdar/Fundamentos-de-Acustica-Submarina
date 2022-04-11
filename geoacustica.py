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

freq   = 50.0; w = 2*pi*freq
# Valores procurados:
cb     = 1900.0; rhob = 2.0
# Guia de onda:
D      =  100.0
c1     = 1500.0; rho1 = 1.0
# Parâmetros do Bartlett:
nc     = 101
cmin = 1800.0
cmax = 2000.0
c2     = linspace(cmin,cmax,nc)
nrho = 101
rhomin = 1.5
rhomax = 2.5
rho2   = linspace(rhomin,rhomax,nrho)
# Guia de onda:
zs     = 50.0
rh     = array([5000.0])
B      = zeros((nrho,nc))
nzh    = 51 
zh     = linspace(25,75,nzh)
z      = linspace(0,D,101); dz = abs( z[1]-z[0] )

# Observação:
# Pekeris: números de onda
kh     = kpekeris(c1,rho1,cb,rhob,D,freq)
M      = kh.size
Z      = zeros((101,M))
kz     = sqrt( (w/c1)**2 - kh*kh )
# Modos
for j in range(M):
    Zj = sin( kz[j]*z )
    N = sqrt( dz*sum( Zj*Zj ) )
    Z[:,j] = Zj/N
# Campo dos modos
d = pmodes(z,Z,kh,zs,zh,rh,M)
n = linalg.norm(d)
dn = d/n

# Cálculo de réplicas e ajustamento do campo
for j in range(nc):
    ci = c2[j]
    for j2 in range(nrho):
        rhoi = rho2[j2]
        kh = kpekeris(c1,rho1,ci,rhoi,D,freq)
        M = kh.size
        Z = zeros((101,M))
        kz = sqrt( (w/c1)**2 - kh*kh )
        for jj in range(M):
            Zj = sin( kz[jj]*z )
            N = sqrt( dz*sum( Zj*Zj ) )
            Z[:,jj] = Zj/N
        eij = pmodes(z,Z,kh,zs,zh,rh,M)
        n = linalg.norm( eij )
        en = eij/n
        prod = inner( en , conj(dn) )
        B[j2,j] = abs( prod*conj(prod) )

figure(1)
imshow(B, cmap='Greys',
extent=[c2[0],c2[-1],rho2[0],rho2[-1]],
aspect='auto',origin='lower')
colorbar()
xlabel(u'Velocidade do som (m/s)',fontsize=18)
ylabel(r'Densidade (g/cm$^3$)',fontsize=18)
show()

