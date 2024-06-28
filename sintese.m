% Fundamentos de Acústica Submarina 

clear all, close all 

fmin =  20;
fmax = 100;
amostragem = 1000; 
nyquist = 500;
frequencias = [0:1:amostragem-1];
w = 2*pi*frequencias;
S = zeros(1,amostragem);
dt = 1.0/amostragem;
t = [0:dt:1-dt];
t0 = 0.5;
t0 = dt*fix( t0/dt );

fpulse = [fmin:1:fmax];

L = length( fpulse );

for i  = 1:L 

    fi = fix( fpulse(i) );
    S(fi)            = ( 1.0 + 1i*0 )*nyquist/L;
    S(amostragem-fi) = ( 1.0 + 1i*0 )*nyquist/L;

endfor

S = S.*exp( -1i*w*t0 );
s = real( ifft( S ) );

figure(1)
plot(frequencias,abs(S),'k','LineWidth',2)
xlabel('Frequência (Hz)','FontSize',18)
ylabel('Amplitude','FontSize',18)
ylim([0,1.1])
grid on, box on

figure(2)
plot(t,s,'k','LineWidth',2)
xlabel('Tempo (s)','FontSize',18)
ylabel('Amplitude','FontSize',18)
grid on, box on
