% Fundamentos de Acústica Submarina 

clear all, close all 

theta = linspace(0,90,181);
thetar = theta*pi/180;

% Fundo suave
cw = 1500.0;
cp = 1300.0;
cs = 0.0;
alphap = 0.0;
alphas = 0.0;
rhow = 1000.0;
rhob = 1800.0;

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar);

Rs = abs( R );

% Fundo rígido
cw = 1500.0;
cp = 1800.0;
cs = 0.0;
alphap = 0.0;
alphas = 0.0;
rhow = 1000.0;
rhob = 1800.0;

thetacr = 180.0/pi*asin( cw/cp )

R = bdryr(rhow,rhob,cw,cp,cs,alphap,alphas,thetar);

Rr = abs( R );

figure(1)
plot(theta,Rr,'k'  ,'LineWidth',2), hold on
plot(theta,Rs,'k--','LineWidth',2), hold off
xlabel('\theta','FontSize',18)
ylabel('|R(\theta)|','FontSize',18)
ylim([0,1.1])
legend('Fundo rijo','Fundo suave')
grid on, box on

