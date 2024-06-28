function [sigmakr,sigmapr] = apl_bottom_bsigma(qi,qs,phis,g2,w2,kw,arho,vp,dp)

kappa = ( 1.0 + 1i*dp )/vp;
kappaxkappa = kappa*kappa;

alpha = g2/2.0 - 1.0;
opa   = 1.0 + alpha;
oma   = 1.0 - alpha;
omta  = 1.0 - alpha*2.0;
twoma = 2.0 - alpha;
twoa  = 2.0*alpha;
ooa   = 1.0/alpha;
oota  = 1.0/twoa;
       
G2ma = gamma( twoma );
Gopa = gamma( opa   );
       
cqs   = cos( qs   ); sqs = sin( qs );
cqsxcqs = cqs*cqs;
cqi   = cos( qi   ); sqi = sin( qi );
cqixcqi = cqi*cqi;
cphis = cos( phis );

Pi = sqrt( kappaxkappa - cqixcqi );
Ps = sqrt( kappaxkappa - cqsxcqs );
       
S = cqs*cqi*cphis;

d  = 1.0/sqrt(2.0)*sqrt( 1.0 + sqi*sqs - S );
dz = 0.5*( sqi + sqs );
dt = 0.5*sqrt( cqixcqi - 2.0*S + cqsxcqs );
       
qis = asin( d );
 
dK = 2.0*kw*( dt + 0.0001 );

W2dK = w2/( dK^g2 );
        
Ris = freflco(qis,arho,vp,dp);
Ri  = freflco(qi ,arho,vp,dp) + 1.0;
Rs  = freflco(qs ,arho,vp,dp) + 1.0;

RxR   = abs( Ris )^2.0;
RixRi = abs( Ri  )^2.0;      
RsxRs = abs( Rs  )^2.0;      
       
A = RxR/( 8.0*pi );
A1 = 8.0*alpha*alpha*gamma( oota + 0.5 );
A2 = gamma( 0.5 )*gamma( ooa )*gamma( oota );
a  = ( A1/A2 )^twoa;
b = ( a^( 0.5 + 1.0/twoa )*gamma( ooa ) )/twoa;
E = 2.0*pi*w2*G2ma*( 2.0^( -twoa ) );
F = alpha*oma*Gopa;
ChxCh = E/F;
q0 = ChxCh*( 2.0^( omta ) )*( kw^( 2.0*oma ) ); 
C  = ( dt^( 4.0*alpha ) + a*q0*q0*( dz^4.0 ) )^( opa/twoa );
B = b*q0*( 1.0 + 100.0*dt^4.0 )/C;
G = ( 1.0/arho - 1.0 )*( S - Pi*Ps/arho ) + 1.0 - kappaxkappa/arho;
GxG = abs( G )^2.0;

sigmakr = A*( d^4.0 )*B;                        
sigmapr = 0.25*( kw^4.0 )*RixRi*RsxRs*GxG*W2dK;

endfunction
