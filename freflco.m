function Vww = freflco(q,arho,vp,dp)

a_p   = vp/( 1.0 + 1i*dp );
apxap = a_p*a_p;
cosq  = cos( q );
sinq  = sin( q );
cqxcq = cosq*cosq;
sinqp = sqrt( 1.0 - apxap*cqxcq );
zwp   = arho*a_p*sinq/sinqp;
Vww   = ( zwp - 1.0 )/( zwp + 1.0 );

endfunction
