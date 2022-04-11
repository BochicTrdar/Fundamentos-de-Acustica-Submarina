# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *
from matplotlib import animation

def data_gen(framenumber, p, plotxp):
    p = sin( k*x - w*t[framenumber] )
    ax.clear()
    nx = x.size
    for j in range(nx):
        plot( (x[j]+p[j])*ones(nx),y,'ko')
    xlabel(r'$X$',fontsize=18)
    ylabel(r'$Y$',fontsize=18)
    xlim(-3*pi,3*pi)
    grid(True)
    return plotxp

quadros = 101
nx    = 51
ny    = 51
w     = 1.0
k     = 1.0
xmax  = 3.0*pi
ymax  = 1.0
t     = linspace(0.0,10.0*pi,quadros)
x     = linspace(-xmax,xmax,nx)
y     = linspace(-ymax,ymax,ny)

# Definir parâmetros iniciais:
p = sin( k*x - w*t[0] )
fig = figure(1)
ax = fig.gca()
plotxp = plot( x+p,y,'ko')

# Animação:
animacao = animation.FuncAnimation(fig, 
data_gen, fargs=(p, plotxp),
frames=quadros,interval=1, blit=False)

show()
