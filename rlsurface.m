% Fundamentos de Acústica Submarina

clear all, close all 

freqkHz = 25;
freq = freqkHz*1000;

nthetas = 180;
thetas  = linspace(1,90,nthetas);
q  = thetas*pi/180.0;
qi = 0.5*pi - q;
secg = 1.0./cos( qi );
p1 = secg.^4.0;

U = [3.0:11.0]; % Vento
U = [U,15.0];
lU = length( U );

qf    = zeros(1,lU);
sigma = zeros(lU, nthetas);

for i = 1:lU
    sxs = 0.034;
    Ui = U(i);
    if ( Ui >= 1.0 )
       sxs = 4.6e-3*log( 2.1*Ui*Ui );
    endif
    p2 = 4.0*pi*sxs;
    sf90 = 1.0/p2;
    x = tan(qi).^2.0/sxs;
    sf = p1/p2.*exp( -x );
    threshold = sf90/( 10^1.5 );
    [themax,imax] = find( sf >= threshold );
    qf(i) = q(imax(1));
    for j = 1:nthetas
        sb = apl_bub_sigma(q(j),freq,U(i));
        sr = apl_surface_sigma(q(j),freq,U(i),qf(i));
        sigma(i,j) = sr + sb;
    endfor
endfor

SS = 10*log10( sigma );

figure(1), hold on
for i = 1:lU
    plot(thetas,SS(i,:),'k','LineWidth',2)
    thetext = num2str( U(i) );
    if i < 5
       text(thetas(45),SS(i,45)+1,thetext)
    elseif i == 5
       text(thetas(90),SS(i,90)+1,thetext)
    elseif i == 6
       text(thetas(90),SS(i,90)+4,thetext)
    elseif i == 7
       text(thetas(18),SS(i,18)+3,thetext)
    else
       text(thetas(40),SS(i,40)+0.75,thetext)
    endif
endfor
hold off
xlabel('Ângulo Rasante (graus)','FontSize',18)
ylabel('SS (dB)','FontSize',18)
ylim([-60,10])
grid on, box on

