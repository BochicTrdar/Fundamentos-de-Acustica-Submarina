% Fundamentos de Acústica Submarina

function s = apl_bub_sigma(q,freq,U)

fkHz = freq/1000.0;
f2 = ( fkHz/25.0 )^0.85;
       
if U < 11
   f1 = -5.2577 + 0.4701*U;
   bv = f2*( 10.0^f1 );
else
   f1 = -5.2577 + 0.4701*11;
   bv11 = f2*( 10.0^f1 );
   f3 = (U/11.0)^3.5;
   bv = bv11*f3;
endif
       
b = bv/sin( q );
dr = 0.0136;
p1 = bv*dr;
d = 2.55e-2*( fkHz^(1.0/3.0) );
p2 = 4.0*pi*d;
r1 = 1.0 + 8.0*b*exp( -2.0*b ) - exp( -4.0*b );
r2 = 2.0*b;
r = r1/r2;
s = p1/p2*r;

endfunction
