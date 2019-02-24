# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:01:17 2019

@author: yury1
"""

import random
# Defining a class which will create our nodes
class Node:
    def init(self, data):
        self.data = data
        self.next = None

# Defining a class which will create our linked list and also defining other utility methods
class LinkedList:
    def init(self):
        self.head = None
        self.tail = None

# Defining the method to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next
    def Print(L):
    # Prints list L's items in order using a loop
        temp = L.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
# New line 
# Defining the method to create a node at the end of the linked list
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def BubbleSort(theList):
    change = True
    count = 1
    if theList is None:
        return theList
    while change:
        temp = theList
        change = False
        while temp.next is not None:
            count += 1
            if temp.data> temp.next.data:
                temp2 = temp.data
                temp.data = temp.next.data
                temp.next.data = temp2
                change = True
            temp = temp.next
    return theList

#will merge two linked lists
def mergeLists(list1, list2):
    temp = None
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.data <= list2.data:
        temp = list1
        temp.next = mergeLists(list1.next, list2)
    else:
        temp = list2
        temp.next = mergeLists(list1, list2.next)
    return temp
# will sort the linked list using mergeSort
def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    head = mergeLists(l1, l2)
    return head

# divide a linked list into two equal linked lists
def divideLists(head):
    slow = head                     # slow is a pointer to reach the mid of linked list
    fast = head                     # fast is a pointer to reach the end of the linked list
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next            # fast is incremented twice while slow is incremented once per loop
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid



def listFiller(theList, numOfItems):
    temp = theList
    for i in range(numOfItems):
        if temp.head == None:
            temp.head = Node(random.randrange(101))
            temp.tail = temp.head
        else:
            temp.tail.next = Node(random.randrange(101))
            temp.tail = temp.tail.next
# The main logic starts from here
listFiller(list1,10)

print ("Linked list before bubble sorting")
list1.printList() 
print() 
#print("No new Lines")
#list1.Print()                   # Printing the unsorted linked list

list1.head = mergeSort(list1.head)      # Applying mergeSort to linked list

print()
print()

print ("Linked list after  merge sorting")
list1.printList()    # Printing the sorted linked list
print()
#print("No New Lines") 
#list1.Print()

print()
print()

list2 = LinkedList()
listFiller(list2,10)


print()


print ("Linked list before bubble sorting")
list2.printList()
print()
#print("No new Lines")
#list2.Print()                   # Printing the unsorted linked list
print()
print()
print ("Linked list after bubble sorting")
list2.printList()    # Printing the sorted linked list
print()
#print("No New Lines") 
#list2.Print()