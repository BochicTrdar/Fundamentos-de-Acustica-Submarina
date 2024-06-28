% Fundamentos de Acústica Submarina 

clear all, close all 

mu    = 0.0;
sigma = 1.0;
n = 1000;
g = sigma*randn(1,n) + mu;

figure(1)
hist(g, bins=20,normed=1,color='w','LineWidth',2)

