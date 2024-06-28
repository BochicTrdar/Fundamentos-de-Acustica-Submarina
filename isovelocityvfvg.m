% Fundamentos de Acústica Submarina

clear all, close all

M = 5;
m = 1:M;
n = 101;
fmin = 100.0;
fmax = 200.0;
freqs = linspace(fmin,fmax,n);
w = 2*pi*freqs;
wxw = w.*w;
c = 1500.0; cxc = c*c;
D = 100.0;

khm = zeros(1,n);

figure(1), hold on
for i = 1:M

    km = ( m(i) - 0.5 )*pi/D;
    kmxkm = km.*km;
    khm = sqrt( wxw/cxc - kmxkm );
    vf = w./khm;
    vg = cxc*khm./w;
    them = num2str( i+1 );
    text(freqs(21),vf(21)+1.0,them,'FontSize',16)
    text(freqs(21),vg(21)-7.0,them,'FontSize',16)
    plot(freqs,vf,'k','LineWidth',2)
    plot(freqs,vg,'k--','LineWidth',2)

endfor
hold off
xlabel('Frequência (Hz)','FontSize',18)
ylabel('Velocidade (m/s)','FontSize',18)
grid on, box on



