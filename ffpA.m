function A = ffpA( z, c, freq, k)

A = [];

h = abs( z(2) - z(1) );
hh = h*h;

w = 2*pi*freq;
ww = w*w;
cc = c.*c;
lengthA = length(z); 
A  = zeros(lengthA,lengthA);

cdiag = -2.0/hh + ww./cc;

A = diag(cdiag,0);

for i = 1:lengthA-1
    A(i,i+1) = 1.0/hh;
    A(i+1,i) = 1.0/hh;
endfor
    
A = A - k*k*eye( lengthA );
    
endfunction
