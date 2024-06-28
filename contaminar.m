% Fundamentos de Acústica Submarina

clear all, close all 

SNRdB = 10;
SNR   = 10^( SNRdB/10.0 );

otitulo = [ 's(t) + n(t), SNR = ' ];
otitulo = [ otitulo num2str(SNRdB) ' dB'];
freq       =    8; % Frequência do sinal
amostragem = 1000; % Frequência de amostragem
nyquist    = amostragem/2; % Frequência de Nyquist
frequencias = linspace(0,amostragem,amostragem);
dt = 1.0/amostragem;
t = [0:dt:1-dt];
w = 2*pi*freq;
s = cos( w*t ); % Tom

Ps = var( s );

sigma = sqrt( Ps/SNR );

% Contaminação do sinal:
r = s + sigma*randn(1,amostragem);

figure(1)
subplot(211)
plot(t,s,'k','LineWidth',2)
ylim([-1.5,1.5])
grid on, box on
title('s(t)','FontSize',18)
subplot(212)
plot(t,r,'k')
ylim([-1.5,1.5])
grid on, box on
title(otitulo,'FontSize',18)
xlabel('Tempo (s)','FontSize',18)

