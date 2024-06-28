function [c,dcdz] = munk(z,z0,c0)

B = 1.3e3;
e = 7.37e-3;
eta = 2*( z - z0 )/B;
c   = c0*( 1 + e*( eta + exp( -eta ) - 1 ) );
dcdz = ( 2*c0*e/B  )*( 1 - exp( -eta ) );

endfunction
