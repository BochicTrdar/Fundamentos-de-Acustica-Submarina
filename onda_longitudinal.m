% Fundamentos de Acústica Submarina 

clear all, close all 

quadros = 101;
nx    = 51;
ny    = 51;
w     = 1.0;
k     = 1.0;
xmax  = 3.0*pi;
ymax  = 1.0;
t     = linspace(0.0,10.0*pi,quadros);
x     = linspace(-xmax,xmax,nx);
y     = linspace(-ymax,ymax,ny);

% Animação: 

figure(1)
for i = 1:quadros
%i
p = sin( k*x - w*t(i) );
xi = x + p;
[Xi,Y] = meshgrid(xi,y);
figure(1)
plot(Xi,Y,'ko')
xlabel('X','FontSize',18)
ylabel('Y','FontSize',18)
xlim([-3*pi,3*pi])
pause(0.1)

endfor

