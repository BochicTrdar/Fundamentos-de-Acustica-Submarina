# coding=utf-8
from numpy import * 
from matplotlib.pyplot import *

mu    = 0.0
sigma = 1.0
n = 1000 
g = sigma*random.randn(n) + mu

figure(1)
hist(g, bins=20,normed=1,color='w',linewidth=2)
show()
