% Fundamentos de Acústica Submarina 

clear all, close all 

Dmax = 5000;
Rmaxkm = 100; 
Rmax = Rmaxkm*1000;

% Posição inicial:
rs = 0;
zs = 1500;

dtau = 0.1;
t = [0:dtau:67];

z0 = 1500.0;
c0 = 1480.0;

% Ângulos de lançamento:
nrays = 25;
thetas = linspace(-12,12,nrays);

for i = 1:nrays

    vr = c0*cos( -thetas(i)*pi/180 );
    vz = c0*sin( -thetas(i)*pi/180 );
    y0 = [rs, zs, vr, vz];
    % Integração da ODE:
    y = lsode("solverg", y0, t);

    r = squeeze( y(:,1) ); rkm = r/1000.0;
    z = squeeze( y(:,2) );

    figure(1), hold on
    plot(rkm,z,'k','LineWidth',2)

endfor

xlabel('Distância (km)','FontSize',18)
ylabel('Profundidade (m)','FontSize',18)
xlim([0,Rmaxkm])
view(0,-90)
grid on, box on


