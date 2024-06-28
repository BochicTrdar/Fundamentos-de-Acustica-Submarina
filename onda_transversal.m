% Fundamentos de Acústica Submarina 

clear all, close all 

quadros = 101;
nx    = 21;
w     = 1.0;
k     = 1.0;
xmax  = 2.0*pi;
t     = linspace(0.0,20.0*pi,quadros);
x     = linspace(0.0,xmax,nx);

for i = 1:quadros
p = sin( k*x - w*t(i) );
figure(1)
plot(x,p,'ko'), hold on
stem(x,p,'k--'), hold off
xlabel('X','FontSize',18)
ylabel('Y','FontSize',18)
box on, grid on
pause(0.1)
endfor

