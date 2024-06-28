% Fundamentos de Acústica Submarina 

clear all, close all

D = 5000;
nz = 101;
z = linspace(0,D,nz);
dz = abs( z(2) - z(1) );
rmaxkm = 100;
rmax = rmaxkm*1000;
nr = 101;
r = linspace(0,rmax,nr); 
r(1) = 1.0;
rkm = r/1000.0;
freq = 50;
z0 = 1500.0;
c0 = 1480.0;
[c,dcdz] = munk(z,z0,c0);
p0 = 1.0/( 4*pi );
[Z,kh] = modos( z, c, freq, [1,0], [1,0]);

m = length( kh );

for i = 1:m
    Zi = Z(:,i);
    Im = sqrt( dz*sum( Zi.*Zi ) );
    Z(:,i) = Zi/Im;
endfor

p = pmodos(z,Z,kh,z0,z,r,m);
p = p/p0;
tl = -20*log10( abs( p ) );

tej = flipud( colormap('jet') );
colormap(tej)
figure(1)
pcolor(rkm,z,tl), shading interp, colorbar 
view(0,-90)
xlabel('Distância (km)','FontSize',18)
ylabel('Profundidade (m)','FontSize',18)

