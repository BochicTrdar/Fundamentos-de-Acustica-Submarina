% Fundamentos de Acústica Submarina 

clear all, close all 

D    =  100.0;
rho1 =    1.0;
rho2 =    1.5;
c1   = 1500.0;
c2   = 1600.0;
nfreqs = 101;
fmin = 11.0;
fmax = 150.0;
freqs = linspace(fmin,fmax,nfreqs);
w = 2*pi*freqs;

k1 = zeros(1,nfreqs);
k2 = zeros(1,nfreqs) + nan;
k3 = zeros(1,nfreqs) + nan;
k4 = zeros(1,nfreqs) + nan;

mc2 = nfreqs;
mc3 = nfreqs;
mc4 = nfreqs;

for i = 1:nfreqs

    wi = 2*pi*freqs(i);
    kpek = kpekeris(c1,rho1,c2,rho2,D,freqs(i));
    k1(i) = kpek(1);
    nk = length( kpek );
    
    if nk == 2
       k2(i) = kpek(2);
       mc2 = min([i,mc2]);
    endif
    if nk == 3
       k2(i) = kpek(2);
       k3(i) = kpek(3);
       mc3 = min([i,mc3]);
    endif
    if nk >= 4
       k2(i) = kpek(2);
       k3(i) = kpek(3);
       k4(i) = kpek(4);
       mc4 = min([i,mc4]);
    endif   

endfor

dw = diff( w );
vf1 = w./k1; vg1 = dw./diff(k1); vg1 = [vg1,vg1(end)];
vf2 = w./k2; vg2 = dw./diff(k2); vg2 = [vg2,vg2(end)];
vf3 = w./k3; vg3 = dw./diff(k3); vg3 = [vg3,vg3(end)];
vf4 = w./k4; vg4 = dw./diff(k4); vg4 = [vg4,vg4(end)];

figure(1)
plot(freqs,vf1,'k'  ,'LineWidth',2), hold on
plot(freqs,vg1,'k--','LineWidth',2)
plot(freqs,vf2,'k'  ,'LineWidth',2)
plot(freqs,vg2,'k--','LineWidth',2)
plot(freqs,vf3,'k'  ,'LineWidth',2)
plot(freqs,vg3,'k--','LineWidth',2)
plot(freqs,vf4,'k'  ,'LineWidth',2)
plot(freqs,vg4,'k--','LineWidth',2)
text(5,vf1(1)-7.5,'1','FontSize',16)
text(5,vg1(1)-7.5,'1','FontSize',16)
text(freqs(mc2-3),vf2(mc2)-10,'2','FontSize',16)
text(freqs(mc2-3),vg2(mc2)-10,'2','FontSize',16)
text(freqs(mc3-3),vf3(mc3)-10,'3','FontSize',16)
text(freqs(mc3-3),vg3(mc3)-10,'3','FontSize',16)
text(freqs(mc4-3),vf4(mc4)-10,'4','FontSize',16)
text(freqs(mc4-3),vg4(mc4)-10,'4','FontSize',16)
xlabel('Frequência (Hz)','FontSize',18)
ylabel('Velocidade (m/s)','FontSize',18)
xlim([0,fmax])
grid on, box on
hold off

