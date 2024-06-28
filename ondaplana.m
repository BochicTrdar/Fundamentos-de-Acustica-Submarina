% Fundamentos de Acústica Submarina

clear all, close all 

quadros  =  36;
periodos =   6;
nx       =  51;

freq  =   50.0; T = 1.0/freq; w = 2.0*pi*freq;
c     = 1500.0;
k     = w/c;
% Ângulo de propagação (mudar e ver efeito)
phi   = 0.0;
% Componentes do número de onda:
kx    = k*cos( phi*pi/180.0 );
ky    = k*sin( phi*pi/180.0 );
% Comprimento de onda:
L     = 2.0*pi/k;
tmin  =  0;
tmax  =  T*periodos;
xmax  = 3.0*L;
x = linspace(-xmax,xmax,nx); y = x;

[X,Y] = meshgrid(x,y);

t = linspace(tmin,tmax,quadros);

% Animação:
for i = 1:quadros
figure(1)
p = real( exp( 1i*( kx*X + ky*Y - w*t(i) ) ) );
mesh(x,y,p)
xlabel('X','FontSize',18)
ylabel('Y','FontSize',18)
zlim([-0.5,0.5])
pause(0.1)
endfor
