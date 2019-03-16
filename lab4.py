# Code to implement a b-tree
# Programmed by Yury Ionov
# Instructor: Olac Fuentas 
# TA: Mali, Anindita Nath
# LAB 4
# Last modified March 12, 2019

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=3):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
        
def getMinAtDepth(T, d):
    if T != None:
        if d == 0:
            return T.item[0]
        if d > height(T):
            return -1
        else:
            return getMinAtDepth(T.child[0], d - 1)

def getMaxAtDepth(T, d):
    if T != None:
        if d == 0:
            return T.item[-1]
        if d > height(T):
            return -1
        else:
            return getMaxAtDepth(T.child[-1], d - 1)

def sortedList(T):
    if T.isLeaf:
        return list(T.item)
    C = []
    for i in range(len(T.child)-1):
        A = sortedList(T.child[i])
        C = C + A + [T.item[i]]
    B = sortedList(T.child[-1])
    return C + B
            
def nodesAtDepth(T,d):
    if d==0:
        return 1
    if T.isLeaf:
        return 0
    count = 0 
    for i in range(len(T.child)):
        count = count + nodesAtDepth(T.child[i], d-1)
    return count

def printAtDepth(T,d):
    if d == 0:
        print(T.item, end=" ")
    for i in range(len(T.child)):
        printAtDepth(T.child[i],d-1)
        
def fullNodes(T):
    if T.isLeaf:
        if IsFull(T):
            return 1
    else:
        if IsFull(T):
            return 1
    count = 0
    for i in range(len(T.child)):
        count = count + fullNodes(T.child[i])
    return count

def fullLeaves(T):
    if T.isLeaf:
        if IsFull(T):
            return 1
    count = 0
    for i in range(len(T.child)):
        count=count + fullNodes(T.child[i])
    return count

def keyAtDepth(T,k,h):
    if k in T.item:
        return 0
    c = 0
    for i in range(h):
        c = c + 1
        for j in range(len(T.child)):
            if k in T.child:
                return c
            keyAtDepth(T.child[j],k,h)
    return -1


def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')

SearchAndPrint(T,60)
SearchAndPrint(T,200)
SearchAndPrint(T,25)
SearchAndPrint(T,20)

print(height(T))
print(getMinAtDepth(T, 2))
print(getMaxAtDepth(T, 2))
print(sortedList(T))
print(nodesAtDepth(T,2))
printAtDepth(T,2)
print()
print(fullNodes(T))
print(fullLeaves(T))
print(keyAtDepth(T,3,height(T)))





