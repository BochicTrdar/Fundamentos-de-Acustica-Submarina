% Fundamentos de Acústica Submarina 

clear all, close all 

dr = 100; % Passo em distância horizontal

Dmax = 5000;
Rmaxkm = 100; 
Rmax = Rmaxkm*1000;

% Posição da fonte:
rs = 0:
zs = 1500;

r = [rs:dr:Rmax]; rkm = r/1000.0;

% Definir ângulos de lançamento:

nrays = 25;
thetas = linspace(-12,12,nrays);

for i = 1:nrays

    p0 = tan( -thetas(i)*pi/180 );
    z0 = zs;
    y0 = [p0,z0];
    % Integrar a ODE:
    y = lsode("solverh", y0, r);
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

