% Fundamentos de Acústica Submarina 

clear all, close all 

mu    = 0.0;
sigma = 1.0;
amostragem = 1000; 
n = sigma*randn(1,amostragem) + mu;
x = linspace(-10,10,amostragem);
t = x + 10; 
s = 1.5*exp( -x.*x );
spn = s + 0.5*n;

figure(1)
subplot(211)
plot(t,s)
ylabel('Amplitude','FontSize',18)
title('Sinal a detetar','FontSize',18)
ylim([-1,2])
grid on, box on
subplot(212)
plot(t,spn)
xlabel('Tempo (s)','FontSize',18)
ylabel('Amplitude','FontSize',18)
title('Sinal detetado','FontSize',18)
ylim([-2,2])
grid on, box on

