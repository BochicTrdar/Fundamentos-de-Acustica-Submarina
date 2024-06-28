% Fundamentos de Acústica Submarina 

clear all, close all 

pkg load signal

amostragem = 10000;
nyquist    =  5000;
nbranco = randn(1,amostragem);
dt = 1.0/amostragem;
t = [0:dt:1-dt];
B = [0.049922035, -0.095993537, 0.050612699, -0.004408786];
A = [1.0        , -2.494956002, 2.017265875, -0.522189400];
[w,h] = freqz(B,A);
frequencias = w/pi*nyquist;
nrosa = filter(B, A, nbranco);
Rbranco = xcorr(nbranco,nbranco);
Rrosa   = xcorr(nrosa  , nrosa );
l = length( Rbranco );
tR = linspace(-1.0,1.0,l);
Rbranconor = abs( Rbranco )/max( abs( Rbranco ) );
Rrosanor   = abs( Rrosa   )/max( abs( Rrosa   ) );

figure(1)
subplot(211)
plot(frequencias,abs(h),'k','LineWidth',2)
xlabel('Frequência (Hz)')
ylabel('H(f)','FontSize',18)
xlim([0,0.1*nyquist])
grid on, box on
subplot(212)
plot(t,nrosa,'k')
xlabel('Tempo (s)')
ylabel('n(t)','FontSize',18)
grid on, box on
figure(2)
plot(tR,Rbranconor,'k'  ,'LineWidth',2), hold on
plot(tR,Rrosanor  ,'k--','LineWidth',2), hold off
xlabel('Tempo (s)')
title('|R(\tau)|','FontSize',18)
xlim([-0.1,0.1])
legend('Branco','Rosa')
grid on, box on

