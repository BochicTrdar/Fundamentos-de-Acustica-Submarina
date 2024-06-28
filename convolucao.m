% Fundamentos de Acústica Submarina

clear all, close all 

amostragem = 1000;
dt = 1.0/amostragem;
t = [0:dt:1-dt];

s = zeros(1,amostragem);
s(100:199) =  1; 
s(200:299) = -1;
h = exp( -((t-0.2)/0.02).^2 ) + 0.75*exp( -((t-0.36)/0.02).^2 );

S = fft( s );
H = fft( h );
P = H.*S;
p = real( ifft(P) );
p = p/max( abs( p ) );

figure(1)
subplot(311)
plot(t,s,'k','LineWidth',2)
title('s(t)','FontSize',18)
ylim([-1.1,1.1])
grid on, box on
subplot(312)
plot(t,h,'k','LineWidth',2)
title('h(t)','FontSize',18)
ylim([0,1.1])
grid on, box on
subplot(313)
plot(t,p,'k','LineWidth',2)
title('p(t)','FontSize',18)
ylim([-1.1,1.1]) 
grid on, box on
xlabel('Tempo (s)','FontSize',18)


