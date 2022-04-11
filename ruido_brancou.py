# coding=utf-8
from numpy import * 
from matplotlib.pyplot import *

a = -1.0
b =  1.0
n = 1000 
u = random.uniform(a,b,n)

figure(1)
hist(u, bins=20,normed=1,color='w',linewidth=2)
show()
