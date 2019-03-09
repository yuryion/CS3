# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019

import matplotlib.pyplot as plt
import numpy as np
import math



class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
    def getDepth(self):
        if self.left and self.right:
            return 1 + max(self.left.getDepth(), self.right.getDepth())
        elif self.left:
            return 1 + self.left.getDepth()
        elif self.right:
            return 1 + self.right.getDepth()
        else:
            return 1
        
        
        
        

        
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

'''def Find(T,k):    #recursive
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
'''
def Find(T,k):   #itterative
    while T != None:
        if T.item == k:
            return T
        if k > T.item:
            T = T.right
        elif k < T.item:
            T = T.left
        else:
            return None


def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')


def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,center,radius, tree):
#def draw_circles(ax, n, center, radius):
    if tree != None:
        x,y = circle(center,radius)
        ax.fill(x,y, c = 'w')
        ax.plot(x,y,color='k')
        ax.text(center[0]-2, center[1]-1, tree.item, fontsize = 8)
        ax.text(center[0]-2, center[1]-1, 10, fontsize = 8)
        newCenterL = center - 40
        newCenterL[0] = newCenterL[0] * 0.4
        newCenterR = center
        newCenterR[0] = ((newCenterR[0] + 40) * 0.4) + 120
        newCenterR[1] = newCenterR[1] - 40
        draw_circles(ax, newCenterL, radius, tree.left)
        x,y = circle(center,radius)
        ax.fill(x,y, c = 'w')
        ax.plot(x,y,color='k')
        ax.text(center[0]-2, center[1]-1, tree.item, fontsize = 8)
        draw_circles(ax, newCenterR, radius, tree.right)
        draw_circles(ax, n - 1, newCenterL, radius)
        draw_circles(ax, n - 1, newCenterR, radius)



def ballancedTree(theList):
    if len(theList)==0:
        return None
    n = len(theList)//2         
    T =  BST(theList[n])
    T.left = ballancedTree(theList[:n])
    T.right = ballancedTree(theList[n+1:])
    return T
    #youre not returning anything DUH :/ 

def treeToList(T):
    if T is None:
        return []
    return treeToList(T.left) + [T.item] + treeToList(T.right)

#def depth(T):
    




def elementsAtDepth(T,n):
    if T is None: 
        return 
    if n == 0: 
        print (T.item, end=" "), 
    else: 
        elementsAtDepth(T.left, n-1) 
        elementsAtDepth(T.right, n-1) 




T = None
A = [1,2,3,4,5,6,7,8,9,10]

T = ballancedTree(A)
InOrder(T)
print()
print(treeToList(T))

plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 50, 100, T)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')



for i in range(T.getDepth()):
    print("Elements at depth ", i, ": ", end=" ")
    elementsAtDepth(T, i)
    print()
'''
   
# Code to test the functions above
T = None
A = [10, 4, 15, 2, 1, 3, 8, 5, 9, 7, 12, 18]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()

print(SmallestL(T).item)
print(Smallest(T).item)

FindAndPrint(T,18)
FindAndPrint(T,8)

n=60
print('Delete',n,'Case 1, deleted node is a leaf')
T = Delete(T,n) #Case 1, deleted node is a leaf
InOrderD(T,'')
print('####################################')

n=90      
print('Delete',n,'Case 2, deleted node has one child')      
T = Delete(T,n) #Case 2, deleted node has one child
InOrderD(T,'')
print('####################################')

n=70      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')

n=40      
print('Delete',n,'Case 3, deleted node has two children') 
T = Delete(T,n) #Case 3, deleted node has two children
InOrderD(T,'')
'''