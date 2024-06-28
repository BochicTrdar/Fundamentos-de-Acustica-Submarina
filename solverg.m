function dYds = solverg(Y,s)

    r  = Y(1);
    z  = Y(2);
    X1 = Y(3);
    X2 = Y(4);
    [c,dcdz] = munk(z,1500,1480);
    X1t = ( 2.0/c )*dcdz*X1*X2;
    X2t = ( 1.0/c )*dcdz*( X2*X2 - X1*X1 );
    dYds(1) = X1 ; 
    dYds(2) = X2 ;
    dYds(3) = X1t;
    dYds(4) = X2t;

endfunction

