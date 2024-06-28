% Fundamentos de Acústica Submarina 

clear all, close all 

a = -1.0;
b =  1.0;
n = 1000;
u = (b-a)*rand(1,n)-b;

figure(1)
hist(u, bins=20,normed=1,color='w','LineWidth',2)

