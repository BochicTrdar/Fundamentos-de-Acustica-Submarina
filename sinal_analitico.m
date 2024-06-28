% Fundamentos de Acústica Submarina 

clear all, close all 

amostragem = 1000;
nyquist = 500;
dt = 1.0/amostragem;
t = [0:dt:1-dt];
x = 4*( t - 0.5 );
freq = 10;
w = 2*pi*freq;
s = exp( -x.*x ).*cos( w*t);
sinal_analitico = hilbert(s);
envelope = abs(sinal_analitico);
fase     = angle(sinal_analitico);
wi = diff( unwrap(fase) )./diff( t );
fi = wi/( 2*pi );

figure(1)
subplot(211)
plot(t,s,'k','LineWidth',2)
plot(t,envelope,'k--','LineWidth',2)
ylim([-1.1,1.1])
grid on, box on
subplot(212)
plot(t(1:end-1),fi,'k','LineWidth',2)
xlabel('t (s)','FontSize',18)
ylabel('f (Hz)','FontSize',18)
ylim([5,11])
grid on, box on

