import matplotlib.pyplot as plt
import numpy as np

def trees(ax, n, points, w):
    if n > 0:

        i1 = [0, 1, 2]
        newpointL = points -800
        newpointL[i1, 0] = newpointL[i1, 0] * w
        newpointR = points
        newpointR[i1, 0] = ((newpointR[i1, 0] + 800) * w) + 800 
        newpointR[i1, 1] = newpointR[i1, 1] - 800 
        ax.plot(points[:, 0], points[:, 1], color = 'k')
        trees(ax, n - 1, newpointL, w)
        trees(ax, n - 1, newpointR, w)

pointsTree = np.array([[0, 0], [800, 800], [1600, 0]])
figTree, axTree = plt.subplots()
trees(axTree, 6, pointsTree, .5)
axTree.set_aspect(1.0)
axTree.axis('off')

plt.show()