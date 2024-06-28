function R = bdryr(rho1,rho2,cp1,cp2,cs2,alphap,alphas,theta)
       
e = exp(1);
       
tilap = alphap/( 40.0*pi*log10( e ) );
tilas = alphas/( 40.0*pi*log10( e ) );

tilcp2 = cp2*(1.0-1i*tilap)/(1.0+tilap*tilap);
tilcs2 = cs2*(1.0-1i*tilas)/(1.0+tilas*tilas);

a1 = rho2/rho1;
a2 = tilcp2/cp1;
a3 = tilcs2/cp1;
a4 = a3*sin( theta );
a5 = 2.0*a4.*a4;
a6 = a2*sin( theta );
a7 = 2.0*a5 - a5.*a5;
       
d = a1*( a2*( 1.0 - a7 )./sqrt( 1.0 - a6.*a6 ) + a3*a7./sqrt( 1.0 - 0.5*a5 ) );
       
R = ( d.*cos(theta) - 1.0 )./( d.*cos(theta) + 1.0 );

endfunction


