% Fundamentos de Acústica Submarina 

clear all, close all

D = 5000;
nz = 201;
z = linspace(0,D,nz);
rmaxkm = 100; rmax = rmaxkm*1000;
nr = 501;
r = linspace(0,rmax,nr);
dr = r(2) - r(1);
r(1) = 1.0;
rkm = r/1000.0;
freq = 50; w = 2*pi*freq;
z0 = 1500.0;
c0 = 1480.0;
[c,dcdz] = munk(z,z0,c0);
k0 = w/c0;
n  = c0./c;
p = zeros(nz,nr);
U = zeros(nz,nr);
ks = k0/15;
U(:,1) = sqrt( ks )*exp( -0.5*ks*ks*( z - z0 ).^2 );

[B,C] = peBC(z, n, k0, dr);

for i = 1:nr-1
    y = B*U(:,i);
    U(:,i+1) = C\y;
endfor    

for i = 1:nr
    H0 = sqrt( 2/(pi*k0*r(i)) )*exp( 1i*( k0*r(i) - pi/4  ) );
    p(:,i) = U(:,i)*H0;
endfor    

tl = -20*log10( abs( p ) );

tej = flipud( colormap('jet') );
colormap(tej)
figure(1)
pcolor(rkm,z,tl), shading interp, colorbar, caxis([30 120])
view(0,-90)
xlabel('Distância (km)','FontSize',18)
ylabel('Profundidade (m)','FontSize',18)

