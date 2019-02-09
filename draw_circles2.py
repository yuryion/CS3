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
        draw_circles(ax,n-1,center*[1,1],radius/3,w)
        draw_circles(ax,n-1,center*[1,1.667],radius/3,w)
        #print(center)
        draw_circles(ax,n-1,center*[1,.333],radius/3,w)
        #print(center)
        draw_circles(ax,n-1,center*[1.667,1],radius/3,w)
        #print(center)
        draw_circles(ax,n-1,center*[.333,1],radius/3,w)
        #print(center)
        
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 2, np.array([100,100]), 100,.5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('circles.png')