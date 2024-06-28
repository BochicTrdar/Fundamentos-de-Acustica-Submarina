% Fundamentos de Acústica Submarina

clear all, close all

pkg load signal

amostragem = 1000;
nyquist = amostragem/2; 
dt = 1.0/amostragem;
t = [0:dt:1-dt]; % tmax = 1 s
s  = zeros( 1, amostragem );
f0 =  5.0;
f1 =  5.0;
f2 = 50.0;
k = (f2-f1); % dividir por tmax se tmax ~= 1
freq = k*t + f0;
w = 2.0*pi*freq;
fase = cumsum( w )*dt; % Fase = integral de w(t) 
s = cos( fase );
S = fft( s );
PSD = real( S.*conj( S ) );
PSD = PSD/max( PSD );
frequencias = [0:1:amostragem-1];

figure(1)
plot(t,s,'k','LineWidth',2)
grid on, box on
xlabel('Tempo (s)','FontSize',18)
ylabel('Amplitude','FontSize',18)

figure(2)
plot(frequencias,PSD,'k','LineWidth',2)
xlim([0,2*f2])
grid on, box on
xlabel('Frequência (Hz)','FontSize',18)
ylabel('Amplitude','FontSize',18) 

figure(3)
specgram(s, 256, amostragem, 256, 64);
xlabel('Tempo (s)','FontSize',18)
ylabel('Frequência (Hz)','FontSize',18)

