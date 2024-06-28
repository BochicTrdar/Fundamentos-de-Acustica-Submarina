% Fundamentos de Acústica Submarina

clear all, close all 

pkg load signal

amostragem = 2048;
h = zeros( 1, amostragem );
nyquist = 1024;
freqs = [0:1:amostragem-1];
dt = 1.0/amostragem;
t = [0:dt:1-dt];
D = 100.0;
Rkm = 20.0;
R = Rkm*1000.0;
c  = 1500.0;
cxc = c*c;
% Atraso temporal para não começar em t = 0:
t0 = R/c;
t0 = ( fix( t0/dt ) - 50 )*dt;

for m = 1:6

    H  = ones(1,amostragem) + 1i;
    w  = 2*pi*freqs;
    % Frequência de corte:
    f0m = (m - 0.5)*c/(2*D);
    w0m = 2*pi*f0m;
    % Quadrado do número de onda:
    kxk = ( w.^2 - w0m^2 )/cxc;
    % Procurar modos evanescentes:
    indexes = find( kxk < 0 );
    L = length( indexes );
    % Eliminar modos evanescentes: 
    kxk( indexes ) = 0.0;
    w(   indexes ) = 0.0;
    k = sqrt( kxk );
    H( indexes ) = 0.0;
    H( amostragem-indexes ) = 0.0;
    % Resposta impulsiva:
    fase = R*k - w*t0;
    H = H.*exp( -1i*fase );
    h = h + real( ifft( H ) );

endfor

figure(1)
plot(t,h)
xlabel('Tempo (s)','FontSize',18)
title('Resposta Impulsiva do canal h(t)','FontSize',18)
grid on, box on

figure(2)
specgram(h, 128, amostragem, 128, 100);
xlabel('Tempo (s)','FontSize',18)
ylabel('Frequência (Hz)','FontSize',18)

