function p = pmodos(z,Z,k,zs,zh,rh,M)

p = [];
nr = length( rh );
nz = length( zh );

p  = zeros(nz,nr) + 1i*0;
pm = zeros(nz,nr) + 1i*0;

e0 = 1i*exp( -1i*pi/4.0 )/sqrt( 8*pi );

for i = 1:M
    Zm  = Z(:,i);
    Zms = interp1( z, Zm, zs );
    Zmh = interp1( z, Zm, zh );        
    Zsh = Zms*Zmh;
    Rm  = exp( 1i*k(i)*rh )./sqrt( k(i)*rh );
   [RM,ZM] = meshgrid(Rm,Zsh);
    pm  = RM.*ZM;
    p = p + pm;

endfor

p = p*e0;

endfunction
