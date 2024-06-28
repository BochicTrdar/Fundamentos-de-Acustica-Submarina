% Fundamentos de Acústica Submarina 

clear all, close all 

amostragem = 1000;
nyquist = 500;
dt = 1.0/amostragem;
t = [0:dt:1-dt];
freq = 55;
w = 2*pi*freq;
s = cos(w*t);
stau = zeros( 1, amostragem );
tau = 0.19;
a = 0.5;
n = fix( tau/dt );
stau(n:end) = s(1:amostragem-n+1); % sinal atrasado
p = s + a*stau; % sinal mais eco
P = fft( p );
Cc = ifft( log( P ) ); % Cepstrum complexo
%Cr = ifft( log( abs( P ) ) ) % Cepstrum "real"

figure(1)
subplot(211)
plot(t,p,'k','LineWidth',2)
xlabel('Tempo (s)')
ylabel('p(t)')
grid on, box on
subplot(212)
plot(t,abs(Cc),'k','LineWidth',2)
xlabel('Quefrência (s)')
ylabel('|C_c|')
grid on, box on
%subplot(212)
%plot(t,real(Cr),'k','LineWidth',2)
%xlabel('Quefrência (s)')
%ylabel('Re$(C_r)$')
%grid on, box on


