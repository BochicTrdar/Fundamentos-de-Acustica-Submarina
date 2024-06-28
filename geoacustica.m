% Fundamentos de Acústica Submarina 

clear all, close all 

freq   = 50.0; w = 2*pi*freq;
% Valores procurados:
cb     = 1900.0; rhob = 2.0;
% Guia de onda:
D      =  100.0;
c1     = 1500.0; rho1 = 1.0;
% Parâmetros do Bartlett:
nc     = 101;
cmin = 1800.0;
cmax = 2000.0;
c2     = linspace(cmin,cmax,nc);
nrho = 101;
rhomin = 1.5;
rhomax = 2.5;
rho2   = linspace(rhomin,rhomax,nrho);
% Guia de onda:
zs     = 50.0;
rh     = 5000.0;
B      = zeros(nrho,nc);
nzh    = 51;
zh     = linspace(25,75,nzh);
nz     = 101;
z      = linspace(0,D,nz); 
dz     = z(2) - z(1);

% Observação:

% Pekeris: números de onda
kh     = kpekeris(c1,rho1,cb,rhob,D,freq);
M      = length( kh );
Z      = zeros(nz,M);
kz     = sqrt( (w/c1)^2 - kh.*kh );

% Modos:
for j = 1:M
    Zj = sin( kz(j)*z );
    N = sqrt( dz*sum( Zj.*Zj ) );
    Z(:,j) = Zj/N;
endfor

% Campo dos modos
d = pmodos(z,Z,kh,zs,zh,rh,M); dn = d/norm( d );

% Cálculo de réplicas e ajustamento do campo
for j = 1:nc
    ci = c2(j);
    for j2 = 1:nrho
        rhoi = rho2(j2);
        kh = kpekeris(c1,rho1,ci,rhoi,D,freq);
        M = length( kh );
        Z = zeros(101,M);
        kz = sqrt( (w/c1)^2 - kh.*kh );
        for jj = 1:M
            Zj = sin( kz(jj)*z );
            N = sqrt( dz*sum( Zj.*Zj ) );
            Z(:,jj) = Zj/N;
        endfor    
        eij = pmodos(z,Z,kh,zs,zh,rh,M);
        en = eij/norm( eij );
        R = dn*dn';
        B(j2,j) = abs( en'*R*en );
    endfor
endfor

colormap('jet')
figure(1)
pcolor(c2,rho2,B), shading interp
colorbar
xlabel('Velocidade do som (m/s)','FontSize',18)
ylabel('Densidade (g/cm$^3$)','FontSize',18)

