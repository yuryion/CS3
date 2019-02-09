import numpy as np
import matplotlib.pyplot as plt
import math


def squares(ax, n, p, w):
    if n > 0:
        i1 = [0, 1, 2, 3, 4]

        q = (p + 350) * w
        q1 = (p - 350) * w
        
        q2 = p
        q2[i1, 1] = ((p[i1, 1] + 350) * w)
        q2[i1, 0] = ((p[i1, 0] - 350) * w)
        q3 = q2* -1 

        ax.plot(p[:, 0], p[:, 1], color = 'k')
        squares(ax, n - 1, q, w)
        squares(ax, n - 1, q1, w)
        squares(ax, n - 1, q2, w)
        squares(ax, n - 1, q3, w)
        
plt.close("all")
p = np.array([[200, 200], [-200, 200], [-200, -200], [200, -200], [200, 200]])
figSq, axSq = plt.subplots() 
squares(axSq, 4, p, .5)