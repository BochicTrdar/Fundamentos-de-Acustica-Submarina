# coding=utf-8
from numpy import * 
from scipy import * 
from scipy.special import *
from matplotlib.pyplot import *

def freflco(q=None,arho=None,vp=None,dp=None):

       a_p   = vp/( 1.0 + 1j*dp )
       apxap = a_p*a_p
       cosq  = cos( q )
       sinq  = sin( q )
       cqxcq = cosq*cosq
       sinqp = sqrt( 1.0 - apxap*cqxcq )
       zwp   = arho*a_p*sinq/sinqp
       Vww   = ( zwp - 1.0 )/( zwp + 1.0 )

       return Vww

def apl_bottom_bsigmav(qi=None,qs=None,phis=None,
       g3=None,w3=None,kw=None,arho=None,
       vp=None,dp=None):

       kappa = ( 1.0 + 1j*dp )/vp
       kappaxkappa = kappa*kappa

       cqs   = cos( qs   ); cqsxcqs = cqs*cqs
       cqi   = cos( qi   ); cqixcqi = cqi*cqi
       cphis = cos( phis )

       S = cqs*cqi*cphis

       pps = sqrt( kappaxkappa - cqsxcqs )
       ppi = sqrt( kappaxkappa - cqixcqi )

       Rs = freflco(qs,arho,vp,dp) + 1.0
       Ri = freflco(qi,arho,vp,dp) + 1.0
       RsxRs = abs( Rs )**2.0
       RixRi = abs( Ri )**2.0

       Repis = real( ppi + pps )
       Impis = imag( ppi + pps )
       A = 2.0*kw*arho*arho*Impis
       F = S - kappaxkappa - ppi*pps
       FxF = abs( F )**2.0
       dt = 0.5*sqrt( cqixcqi + cqsxcqs - 2.0*S ) 
       dk = kw*sqrt( 4.0*dt*dt + Repis*Repis )    
       Wpp = w3/( dk**g3 )                        
       sigmav0 = pi/2.0*( kw**4.0 )*FxF*Wpp       
       sigmav = sigmav0*RixRi*RsxRs/A             
       
       return sigmav

def apl_bottom_bsigma(qi=None,qs=None,phis=None,
       g2=None,w2=None,kw=None,arho=None,
       vp=None,dp=None):

       kappa = ( 1.0 + 1j*dp )/vp
       kappaxkappa = kappa*kappa

       alpha = g2/2.0 - 1.0
       opa   = 1.0 + alpha
       oma   = 1.0 - alpha
       omta  = 1.0 - alpha*2.0
       twoma = 2.0 - alpha
       twoa  = 2.0*alpha
       ooa   = 1.0/alpha
       oota  = 1.0/twoa
       
       G2ma = gamma( twoma )
       Gopa = gamma( opa   )
       
       cqs   = cos( qs   ); sqs = sin( qs )
       cqsxcqs = cqs*cqs
       cqi   = cos( qi   ); sqi = sin( qi )
       cqixcqi = cqi*cqi
       cphis = cos( phis )

       Pi = sqrt( kappaxkappa - cqixcqi )
       Ps = sqrt( kappaxkappa - cqsxcqs )
       
       S = cqs*cqi*cphis 

       d  = 1.0/sqrt(2.0)*sqrt( 1.0 + sqi*sqs - S )
       dz = 0.5*( sqi + sqs )
       dt = 0.5*sqrt( cqixcqi - 2.0*S + cqsxcqs )
       
       qis = math.asin( d )
 
       dK = 2.0*kw*( dt + 0.0001 )

       W2dK = w2/( dK**g2 )
        
       Ris = freflco(qis,arho,vp,dp)
       Ri  = freflco(qi ,arho,vp,dp) + 1.0
       Rs  = freflco(qs ,arho,vp,dp) + 1.0

       RxR   = abs( Ris )**2.0
       RixRi = abs( Ri  )**2.0       
       RsxRs = abs( Rs  )**2.0       
       
       A = RxR/( 8.0*pi )
       A1 = 8.0*alpha*alpha*gamma( oota + 0.5 )
       A2 = gamma( 0.5 )*gamma( ooa )*gamma( oota )
       a  = ( A1/A2 )**twoa                            
       b = ( a**( 0.5 + 1.0/twoa )*gamma( ooa ) )/twoa
       E = 2.0*pi*w2*G2ma*( 2.0**( -twoa ) )
       F = alpha*oma*Gopa
       ChxCh = E/F
       q0 = ChxCh*( 2.0**( omta ) )*( kw**( 2.0*oma ) ) 
       C  = ( dt**( 4.0*alpha ) + \
          a*q0*q0*( dz**4.0 ) )**( opa/twoa )
       B = b*q0*( 1.0 + 100.0*dt**4.0 )/C
       G = ( 1.0/arho - 1.0 )*\
       ( S - Pi*Ps/arho ) + 1.0 -kappaxkappa/arho
       GxG = abs( G )**2.0

       sigmakr = A*( d**4.0 )*B                        
       sigmapr = 0.25*( kw**4.0 )*RixRi*RsxRs*GxG*W2dK
     
       return sigmakr,sigmapr

freqkHz = 10.0
freq    = freqkHz*1000
cw      = 1500.0
kw      = 2.0*pi*freq/cw

# Fundo arenoso: 

arho    = 1.940
vp      = 1.113
dp      = 0.0115

g2      = 3.25
w2      = 0.000141
g3      = 3.0
w3      = 0.0004

eta = -2.0

thetai = 45; qi = thetai*pi/180

nthetas = 90
theta = linspace(1.0,90.0,nthetas)

nphis = 361
phis  = linspace(-180,180,nphis)

Sb = zeros((nphis,nthetas))
sigma = zeros((nphis,nthetas))

for j in range(nphis):
    phi = phis[j]*pi/180.0
    for i in range(nthetas):
        q = theta[i]*pi/180.0
        sigmav          = apl_bottom_bsigmav(qi,q,phi,
                          g3,w3,kw,arho,vp,dp) 
        sigmakr,sigmapr = apl_bottom_bsigma( qi,q,phi,
                          g2,w2,kw,arho,vp,dp)
        sigmar = ( sigmakr**eta + \
                   sigmapr**eta )**( 1.0/eta )
        sigma[j,i]  = sigmav + sigmar
        Sb[j,i]  = 10*log10( sigmav + sigmar )

[R,Bearings] = meshgrid(theta,phis)

X = R*cos( Bearings*pi/180.0 )
Y = R*sin( Bearings*pi/180.0 )

figure(1)
pcolor(X,Y,Sb,cmap='Greys_r',vmin=-30,vmax=-10)
colorbar()
axis('off')

thetan = arange(15,90,15)
n = thetan.size
for i in range(n):
    s = str( thetan[i] )+r'$^\circ$'
    text(thetan[i],0,s,color='black')
n = 18
for i in range(9):
    s = str( i*20 )+r'$^\circ$'
    text(100*cos(i*2*pi/n),100*sin(i*2*pi/n),s,
    horizontalalignment='center',
    verticalalignment='center')

text(-100,0,r'$\pm$180$^\circ$',
horizontalalignment='center',
verticalalignment='center')

for i in range(9):
    s = str( -i*20 )+r'$^\circ$'
    text(100*cos(i*2*pi/n),100*sin(-i*2*pi/n),s,
    horizontalalignment='center',
    verticalalignment='center')

show()

