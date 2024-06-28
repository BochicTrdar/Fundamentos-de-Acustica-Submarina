% Fundamentos de Acústica Submarina 

clear all, close all 

amostragem = 1000;
tmax = 10.0;
nyquist = 500;
w1 = 2*pi*nyquist/50;
dt = 1.0/amostragem;
t = [0:dt:tmax-dt];
s = zeros( 1, length(t) );
s(1:nyquist) = 1.0;
sn =  fliplr( s );
tn = -fliplr( t );
f = linspace(-amostragem,amostragem,2*length(t));
w = 2*pi*f;
S = real( fft(s) );
Sn =  fliplr( S );
snp = [sn,s];
tnp = [tn,t];
Snp = [Sn,S];
Snp = Snp/max( abs( Snp ) );

figure(1)
subplot(211)
plot(tnp,snp,'k','LineWidth',2)
xlabel('t (s)')
ylabel('\Pi(t)')
xlim([-1,1])
ylim([-0.1,1.1])
grid on, box on
subplot(212)
plot(w,Snp,'k','LineWidth',2)
xlabel('\omega (rad/s)')
ylabel('FT[\Pi(t)]')
xlim([-w1,w1])
ylim([-0.25,1.1])
grid on, box on

