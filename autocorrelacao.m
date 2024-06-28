% Fundamentos de Acústics Submarina

clear all, close all 

pkg load signal

a = -1.0;
b =  1.0;
amostragem = 1000; 
n = (b-a)*rand(1,amostragem) - b; % Ruído uniforme entre a e b
dt = 1.0/amostragem;
t = [0:dt:1-dt];
freq = 50;
w = 2*pi*freq;
s = cos( w*t ) + n; % Ruído no sinal
nfft = 2^nextpow2(2*amostragem-1);
% Autocorrelação:
R = xcorr( s, s );
L = length(R);
tR = dt*( [1:L] - L/2 );
figure(1)
subplot(211),plot(t,s,'k')
ylabel('s(t)')
grid on, box on
subplot(212),plot(tR,R,'k','LineWidth',2)
ylabel('R(\tau)')
xlabel('Tempo (s)','FontSize',18)
xlim([-0.5,0.5])
grid on, box on

