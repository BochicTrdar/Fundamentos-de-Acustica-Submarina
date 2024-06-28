function dYds = solver(Y,s)

r  = Y(1);
z  = Y(2);
sr = Y(3);
sz = Y(4);

[c,dcdz] = munk(z,1500,1480);

cc = c*c; dcdr = 0.0;

dYds(1) = c*sr;
dYds(2) = c*sz;
dYds(3) = -dcdr/cc;
dYds(4) = -dcdz/cc;

endfunction
