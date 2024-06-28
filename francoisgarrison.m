function a = francoisgarrison(freq,T,S,pH,z)
    
c   = 1412.0 + 3.21*T + 1.19*S + 0.0167*z;
theta = 273.0 + T;
fxf = freq.^2;
f1 = 2.8*sqrt(S/35.0)*10^(4.0-1245.0/theta);
f2 = 8.17*10^(8.0-1990.0/theta)/( 1.0 + 0.0018*(S-35.0) );
A1 = 8.86/c*10^(0.78*pH-5);
A2 = 21.44*S/c*( 1.0 + 0.025*T );
TT = T*T; TTT = TT*T;
zz = z*z;

if T <= 20
A3 = 4.937e-4 - 2.59e-5*T + 9.11e-7*TT - 1.50e-8*TTT;
else
A3 = 3.964e-4 - 1.146e-5*T + 1.45e-7*TT - 6.5e-10*TTT;
endif

P2 = 1 - 1.35e-4*z + 6.2e-9 *zz;
P3 = 1 - 3.83e-5*z + 4.9e-10*zz;

a = A1*f1*fxf./( f1^2 + fxf ) + A2*P2*f2*fxf./( f2^2 + fxf ) + A3*P3*fxf;

endfunction

