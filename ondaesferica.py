# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *
from matplotlib import cm
from matplotlib import animation
from mpl_toolkits.mplot3d.axes3d import *

def data_gen(framenumber, p, plot):
    f = k*R - w*t[framenumber]
    p = real( exp( 1j*f )/R )
    ax.clear()
    plot = ax.plot_wireframe(X, Y, p, color='b')
    xlabel(r'$X$',fontsize=18)
    ylabel(r'$Y$',fontsize=18)
    ax.set_zlabel(r'$p_h(r,t)$',fontsize=18)
    ax.set_zlim(-0.2,0.2)
    return plot,

quadros  =  36
periodos =   6
nx       =  51

freq  =   50.0; T = 1.0/freq; w = 2.0*pi*freq
c     = 1500.0
k     = w/c
# Comprimento de onda:
L     = 2.0*pi/k
tmin  =  0
tmax  =  T*periodos
xmax  = 3.0*L 
x = linspace(-xmax,xmax,nx)
y = linspace(-xmax,xmax,nx)

X,Y = meshgrid(x,y) 
R = sqrt( X*X + Y*Y )
R[24:26,24:26] = NaN # evitar R = 0...

t = linspace(tmin,tmax,quadros)

# Definir parâmetros iniciais:
f = k*R - w*t[0]
p = real( exp( 1j*f )/R )
fig = figure(1)
ax = Axes3D(fig)
plot = ax.plot_wireframe(X, Y, p)

# Animação:
animacao = animation.FuncAnimation(fig, 
data_gen, fargs=(p, plot),
frames=quadros,interval=1, blit=False)

show()

