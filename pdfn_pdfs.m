% Fundamentos de Acústica Submarina 

clear all, close all 

% Médias e variâncias do ruído e do sinal
mun    = 0.0;
sigman = 0.6;
mus    = 1.0;
sigmas = 0.5;
xt = 0.2;

n = 1000;

x = linspace(-2,2,n);
y = (x-mun)/sigman;
pdfn = 1/( sqrt(2*pi)*sigman )*exp( -0.5*y.*y );
y = (x-mus)/sigmas;
pdfs = 1/( sqrt(2*pi)*sigmas )*exp( -0.5*y.*y );
yaux = zeros(1,n);

indexes = find( x > xt ); 
xf  =    x(indexes);
yf  = pdfn(indexes);
yfs = pdfs(indexes);
figure(1)
subplot(211)
plot(x,pdfn,'k','LineWidth',2), hold on
fill([xf(1),xf,xf(end)],[0,yf,0],0.9)
hold off
text(0.3, 0.2, 'p(FA)', 'FontSize',22)
title('PDF do ruído','FontSize',18)
xlim([-2,2])
ylim([0,1])
grid on, box on
subplot(212)
plot(x,pdfs,'k','LineWidth',2), hold on
fill([xf(1),xf,xf(end)],[0,yfs,0],0.8)
hold off
text(1.0, 0.2, 'p(D)', 'FontSize',22)
title('PDF do sinal','FontSize',18)
xlim([-2,2])
ylim([0,1])
grid on, box on
xlabel('Amplitude do sinal','FontSize',18)

