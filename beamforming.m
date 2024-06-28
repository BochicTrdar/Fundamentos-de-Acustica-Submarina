% Fundamentos de Acústica Submarina

clear all, close all

ntheta = 181;
theta = linspace(-90,90,ntheta);
thetar = theta*pi/180;
nphi = 361;
phi = linspace(-180,180,nphi);
phir = phi*pi/180;

thetas  = 40;
thetasr = thetas*pi/180;
phis    = 20;
phisr   = phis*pi/180;

nsensors = 11;
c    = 1500;
freq =  500; w0 = 2*pi*freq;
d = [0, 0, 1]; % Antena vertical

yp = zeros(1,nsensors) + 1i;
ep = zeros(1,nsensors) + 1i;
B  = zeros(ntheta,nphi);

kx = cos(phisr)*cos(thetasr); 
ky = sin(phisr)*cos(thetasr);
kz =            sin(thetasr);
ks = w0/c*[kx,ky,kz];

for l = 1:nsensors
    rl = l*d;
    yp(l) = exp( -1i*dot(ks,rl) );
endfor

yp = yp/norm( yp );

for j = 1:nphi

    phij = phir(j);

    for i = 1:ntheta

         thetai = thetar(i);
         kx = cos(phij)*cos(thetai); 
         ky = sin(phij)*cos(thetai);
         kz =           sin(thetai);
         k  = w0/c*[kx,ky,kz];

 	 for l = 1:nsensors

 	     rl = l*d;
 	     ep(l) = exp( 1i*dot(k,rl) );
 	     
	 endfor
	 
	 ep = ep/norm( ep );
	
	 B(i,j) = abs( dot(yp,ep) );
      
    endfor

endfor

colormap('jet')

figure(1)
pcolor(phi,theta,B), shading interp, colorbar
xlim([-180,180])
ylim([-90,90])
xlabel('\phi (graus)'  ,'FontSize',18)
ylabel('\theta (graus)','FontSize',18)

