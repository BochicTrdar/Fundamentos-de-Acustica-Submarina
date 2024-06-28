% Fundamentos de Acústica Submarina 

clear all, close all 

nfreqs = 11;
fmin   = 21.5;
fmax   = 26.0;
freqs  = linspace(fmin,fmax,nfreqs);
D      =  100.0;
c1     = 1500.0; rho1 = 1.0;
c2     = 1800.0; rho2 = 1.8;
rmax   = 3000.0;
rh     = linspace(0,rmax,101);
rh(1)  = 1.0;
rhkm   = rh/1000.0;
z      = linspace(0,D,101); dz = abs( z(2) - z(1) );
zs     = 36.0;
zh     = 36.0;
p0     = 1/( 4*pi );

for i = 1:nfreqs

    wi = 2*pi*freqs(i);
    kh = kpekeris(c1,rho1,c2,rho2,D,freqs(i));
    M = length( kh );
    Z = zeros(101,M);
    kz = sqrt( (wi/c1)^2 - kh.*kh );
    for j = 1:M
        Zj = sin( kz(j)*z );
        N = sqrt( dz*sum( Zj.*Zj ) );
        Z(:,j) = Zj/N;
    endfor
    p = pmodos(z,Z,kh,zs,zh,rh,M);
    p = p/p0;
    tl = -20*log10( abs( p ) ) + i*2.0;
    figure(1), hold on
    plot(rhkm,tl,'k','LineWidth',2)

endfor
hold off
xlabel('Distância (km)','FontSize',18)
ylabel('TL (dB)','FontSize',18)
view(0,-90)
grid on, box on

