from algo1 import *
from linkedlist import *

class PriorityQueue:
  head = None

class PriorityNode:
  value = None
  nextNode = None
  priority = None

def enqueue_priority(Q,element,priority):
    currentNode = Q.head
    i=0
    if currentNode == None:
        node = PriorityNode()
        node.value = element
        node.priority = priority
        Q.head = node
        return
    while currentNode != None:
        if priority > currentNode.priority:
            insert_priority(Q,element,i,priority)
            return
        if currentNode.nextNode == None:
            insert_priority(Q,element,i+1,priority)
            return
        currentNode = currentNode.nextNode
        i+=1


def dequeue(Q):
    current = Q.head
    Q.head = current.nextNode
    return current.value, current.priority


def insert_priority(L,element,position,priority): #Inserta un elemento en una posición determinada

  CurrentNode= L.head
  currentPosition= 0

  if position== 0:
        current = Q.head
        node = PriorityNode()
        node.value = element
        node.priority = priority
        Q.head = node
        Q.head.nextNode = current
        return position

  while CurrentNode!=None and currentPosition < position -1:
    CurrentNode= CurrentNode.nextNode
    currentPosition= currentPosition +1

  if CurrentNode!=None:
    newNode=PriorityNode()
    newNode.value= element
    newNode.priority = priority
    newNode.nextNode= CurrentNode.nextNode
    CurrentNode.nextNode= newNode

    return currentPosition +1
  else:
    return None



Q = PriorityQueue()

enqueue_priority(Q,"hola",1)
enqueue_priority(Q,"vfrvd",6)
enqueue_priority(Q,"hvedfa",5)
enqueue_priority(Q,"cdferc",2)
enqueue_priority(Q,"cduniunic",1)
enqueue_priority(Q,"cdferc",2)
enqueue_priority(Q,"hybuyhbuy",2)

print(dequeue(Q))
print(dequeue(Q))
print(dequeue(Q))
print(dequeue(Q))
print(dequeue(Q))
print(dequeue(Q))
print(dequeue(Q))

#printList(Q,0)

