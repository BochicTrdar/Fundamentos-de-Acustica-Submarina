# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

def kpekeris(c1=None,rho1=None,
             c2=None,rho2=None,
             D=None,freq=None):
    
    kp = []

    w = 2*pi*freq
    k1 = w/c1
    k2 = w/c2

    nk = 1001
    k = linspace(k1,k2,nk)
    kxk = k*k

    r1 = sqrt( k1*k1 - kxk )
    r2 = sqrt( kxk - k2*k2 ) 

    s1 = sin( r1*D )
    c1 = cos( r1*D )

    f = s1*r2/rho2 + c1*r1/rho1

    for i in range(nk-1): 
   
        x1 = k[ i ]
        x2 = k[i+1]
        y1 = f[ i ]
        y2 = f[i+1]
        p = y1*y2
        x3  = (x1*y2-x2*y1)/(y2-y1)
     
        if p < 0:

           kp = append(kp,x3)

    return kp

D    =  100.0
rho1 =    1.0
rho2 =    1.5
c1   = 1500.0
c2   = 1600.0
nfreqs = 101
fmin = 11.0
fmax = 150.0
freqs = linspace(fmin,fmax,nfreqs)
w = 2*pi*freqs

k1 = zeros(nfreqs)
k2 = zeros(nfreqs) + nan
k3 = zeros(nfreqs) + nan
k4 = zeros(nfreqs) + nan

mc2 = nfreqs
mc3 = nfreqs
mc4 = nfreqs

for i in range(nfreqs):
    wi = 2*pi*freqs[i]
    kpek = kpekeris(c1,rho1,c2,rho2,D,freqs[i])
    k1[i] = kpek[0]
    nk = kpek.size
    if nk == 2:
       k2[i] = kpek[1]
       mc2 = min([i,mc2])
    if nk == 3:
       k2[i] = kpek[1]
       k3[i] = kpek[2]
       mc3 = min([i,mc3])
    if nk >= 4:
       k2[i] = kpek[1]
       k3[i] = kpek[2]
       k4[i] = kpek[3]
       mc4 = min([i,mc4])

dw = diff( w )
vf1 = w/k1
vg1 = dw/diff(k1); vg1 = append(vg1,vg1[-1])
vf2 = w/k2
vg2 = dw/diff(k2); vg2 = append(vg2,vg2[-1])
vf3 = w/k3
vg3 = dw/diff(k3); vg3 = append(vg3,vg3[-1])
vf4 = w/k4
vg4 = dw/diff(k4); vg4 = append(vg4,vg4[-1])

figure(1)
plot(freqs,vf1,'k'  ,linewidth=2)
plot(freqs,vg1,'k--',linewidth=2)
plot(freqs,vf2,'k'  ,linewidth=2)
plot(freqs,vg2,'k--',linewidth=2)
plot(freqs,vf3,'k'  ,linewidth=2)
plot(freqs,vg3,'k--',linewidth=2)
plot(freqs,vf4,'k'  ,linewidth=2)
plot(freqs,vg4,'k--',linewidth=2)
text(5,vf1[0]-7.5,'1',fontsize=16)
text(5,vg1[0]-7.5,'1',fontsize=16)
text(freqs[mc2-3],vf2[mc2]-10,'2',fontsize=16)
text(freqs[mc2-3],vg2[mc2]-10,'2',fontsize=16)
text(freqs[mc3-3],vf3[mc3]-10,'3',fontsize=16)
text(freqs[mc3-3],vg3[mc3]-10,'3',fontsize=16)
text(freqs[mc4-3],vf4[mc4]-10,'4',fontsize=16)
text(freqs[mc4-3],vg4[mc4]-10,'4',fontsize=16)
xlabel(u'Frequência (Hz)',fontsize=18)
ylabel('Velocidade (m/s)',fontsize=18)
xlim(0,fmax)
grid(True)

show()

