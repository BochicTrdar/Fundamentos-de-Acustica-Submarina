% Fundamentos de Acústica Submarina

clear all, close all

quadros  = 101;
periodos =  50;
nx       = 201;

v  = 1500.0; % vfase
% Descomentar e executar a animação: 
c  = v; % vgrupo = vfase
%c = 0; % vgrupo = 0
%c = -250; % vgrupo < 0
f1  = 50.0;
w1 = 2.0*pi*f1;
k1 = w1/v; dk = k1/10.0;
k2 = k1 + dk;
dw = c*dk;
w2 = w1 + dw;
f2 = w2/( 2.0*pi );
T1 = 1.0/f1;
T2 = 1.0/f2;

[v,c]

L1 = 2.0*pi/k1;
L2 = 2.0*pi/k2;

tmin = 0.0;
tmax = max([T1,T2])*periodos;

xmax = 10.0*max([L1,L2]);

x = linspace(-xmax,xmax,nx);
t = linspace(tmin,tmax,quadros);

% Animação:

for i = 1:quadros
    p1 = exp( 1i*( k1*x - w1*t(i) ) );
    p2 = exp( 1i*( k2*x - w2*t(i) ) );
    p = 0.5*real( p1 + p2 );
    figure(1)
    plot(x,p)    
    xlabel('x','FontSize',18)
    ylabel('p(x,t)','FontSize',18)
    pause(0.1)
endfor

