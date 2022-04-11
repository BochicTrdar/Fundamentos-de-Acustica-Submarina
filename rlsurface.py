# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

def apl_bub_sigma(q=None,freq=None,U=None):
    
       fkHz = freq/1000.0
       f2 = ( fkHz/25.0 )**0.85
       if U < 11:
          f1 = -5.2577 + 0.4701*U
          bv = f2*( 10.0**f1 )
       else:
          f1 = -5.2577 + 0.4701*11
          bv11 = f2*( 10.0**f1 )
          f3 = (U/11.0)**3.5
          bv = bv11*f3
       b = bv/sin( q )
       dr = 0.0136
       p1 = bv*dr
       d = 2.55e-2*( fkHz**(1.0/3.0) )
       p2 = 4.0*pi*d
       r1 = 1.0 + 8.0*b*exp( -2.0*b ) - exp( -4.0*b )
       r2 = 2.0*b
       r = r1/r2
       s = p1/p2*r

       return s

def apl_surface_sigma(q=None,freq=None,
                      U=None,qf=None):

       fkHz = freq/1000.0
       A = 1.3e-5*U
       sxs = 0.034
       if ( U >= 1.0 ):
          sxs = 4.6e-3*log( 2.1*U*U )
       p2 = 4.0*pi*sxs
       if ( q*180.0/pi <= 85.0 ):
          ssc = A*( (tan(q))**4.0 )
       else:
          ssc = 0.0
       if (U >= 6 ):
          SBL = 1.26e-3/sin(q)*( U**1.57 )*\
                ( fkHz**0.85 )
       else:
          SBL = 1.26e-3/sin(q)*( 6**1.57 )*\
                ( fkHz**0.85 )*exp( U - 6.0 )
       g = 0.5*pi - q
       secg = 1.0/cos( g )
       p1 = secg**4.0
       x = tan(g)**2.0/sxs
       sf = p1/p2*exp( -x )
       x = 0.524*( qf - q )*180.0/pi 
       f = 1.0/( 1.0 + exp(x) )      
       sri = f*sf + ( 1.0 - f )*ssc  
       sr = sri*10**( -SBL/10.0 )    
       return sr

freqkHz = 25 
freq = freqkHz*1000

nthetas = 180
thetas  = linspace(1,90,nthetas)
q  = thetas*pi/180.0
qi = 0.5*pi - q
secg = 1.0/cos( qi )
p1 = secg**4.0

U = arange(3.0,11.0) # Vento
U = append(U,15.0) 
sU = size( U )

qf    = zeros(sU)
sigma = zeros( (sU,nthetas) )

for i in range(sU):
    sxs = 0.034
    Ui = U[i]
    if ( Ui >= 1.0 ):
       sxs = 4.6e-3*log( 2.1*Ui*Ui )
    p2 = 4.0*pi*sxs
    sf90 = 1.0/p2
    x = tan(qi)**2.0/sxs
    sf = p1/p2*exp( -x )
    threshold = sf90/( 10**1.5 )
    index = argmax( sf >= threshold )
    qf[i] = q[index]
    for j in range(nthetas):
        sb = apl_bub_sigma(q[j],freq,U[i])
        sr = apl_surface_sigma(q[j],freq,U[i],qf[i])
        sigma[i,j] = sr + sb

SS = 10*log10( sigma )

figure(1)
for i in range(sU):
    plot(thetas,SS[i,],'k',linewidth=2)
    if i < 5:
       text(thetas[45],SS[i,45]+1,str(int(U[i])))
    elif i == 5:
       text(thetas[90],SS[i,90]+1,str(int(U[i])))
    elif i == 6:
       text(thetas[90],SS[i,90]+4,str(int(U[i])))
    elif i == 7:
       text(thetas[18],SS[i,18]+3,str(int(U[i])))
    else:
       text(thetas[40],SS[i,40]+0.75,str(int(U[i])))

xlabel(u'Ângulo Rasante (graus)',fontsize=18)
ylabel(u'SS (dB)',fontsize=18)
ylim(-60,10)
grid(True)

show()
