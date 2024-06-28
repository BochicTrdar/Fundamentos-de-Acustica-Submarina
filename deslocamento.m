% Fundamentos de Acústica Submarina

clear all, close all

% Ângulo de incidência:
theta = linspace(50,70,181);
thetar = theta*pi/180;
dtheta = diff( thetar );

f = 150.0;
w = 2*pi*f;

% Fundo rígido
cw = 1500.0;
cp = 1800.0;
cs =    0.0;
alphap =  0.0;
alphas =  0.0;
rhow = 1000.0;
rhob = 1800.0;
k = w/cw;
kh = k*sin( thetar );

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar);

rR = real( R );
iR = imag( R );
phi = atan2( iR, rR );
dphi = diff( phi );
dk   = diff( kh );
displacement = -dphi./dk;

figure(1)
plot(theta(1:180),displacement,'k','LineWidth',2)
xlabel('\theta','FontSize',18)
ylabel('\Delta','FontSize',18)
grid on, box on

