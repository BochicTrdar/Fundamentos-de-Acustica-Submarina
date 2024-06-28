% Fundamentos de Acústica Submarina 

clear all, close all 

pkg load signal

nfreqs = 101;
fmin =  20;
fmax = 100;
f = linspace(fmin,fmax,nfreqs);
amostragem = 1000;
nyquist = 500;
dt = 1.0/amostragem;
t = [0:dt:1-dt];
w = 2*pi*f;
s = zeros(1,amostragem);

for i = 1:nfreqs
    s = s + cos( w(i)*(t-0.5) );
endfor

s = s/max( abs( s ) );

figure(1)
plot(t,s,'k','LineWidth',2)
grid on, box on
xlabel('Tempo (s)','FontSize',18)
ylabel('Amplitude','FontSize',18)

figure(2)
specgram(s, 256, amostragem, 256, 64);
xlabel('Tempo (s)','FontSize',18)
ylabel('Frequência (Hz)','FontSize',18)

