% Fundamentos de Acústica Submarina 

clear all, close all 

pkg load signal

f1 =  5;
f2 = 50;
f3 = 75;
amostragem = 500; 
nyquist = 250;
dt = 1.0/amostragem;
t = [0:dt:1-dt];
w1 = 2*pi*f1;
w2 = 2*pi*f2;
w3 = 2*pi*f3;
s = cos( w1*t ) + cos( w2*t ) + cos( w3*t );
S = fft(s);
Saux = fft(s);

P = real( S.*conj( S ) );
P = P/max( P );
frequencias = [0:1:amostragem-1];
% Filtro improvisado: 
% remover componentes não desejadas:
f = abs( frequencias - f1 );
[themin,i1] = min( f );
f = abs( frequencias - amostragem + f1 );
[themin,i2] = min( f );
Saux(i1+10:i2-10) = 0;
sf = real( ifft(Saux) );

figure(1)
plot(t,s,'k','LineWidth',2)
grid on, box on
xlabel('Tempo (s)','FontSize',18)
ylabel('Amplitude','FontSize',18)

figure(2)
plot(frequencias,P,'k','LineWidth',2)
xlim([0,f3+25])
grid on, box on
xlabel('Frequência (Hz)','FontSize',18)
ylabel('Amplitude','FontSize',18)

figure(3)
specgram(s, 256, amostragem, 256, 64);
xlabel('Tempo (s)','FontSize',18)
ylabel('Frequência (Hz)','FontSize',18)

figure(4)
plot(t,sf,'k','LineWidth',2)
xlabel('Tempo (s)','FontSize',18)
ylabel('Amplitude','FontSize',18)
grid on, box on

