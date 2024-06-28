% Fundamentos de Acústica Submarina 

clear all, close all

quadros  = 36;
periodos =  6;
nx       = 51;

freq  =  100.0; T = 1.0/freq; w = 2.0*pi*freq;
c     = 1500.0;
k     = w/c;
% Comprimento de onda:
L     = 2.0*pi/k;
% Comprimento da antena: 
Larray = 2*L;
tmin  =  0;
tmax  =  T*periodos;
xmax  = 3.0*L;
x = linspace(-xmax,xmax,nx); y = x;

[X,Y] = meshgrid(x,y);
THETA = atan2(Y,X);
R  = sqrt( X.*X + Y.*Y );
o = exp( 1i*k*R ); % Onda circular

theta0 = linspace(0,pi,quadros);

figure(1)
for i = 1:quadros
    XB = 0.5*k*Larray*sin( THETA - theta0(i) );
    p = sinc( XB/pi ).*real( o );
    pcolor(x,y,p), shading interp
    xlim([-xmax,xmax])
    ylim([-xmax,xmax])
    pause(0.1)
endfor


