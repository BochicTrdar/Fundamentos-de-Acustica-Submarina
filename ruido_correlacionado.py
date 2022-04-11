# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *

# Geração de ruído correlado: 
# X => vector gaussiano com N = 20  
# matriz de covariância: 
# E[Xi Xj] = e^|i-j|/5, i,j = 1,...,20. 
# Decomposição de Cholesky => Y = B X

N = 20
I = range(1,N+1)
n = 1000
X = random.randn(N,n)
Y = zeros((N,n))
C = zeros((N,N))

for i in range(N):
    for j in range(N):
        C[i,j] = exp(-abs(i-j)/5)

B = linalg.cholesky(C).T

for i in range(n):
    Y[:,i] = B.dot( X[:,i] )

Ce = cov( Y )

figure(1)
imshow(C, cmap='Greys',extent=[1,N,1,N],
aspect='auto',origin='lower')
xlabel(r'$i$',fontsize=18)
ylabel(r'$j$',fontsize=18)

figure(2)
imshow(Ce, cmap='Greys',extent=[1,N,1,N],
aspect='auto',origin='lower')
xlabel(r'$i$',fontsize=18)
ylabel(r'$j$',fontsize=18)

show()

