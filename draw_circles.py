import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        draw_circles(ax,n-1,center*[.95,0],radius*w,w) #the w value on the buttom has to match the value of center being multiplied
      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 100, np.array([100,0]), 100,.95)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')