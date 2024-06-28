% Fundamentos de Acústica Submarina 

clear all, close all 

% Médias e variâncias do ruí­do e do sinal
mun    = 0.0;
sigman = 0.5;
mus    = 1.0;
sigmas = 0.5;

n = 1000;

% Índice de detecção:
a = mus - mun;
b = sigmas^2 + sigman^2;
d = a^2/( 0.5*b );
d

x = linspace(-2,2,n);
y = (x-mun)/sigman;
pdfn = 1/( sqrt(2*pi)*sigman )*exp( -0.5*y.*y );
y = (x-mus)/sigmas;
pdfs = 1/( sqrt(2*pi)*sigmas )*exp( -0.5*y.*y );

dx = x(2)-x(1);
pFA = zeros( 1,n );
pD  = zeros( 1,n );

for i = 1:n
    pFA(i) = sum( pdfn(i:n) );
    pD( i) = sum( pdfs(i:n) );
endfor

pFA = dx*pFA;
pD  = dx*pD;

figure(1)
plot(pFA,pD,'k','LineWidth',2)
title('ROC do sistema de detecção','FontSize',18)
xlabel('p(FA)','FontSize',18)
ylabel('p(D)' ,'FontSize',18)
xlim([0,1])
ylim([0,1])
grid on, box on

