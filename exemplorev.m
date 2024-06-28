% Fundamentos de Acústica Submarina 

clear all, close all 

% Parâmetros:
SL  = 0;
phi = 2*pi;
tau = 1; % Duração do pulso
freq   = 3000;
Dmax   = 1000;
zs     = 500.0;
cw    = 1500.0;

nr = 501;
rmin =  100.0;
rmax = 1000.0;
r = linspace(rmin,rmax,nr);

s1 = 0.016;
s2 = 0.002;
sigma = linspace(s1,s2,nr); % Idealizado

trev  = ones(1,nr);
RL    = ones(1,nr);

for i = 1:nr

    ri = sqrt(r(i)*r(i) + (Dmax-zs)^2.0);
    TL = 10*log10( abs( ri ) );
    A = 0.5*cw*tau*pi*ri;
    RLb = 10*log10(A);
    RL(i) = SL - 2*TL + 10*log10( sigma(i) ) + RLb;
    trev(i) = 2*ri/cw;

endfor 

figure(1)
plot(trev,RL,'k','LineWidth',2)
xlabel('Tempo (s)','FontSize',18)
ylabel('RL (dB)'  ,'FontSize',18)
grid on, box on

