% Fundamentos de Acústica Submarina 

clear all, close all 

quadros  =  36;
periodos =   6;
nx       =  51;

freq  =   50.0; T = 1.0/freq; w = 2.0*pi*freq;
c     = 1500.0;
k     = w/c;
% Comprimento de onda:
L     = 2.0*pi/k;
tmin  =  0;
tmax  =  T*periodos;
xmax  = 3.0*L;
x = linspace(-xmax,xmax,nx); y = x;

[X,Y] = meshgrid(x,y); 
R = sqrt( X.*X + Y.*Y );
R(24:26,24:26) = NaN; % evitar R = 0...

t = linspace(tmin,tmax,quadros);

% Animação:

for i = 1:quadros
figure(1)
f = k*R - w*t(i);
p = real( exp( 1i*f )./R );
mesh(x,y,p)
zlim([-0.5,0.5])
pause(0.1)
endfor

