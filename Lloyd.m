% Fundamentos de Acústica Submarina 

clear all, close all 

cw   = 1500.0;
freq =  150.0;
Tx   =   25.0;
Rx   =  200.0;
rmin =    0.0; 
rmax = 2000.0;
nr = 501;
r = linspace(rmin,rmax,nr); rxr = r.*r;
r(1) = 1.0;
rkm = r/1000;
l = cw/freq;
k = 2*pi/l;
R1 = sqrt( rxr + ( Tx - Rx )*( Tx - Rx ) );
R2 = sqrt( rxr + ( Tx + Rx )*( Tx + Rx ) );

p = exp( 1i*k*R1 )./R1 - exp( 1i*k*R2 )./R2;

TL  = -20*log10( abs( p ) ); % TL dos raios
TLg =  20*log10( r ); % TL decaimento geométrico

figure(1), hold on
plot(rkm,TL ,'k'  ,'LineWidth',2)
plot(rkm,TLg,'k--','LineWidth',2)
hold off
xlabel('Distância (km)','FontSize',18)
ylabel('TL (dB)','FontSize',18)
view(0,-90)
legend('Exacto','Decaimento geométrico')
grid on, box on



