% Fundamentos de Acústica Submarina 

clear all, close all

D = 5000;
nz = 500;
z = linspace(0,D,nz); dz = z(2) - z(1);
freq = 50; w = 2*pi*freq;
z0 = 1500.0;
zs = z0;
c0 = 1480.0;
c = munk(z,z0,c0);
k = w./c;
kmin = min( k );
kmax = max( k );
nk = 501;
k = linspace(kmin,kmax,nk);
dk = k(2) - k(1);
k = k - 1i*dk;
nr     = 501;
rmaxkm = 100;
rmax = rmaxkm*1000;
dr = rmax/nr;
r = linspace(dr,rmax,nr); rkm = r/1000.0;
p = zeros(nz,nk);
d = zeros( nz,1 );
iz = fix( zs/dz );
d( iz ) = 1.0; % Dirac numérico

G = zeros(nz,nk);

for i = 1:nk
    A = ffpA( z, c, freq, k(i) );
    G(:,i) = A\d;
endfor

for i = 1:nr
     kr = k*r(i);
     for j  = 1:nz
         II = G(j,:).*sqrt( k ).*exp( 1i*kr );
         p(j,i) = dk*sum( II )/r(i);
     endfor
endfor

p = 4*pi*p*exp( 1i*pi/4 )/sqrt( 2*pi );

tl = -20*log10( abs( p ) );

tej = flipud( colormap('jet') );
colormap(tej)
figure(1)
pcolor(rkm,z,tl), shading interp, colorbar 
view(0,-90)
xlabel('Distância (km)','FontSize',18)
ylabel('Profundidade (m)','FontSize',18)

