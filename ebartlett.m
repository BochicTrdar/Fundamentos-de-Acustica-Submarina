% Fundamentos de Acústica Submarina 

clear all, close all

% Coordenadas "reais" da fonte:
zs =   50.0;
rs = 1000.0;

nr   =  201;
rmin =  500.0;
rmax = 1500.0;
rb = linspace(rmin,rmax,nr); rkm = rb/1000.0;
nz   = 101;
D    = 100.0;
z    = linspace(0.0,D,nz);
nzb = 81;
zb = linspace(10,90,nzb);
c = 1500.0;
freq = 50.0; w = 2*pi*freq;
k = w/c; kxk = k*k;
M = fix( w*D/(pi*c) - 0.5 );
nh = 51;
zh = linspace(25,75,nh);
km = ( [1:M] - 0.5 )*pi/D;
kmsq = km.*km;
kh = sqrt( kxk - kmsq );

disp('Generating the data...')

Z = zeros(nz,M);

for i = 1:M
    Z(:,i) = sin( km(i)*z );
endfor

Z = Z*2.0/D;

d = pmodos(z,Z,kh,zs,zh,rs,M); n = norm( d ); dn = d/n; % Dados "reais"

disp('Calculating the Bartlett power...')

B = zeros(nzb,nr);

for j = 1:nzb
    zj = zb(j);
    e = pmodos(z,Z,kh,zj,zh,rb,M);
    for i = 1:nr
        ei = e(:,i); n = norm( ei ); en = ei/n; % Réplica
        R = dn*dn';
        B(j,i) = abs( en'*R*en ); % Estimador de Bartlett
    endfor
endfor

colormap('jet');
figure(1)
pcolor(rkm,zb,B), shading interp, colorbar
xlabel('Distância (km)','FontSize',18)
ylabel('Profundidade (m)','FontSize',18)

