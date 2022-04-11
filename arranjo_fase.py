# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *
from matplotlib import animation
from mpl_toolkits.mplot3d.axes3d import *

def data_gen(framenumber, p, plot):
    XB = 0.5*k*Larray*sin( THETA-theta0[framenumber] )
    p = sinc( XB/pi )*real( o )
    plot = pcolormesh(X, Y, p, color='b')
    return plot,

quadros  = 36
periodos =  6
nx       = 51

freq  =  100.0; T = 1.0/freq; w = 2.0*pi*freq
c     = 1500.0
k     = w/c
# Comprimento de onda:
L     = 2.0*pi/k
# Comprimento da antena: 
Larray = 2*L
tmin  =  0
tmax  =  T*periodos
xmax  = 3.0*L 
x = linspace(-xmax,xmax,nx)
y = linspace(-xmax,xmax,nx)

X,Y = meshgrid(x,y);
THETA = arctan2(Y,X)
R  = sqrt( X*X + Y*Y )
o = exp( 1j*k*R ) # Onda circular

theta0 = linspace(0,pi,quadros)
XB = 0.5*k*Larray*sin( THETA-theta0[0] )

# Definir parâmetros iniciais:
p = sinc( XB/pi )*real( o )
fig = figure(1)
ax = fig.gca
plot = pcolormesh(X, Y, p)

# Animação:
animacao = animation.FuncAnimation(fig, 
data_gen, fargs=(p, plot),
frames=quadros,interval=1, blit=False)

show()

