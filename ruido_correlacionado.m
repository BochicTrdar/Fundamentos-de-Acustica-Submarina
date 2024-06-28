% Fundamentos de Acústica Submarina 

% Geração de ruído correlado: 
% X => vector gaussiano com N = 20  
% matriz de covariância: 
% E[Xi Xj] = e^|i-j|/5, i,j = 1,...,20. 
% Decomposição de Cholesky => Y = B X

clear all, close all 

N = 20;
n = 1000;
X = randn(N,n);
Y = zeros(N,n);
C = zeros(N,N);

for i = 1:N
    for j = 1:N
        C(i,j) = exp(-abs(i-j)/5);
    endfor
endfor

B = chol(C);

Y = B*X;

Ce = cov( Y' );

colormap('jet')

figure(1)
pcolor(C), shading interp, colorbar
xlabel('i','FontSize',18)
ylabel('j','FontSize',18)

figure(2)
pcolor(Ce), shading interp, colorbar
xlabel('i','FontSize',18)
ylabel('j','FontSize',18)

