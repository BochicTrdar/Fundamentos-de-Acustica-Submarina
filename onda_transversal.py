# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *
from matplotlib import animation

def data_gen(framenumber, p, plotxp):
    p = sin( k*x - w*t[framenumber] )
    ax.clear()
    plot(x,p,'ko')
    stem(x,p,'k--')
    xlabel(r'$X$',fontsize=18)
    ylabel(r'$Y$',fontsize=18)
    grid(True)
    return plotxp

quadros = 101
nx    = 21
w     = 1.0
k     = 1.0
xmax  = 2.0*pi
t     = linspace(0.0,20.0*pi,quadros)
x     = linspace(0.0,xmax,nx)

# Definir parâmetros iniciais:
p = sin( k*x - w*t[0] )
fig = figure(1)
ax = fig.gca()
plotxp = plot(x,p,'ko')

# Animação:
animacao = animation.FuncAnimation(fig, 
data_gen, fargs=(p, plotxp),
frames=quadros,interval=1, blit=False)

show()
