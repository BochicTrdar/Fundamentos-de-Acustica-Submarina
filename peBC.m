function [B,C] = peBC( z, n, k0, dr)

B = [];
C = [];

h = abs( z(2) - z(1) );
hh = h*h;
  
lengthA = length( z );

A  = zeros( lengthA,lengthA );
B  = zeros( lengthA,lengthA );
C  = zeros( lengthA,lengthA );

cdiag  = -2.0/hh + k0*k0*( n.*n - 1 );

A = diag(  cdiag, 0  );
B = diag( -cdiag*0.5 + 2*1i*k0/dr, 0  );
C = diag(  cdiag*0.5 + 2*1i*k0/dr, 0  );

for i = 1:lengthA-1

    A(i,i+1) = 1.0/hh;
    A(i+1,i) = 1.0/hh;
    B(i,i+1) = 2*1i*k0/dr - 0.5/hh;
    B(i+1,i) = 2*1i*k0/dr - 0.5/hh;
    C(i,i+1) = 2*1i*k0/dr + 0.5/hh;
    C(i+1,i) = 2*1i*k0/dr + 0.5/hh;

endfor

endfunction
