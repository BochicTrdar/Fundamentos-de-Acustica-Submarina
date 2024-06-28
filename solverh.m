function dYds = solverh(Y,r)

    p = Y(1);
    z = Y(2);
    B = 1.3e3;
    epsilon = 7.37e-3;
    z1 = 1500.0;
    c1 = 1480.0;
    eta = 2*( z - z1 )/B;
    c   = c1*( 1 + epsilon*( eta + exp( -eta ) - 1 ) );
    dcdz = ( 2*c1*epsilon/B  )*( 1 - exp( -eta ) );
    ccc = c^3;
    dHdz = c1*c1/ccc*dcdz;
    dHdp = p;
    dYds(1) = -dHdz;
    dYds(2) =  dHdp;

endfunction

