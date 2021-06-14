from algo1 import *

#===============================#
#Se crea la estructura LinkdList:
class LinkedList:
  head= None
  
#===============================#
#===============================#
#Se crea la clase Node:
class Node:
  value= None
  key = None
  nextNode= None

#===============================#
def addValue(L,element): #Agrega un nuevo Nodo al comienzo de L
  #Crea el Nodo 
  nodeA= Node()
  nodeA.value=element
  
  #Inserta el Nodo
  if L.head==None:
    L.head= nodeA
  else:
    nodeA.nextNode= L.head

  L.head= nodeA
  return
#===============================#
#===============================#
def add(L,element):
  #Descripción: Agrega un elemento al comienzo de L, siendo L una LinkedList que representa el TAD secuencia.
  #Entrada: La Lista sobre la cual se quiere agregar el elemento (LinkedList) y el valor del elemento (element) a agregar.
  #Salida: No hay salida definida.
  #print(element)
  currentNode = Node()
  currentNode.key = element
  currentNode.nextNode = L.head
  L.head = currentNode
  return
#===============================#
#===============================#
def search(L,element):  #Busca un elemento en la lista:

  CurrentNode=L.head
  position= 0

  while CurrentNode!=None:
    if CurrentNode.value==element:
      return position #Devuelve la posición donde se encuentra el elemento  
    else:
      position += 1
      CurrentNode= CurrentNode.nextNode

  return None   #Devuelve None si no se encuentra la posición 
#===============================#
#===============================#
def insert(L,element,position): #Inserta un elemento en una posición determinada

  CurrentNode= L.head
  currentPosition= 0

  while CurrentNode!=None and currentPosition<position-1:
    CurrentNode= CurrentNode.nextNode
    currentPosition= currentPosition +1
  
  if position== 0:
    add(L,element)
    return position
  elif CurrentNode!=None:
    newNode=Node()
    newNode.value= element
    newNode.nextNode= CurrentNode.nextNode
    CurrentNode.nextNode= newNode

    return currentPosition +1
  else:
    return None

#===============================#
#===============================#
def delete(L,element):  #Elimina un elemento en una posición determinada
 
  position=search(L,element)
  CurrentNode=L.head

  if position!=None:

    if position== 0:      
      CurrentNode= CurrentNode.nextNode #Elimina el primer caso
      L.head= CurrentNode

      return position

    for i in range(0,position-1):
      CurrentNode= CurrentNode.nextNode 
    
    CurrentNode.nextNode= CurrentNode.nextNode.nextNode  #Elimina el elemento a eliminar
    return  position  #Devuelve la posición del elemento a eliminar
  else:
    return None #Devuelne None si no se encuentra el elemento    
  
#===============================#
#===============================#
def length(L): #Calcula la cantidad de elementos que tiene la lista

  CurrentNode= L.head
  currentPosition= 0

  while CurrentNode!=None:
    currentPosition += 1
    CurrentNode=CurrentNode.nextNode
  
  return currentPosition
#===============================#
#===============================#
def access(L,position): #Permite acceder a un elemento de la lista en una posición determinada

  currentPosition= length(L)

  if currentPosition<position:
    return None #Devuelve None si la posición ingresada es mayor a la cantidad de elementos

  else:
    CurrentNode= L.head
    cont= 0

    while CurrentNode!= None:
      if cont== position:
        return CurrentNode.value  #Devuelve el valor del Nodo en position
      else:
        CurrentNode= CurrentNode.nextNode
        cont += 1    
#===============================#
#===============================#
def update(L,element,position): #Permite cambiar el valor de un elemento de la lista en una posición determinada

  currentPosition= length(L)

  if currentPosition<position:
    return None #Devuelve None si la posición ingresada es mayor a la cantidad de elementos
  else:
    CurrentNode= L.head
    cont= 0

    while CurrentNode!=None:
      if cont==position:
        CurrentNode.value= element
        return position #Devuelve la posición del nodo que fue modificado
      else:
        CurrentNode= CurrentNode.nextNode
        cont += 1
    
#===============================#
#===============================#
def concatenateList(list1,list2):
  currentNode= list1.head
  if list2.head== None:
    return list1
  while currentNode.nextNode:
    currentNode=currentNode.nextNode
  
  currentNode.nextNode= list2.head
  
  return list1


#===============================#
def printList(L, index):
	list_len = list_length(L)
	if index == 0 or index >= list_len:
		index = list_len
	current_node = L.head
	for i in range(index):
		if current_node.nextNode:
			print(current_node.value,"->", end = " ")
		else: 
			print(current_node.value)
		current_node = current_node.nextNode
#===============================#
#===============================#
def append(List, element):
	newNode = Node()
	newNode.value = element
	currentNode = List.head
	if List.head==None:
		List.head=newNode
	else:
		while currentNode!=None:
			prevNode=currentNode
			currentNode = currentNode.nextNode
		prevNode.nextNode=newNode