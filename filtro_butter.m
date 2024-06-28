% Fundamentos de Acústica Submarina 

clear all, close all 

pkg load signal

a = -1.0;
b =  1.0;
amostragem = 1000;
nyquist    =  500; 
n = (b-a)*rand(1,amostragem) - (b-a)/2; % ruído branco
dt = 1.0/amostragem;
t = [0:dt:1-dt];
freq = 50;
f1   = 20.0; 
f2   = 80.0;
w = 2*pi*freq;
s = cos( w*t ) + n; % sinal e ruído
low  = f1/nyquist;
high = f2/nyquist;
% H = B/A:
[B, A] = butter(4, [low, high], 'bandpass');
sf = filter(B, A, s);

figure(1)
subplot(211)
plot(t,s,'k')
ylabel('s(t)','FontSize',18)
grid on, box on
subplot(212)
plot(t,sf,'k','LineWidth',2)
ylabel('s_f(t)','FontSize',18)
xlabel('Tempo (s)','FontSize',18)
grid on, box on

