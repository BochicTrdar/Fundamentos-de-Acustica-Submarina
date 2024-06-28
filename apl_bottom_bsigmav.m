function sigmav = apl_bottom_bsigmav(qi,qs,phis,g3,w3,kw,arho,vp,dp)

kappa = ( 1.0 + 1i*dp )/vp;
kappaxkappa = kappa*kappa;

cqs   = cos( qs   ); cqsxcqs = cqs*cqs;
cqi   = cos( qi   ); cqixcqi = cqi*cqi;
cphis = cos( phis );

S = cqs*cqi*cphis;

pps = sqrt( kappaxkappa - cqsxcqs );
ppi = sqrt( kappaxkappa - cqixcqi );

Rs = freflco(qs,arho,vp,dp) + 1.0;
Ri = freflco(qi,arho,vp,dp) + 1.0;
RsxRs = abs( Rs )^2.0;
RixRi = abs( Ri )^2.0;

Repis = real( ppi + pps );
Impis = imag( ppi + pps );
A = 2.0*kw*arho*arho*Impis;
F = S - kappaxkappa - ppi*pps;
FxF = abs( F )^2.0;
dt = 0.5*sqrt( cqixcqi + cqsxcqs - 2.0*S ); 
dk = kw*sqrt( 4.0*dt*dt + Repis*Repis );
Wpp = w3/( dk^g3 );   
sigmav0 = pi/2.0*( kw^4.0 )*FxF*Wpp;      
sigmav = sigmav0*RixRi*RsxRs/A;      
       
endfunction
