# Code to implement 
# Programmed by Yury Ionov
# Instructor: Olac Fuentas 
# TA: Mali, Anindita Nath
# LAB 6
# Last modified April 2, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        
def union_by_size(S,i,j):
    ri = find_c(S,i)
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]:
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def numOfSets(S):
    total=0
    for i in range(len(S)):
        if S[i] <= -1:
            total = total + 1
    return total

def BFS(size,s): 
    # Mark all the vertices as not visited 
    visited = [False] * (len(size)) 
  
    # Create a queue for BFS 
    queue = [] 
  
    # Mark the source node as  
    # visited and enqueue it 
    queue.append(s) 
    visited[s] = True
  
    while queue: 
  
        # Dequeue a vertex from  
        # queue and print it 
        s = queue.pop(0) 
        print (s, end = " ") 
  
        # Get all adjacent vertices of the 
        # dequeued vertex s. If a adjacent 
        # has not been visited, then mark it 
        # visited and enqueue it 
        for i in size: 
            if visited[i] == False: 
                queue.append(i) 
                visited[i] = True

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path





plt.close("all") 
maze_rows = 4
maze_cols = 4

walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
    
S = DisjointSetForest(maze_rows*maze_cols)
start_time = time.time()
"""
while numOfSets(S)>1:
    d = random.randint(0,len(walls)-1)
    if find(S,walls[d][0]) != find(S,walls[d][1]):
        union(S,walls[d][0],walls[d][1])
        walls.pop(d)
"""


print("Number of cells:", maze_rows*maze_cols)
numOfWallsToRemove = input("Enter the number of walls to remove \nWalls removed: ")
print(int(numOfWallsToRemove))
i=0
while int(numOfWallsToRemove)>i:
    d = random.randint(0,len(walls)-1)
    if find(S,walls[d][0]) != find(S,walls[d][1]):
        union(S,walls[d][0],walls[d][1])
        walls.pop(d)
    i=i+1

if int(numOfWallsToRemove)<(maze_rows*maze_cols)-1:
    print("A path from source to destination is not guaranteed to exist")
    
if int(numOfWallsToRemove)==(maze_rows*maze_cols)-1:
    print("There is a unique path from source to destination")

if int(numOfWallsToRemove)>(maze_rows*maze_cols)-1:
    print("There is at least one path from source to destination")

listS = []
for i in range(maze_rows*maze_cols):
    listS.append([])
    for j in range(maze_rows*maze_cols):
        if find(S,i) not in listS[i]:
            listS[i].append(find(S,i))
    
print(listS)
    
print(BFS(maze_rows*maze_cols,0))




draw_maze(walls,maze_rows,maze_cols) 



print(time.time()-start_time)





















