% Fundamentos de Acústica Submarina 

clear all, close all 

ds = 100; % Passo do raio

Dmax = 5000;
Rmaxkm = 100; 
Rmax = Rmaxkm*1000;

% Posição da fonte:
rs = 0;
zs = 1500;
z0 = 1500; 
c0 = 1480;

s = [rs:ds:Rmax]; % comprimento do raio

% Definir ângulos de lançamento:

nrays = 25;
thetas = linspace(-12,12,nrays);

for i = 1:nrays

    sr0 = cos( -thetas(i)*pi/180 )/c0;
    sz0 = sin( -thetas(i)*pi/180 )/c0;
    y0 = [rs, zs, sr0, sz0];
    
    % Integrar a ODE:
    y = lsode("solver", y0, s);

    r = squeeze( y(:,1) ); rkm = r/1000.0;
    z = squeeze( y(:,2) );

    figure(1), hold on
    plot(rkm,z,'k','LineWidth',2)

endfor

hold off
xlabel('Distância (km)','FontSize',18)
ylabel('Profundidade (m)','FontSize',18)
xlim([0,Rmaxkm])
view(0,-90)
grid on, box on

