% Fundamentos de Acústica Submarina 

clear all, close all

pkg load signal

tmin     = 0.0;
tmax     = 1.4;
amostragem = 10000;
nyquist = 5000;
dt       = 1.0/amostragem;
freq     = 40;
w        = 2*pi*freq; T = 1.0/freq;
duracao_bit  = 0.2;
t = [0:dt:duracao_bit-dt]; 
nbits    = fix(tmax/duracao_bit);
sr = rand( 1,nbits );
sequencia = round( rand(1,nbits) );
asequencia = num2str( sequencia );

um = sin( w*t );
s = [];

for i = 1:nbits
    if sequencia(i) == 1
      s = [s,um]; 
    else
      s = [s,-um];
    endif
endfor

t = linspace(0,tmax-dt,length(s));

[PSD,w] = periodogram(s,[],2018,amostragem); % periodograma
[themax,imax] = max( PSD );

frequencias = w*nyquist;

figure(1)
plot(t,s,'k','LineWidth',2)
grid on, box on
xlabel("Tempo (s)",'FontSize',18)
ylabel("Amplitude",'FontSize',18) 
title( asequencia )

figure(2)
plot(frequencias,PSD,'k','LineWidth',2)
xlim([0,2*frequencias(imax)])
grid on, box on
xlabel("Frequência (Hz)",'FontSize',18)
ylabel("Amplitude",'FontSize',18)

[S, f, t] = specgram(s);

figure(3)
imagesc(t, f, log(abs(S)));
xlabel("Tempo (s)",'FontSize',18)
ylabel("Frequência (Hz)",'FontSize',18)

