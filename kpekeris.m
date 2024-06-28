function kp = kpekeris(c1,rho1,c2,rho2,D,freq)
    
kp = [];

w = 2*pi*freq;
k1 = w/c1;
k2 = w/c2;

nk = 1001;
k = linspace(k1,k2,nk);
kxk = k.*k;

r1 = sqrt( k1*k1 - kxk );
r2 = sqrt( kxk - k2*k2 );
S1 = sin( r1*D );
C1 = cos( r1*D );

f = S1.*r2/rho2 + C1.*r1/rho1;

for i = 1:nk-1 
   
    x1 = k(i); x2 = k(i+1);
    y1 = f(i); y2 = f(i+1);
    p  = y1*y2;
    x3 = (x1*y2-x2*y1)/(y2-y1);
     
    if p < 0
       kp = [kp x3];
    endif
    
endfor

endfunction

