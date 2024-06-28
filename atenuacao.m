% Fundamentos de Acústica Submarina

clear all, close all

nfreqs = 101;
fmin =     1;
fmax =  1000;
n = linspace(0,3,101);
freqs = 10.^n; % kHz!
S  = 35.0;
T  = 20.0;
pH =  8.0;
Z  =  0.0;
fxf = freqs.^2;

aT = 3.3e-3 + 0.11*fxf./( 1.0 + fxf ) + 44.0*fxf./( 4100.0 + fxf ) + 3.0e-4*fxf;
aFG = francoisgarrison(freqs,T,S,pH,Z);

figure(1)
plot(freqs,aT ,'k'  ,'LineWidth',2), hold on
plot(freqs,aFG,'k--','Linewidth',2)
xlabel('Frequência (kHz)','Fontsize',18)
ylabel('\alpha (dB/km)','Fontsize',18)
xlim([1,1000])
legend('Thorp','Francois-Garrison')
hold off
box on, grid on

