% Fundamentos de Acústica Submarina 

clear all, close all 

freqkHz = 10.0;
freq    = freqkHz*1000;
cw      = 1500.0;
kw      = 2.0*pi*freq/cw;

% Fundo arenoso: 

arho    = 1.940;
vp      = 1.113;
dp      = 0.0115;

g2      = 3.25;
w2      = 0.000141;
g3      = 3.0;
w3      = 0.0004;

eta = -2.0;

thetai = 45; qi = thetai*pi/180;

nthetas = 90;
theta = linspace(1.0,90.0,nthetas);

nphis = 361;
phis  = linspace(-180,180,nphis);

Sb    = zeros(nphis,nthetas);
sigma = zeros(nphis,nthetas);

for j = 1:nphis
    phi = phis(j)*pi/180.0;
    for i = 1:nthetas
        q = theta(i)*pi/180.0;
        sigmav          = apl_bottom_bsigmav(qi,q,phi,g3,w3,kw,arho,vp,dp);
       [sigmakr,sigmapr]= apl_bottom_bsigma( qi,q,phi,g2,w2,kw,arho,vp,dp);
        sigmar = ( sigmakr^eta + sigmapr^eta )^( 1.0/eta );
        sigma(j,i)  = sigmav + sigmar;
        Sb(   j,i)  = 10*log10( sigmav + sigmar );
    endfor
endfor 

[R,Bearings] = meshgrid(theta,phis);

X = R.*cos( Bearings*pi/180.0 );
Y = R.*sin( Bearings*pi/180.0 );

colormap('jet');
figure(1)
pcolor(X,Y,Sb), shading interp, colorbar
xlim([-90,90])
axis('off')
hold on
thetan = [15:15:90];
n = length( thetan );
for i = 1:n
    s = [num2str( thetan(i) ) '^\circ' ];
    text(thetan(i),0,s)
endfor    
n = 18;
for i = 1:9
    s = [num2str( i*20 ) '^\circ' ];
    text(100*cos(i*2*pi/n),100*sin(i*2*pi/n),s)
endfor

for i = 1:9
    s = [num2str( -i*20 ) '^\circ' ];
    text(100*cos(i*2*pi/n),100*sin(-i*2*pi/n),s)
endfor
hold off
