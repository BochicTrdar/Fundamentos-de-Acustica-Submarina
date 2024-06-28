function [themodes, wavenumbers] = modos( z, c, f, tbc, bbc)

themodes    = [];
wavenumbers = [];

h = abs( z(2) - z(1) );
hh = h*h;

alpha1 = tbc(1); 
beta1  = tbc(2);
alpha2 = bbc(1); 
beta2  = bbc(2);

w = 2*pi*f; 
k = w./c;
kk = k.*k;  

lengthz = length( z );  
lengthA = lengthz - 2;
y  = zeros( lengthz,lengthz );  
A  = zeros( lengthA,lengthA );   
Au = zeros( lengthA,lengthA );
Al = zeros( lengthA,lengthA );

ncdiag =  1.0/hh * ones( 1,lengthA-1 );  
cdiag  = -2.0/hh * ones( 1,lengthA   ) + kk(2:end-1);

A = diag( cdiag, 0 );

for i = 1:lengthA-1
    Au(i,i+1) = ncdiag(i);
    Al(i+1,i) = ncdiag(i);
endfor

A = A + Au + Al;

A(  1,  1) =  1/hh * ( hh*kk(2)     + ( -beta1/h )/( alpha1 - beta1/h ) - 2 );  
A(end,end) =  1/hh * ( hh*kk(end-1) + (  beta2/h )/( alpha2 + beta2/h ) - 2 );  

rankA = rank( A );

if rankA < lengthA
   disp( 'Não há solução numérica para estas condições de fronteira...' )
else
   [modese,eigenvalues] = eig( A );
    eigenvalues = diag( eigenvalues );
    modes_at_top    = modese(  1,:)*( -beta1/h )/( alpha1 - beta1/h );
    modes_at_bottom = modese(end,:)*(  beta2/h )/( alpha2 + beta2/h );    
    modes = zeros(lengthz,lengthA);
    modes(  1,:) = modes_at_top;
    modes(end,:) = modes_at_bottom;
    modes(2:end-1,:) = modese;
    [se,indexes] =  sort( eigenvalues ); 

    eigenvalues = eigenvalues( indexes );
    eigenvalues = flipud( eigenvalues );
    modes       = fliplr( modes(:,indexes) );

    ipos = find( eigenvalues > 0 );
    eigenvalues = eigenvalues( ipos );
    wavenumbers = sqrt( eigenvalues );
    themodes = modes(:,ipos);
    
    for i = 1:length(ipos)
        phi = themodes(:,i);
        if phi(2) < 0
           phi = -phi;
        endif
        themodes(:,i) = phi/norm(phi);
    endfor
endif

endfunction
