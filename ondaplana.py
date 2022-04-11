# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *
from matplotlib import animation
from mpl_toolkits.mplot3d.axes3d import *

def data_gen(framenumber, p, plot):
    wxt = w*t[framenumber]
    p = real( exp( 1j*( kx*X + ky*Y - wxt ) ) )
    ax.clear()
    plot = ax.plot_wireframe(X, Y, p, color='b')
    xlabel(r'$X$',fontsize=18)
    ylabel(r'$Y$',fontsize=18)
    ax.set_zlabel(r'$p_h(x,y,t)$',fontsize=18)
    return plot,

quadros  =  36
periodos =   6
nx       =  51

freq  =   50.0; T = 1.0/freq; w = 2.0*pi*freq
c     = 1500.0
k     = w/c
# Ângulo de propagação (mudar e ver efeito):
phi   = 0.0
# Componentes do número de onda:
kx    = k*cos( phi*pi/180.0 )
ky    = k*sin( phi*pi/180.0 )
# Comprimento de onda:
L     = 2.0*pi/k
tmin  =  0
tmax  =  T*periodos
xmax  = 3.0*L 
x = linspace(-xmax,xmax,nx)
y = linspace(-xmax,xmax,nx)

X,Y = meshgrid(x,y);

t = linspace(tmin,tmax,quadros)

# Definir parâmetros iniciais:
p = real( exp( 1j*( kx*X + ky*Y - w*t[0] ) ) )
fig = figure(1)
ax = Axes3D(fig)
plot = ax.plot_wireframe(X, Y, p)

# Animação:
animacao = animation.FuncAnimation(fig, data_gen, fargs=(p, plot),
frames=quadros,interval=1, blit=False)

show()

