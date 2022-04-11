# coding=utf-8
from numpy import * 
from scipy import * 
from matplotlib.pyplot import *
from matplotlib import animation

def data_gen(framenumber, p, plotxp):
    p1 = exp( 1j*( k1*x - w1*t[framenumber] ) )
    p2 = exp( 1j*( k2*x - w2*t[framenumber] ) )
    p = 0.5*real( p1 + p2 )
    ax.clear()
    plot(x,p)
    xlabel(r'$x$',fontsize=18)
    ylabel(r'$p(x,t)$',fontsize=18)
    grid(True)
    return plotxp,

quadros  = 101
periodos =  50
nx       = 201

v  = 1500.0 # vfase
# Descomentar e executar a animação: 
c  = v # vgrupo = vfase
#c = 0 # vgrupo = 0
#c = -250 # vgrupo < 0
f1  = 50.0
w1 = 2.0*pi*f1
k1 = w1/v; dk = k1/10.0
k2 = k1 + dk
dw = c*dk
w2 = w1 + dw
f2 = w2/( 2.0*pi )
T1 = 1.0/f1
T2 = 1.0/f2

print(v,c)

L1 = 2.0*pi/k1
L2 = 2.0*pi/k2

tmin = 0.0
tmax = max([T1,T2])*periodos

xmax = 10.0*max([L1,L2]) 

x = linspace(-xmax,xmax,nx)
t = linspace(tmin,tmax,quadros)

# Definir parâmetros iniciais:
p1 = exp( 1j*( k1*x - w1*t[0] ) )
p2 = exp( 1j*( k2*x - w2*t[0] ) )
p = 0.5*real( p1 + p2 )
fig = figure(1)
ax = fig.gca()
plotxp = plot(x,p)

# Animação:
animacao = animation.FuncAnimation(fig, 
data_gen, fargs=(p, plotxp),
frames=quadros,interval=1, blit=False)

show()    

