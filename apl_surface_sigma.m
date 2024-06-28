% Fundamentos de Acústica Submarina

function sr = apl_surface_sigma(q,freq,U,qf)

fkHz = freq/1000.0;
A = 1.3e-5*U;
sxs = 0.034;

if ( U >= 1.0 )
   sxs = 4.6e-3*log( 2.1*U*U );
   p2 = 4.0*pi*sxs;
endif

if ( q*180.0/pi <= 85.0 )
   ssc = A*( (tan(q))^4.0 );
else
   ssc = 0.0;
endif
   
if (U >= 6 )
   SBL = 1.26e-3/sin(q)*( U^1.57 )*( fkHz^0.85 );
else
   SBL = 1.26e-3/sin(q)*( 6^1.57 )*( fkHz^0.85 )*exp( U - 6.0 );
endif   

g = 0.5*pi - q;

secg = 1.0/cos( g );
p1   = secg^4.0;
x    = tan(g)^2.0/sxs;
sf   = p1/p2*exp( -x );
x    = 0.524*( qf - q )*180.0/pi;
f    = 1.0/( 1.0 + exp(x) );
sri  = f*sf + ( 1.0 - f )*ssc;  
sr   = sri*10^( -SBL/10.0 );

endfunction
