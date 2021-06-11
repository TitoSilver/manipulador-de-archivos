from algo1 import *


class LinkedList:
  head = None

class Node:
  value = None
  key = None
  nextNode = None


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



def search(L,element):
  #Descripción: Busca un elemento de la lista que representa el TAD secuencia.
  #Entrada: la lista sobre el cual se quiere realizar la búsqueda (Linkedlist) y el valor del elemento (element) a buscar.
  #Salida: Devuelve la posición donde se encuentra la primera instancia del elemento. Devuelve None si el elemento no se encuentra.

  cont = 0 
  currentNode = L.head
  if currentNode == None:
     return None
  while currentNode.value != element:
    cont = cont +1
    currentNode = currentNode.nextNode
    if currentNode == None:
     return None
  return cont


def list_length(L):
  #Descripción: Calcula el número de elementos de la lista que representa el TAD secuencia.
  #Entrada: La lista sobre la cual se quiere calcular el número de elementos.
  #Salida: Devuelve el número de elementos.
  if L.head == None:
    return None
  else:
    currentNode = L.head
    cont = 0
    while currentNode != None:
      cont = cont+1
      currentNode = currentNode.nextNode
    return cont


def insert(L,element,position):
  #Descripción: Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
  #Entrada: la lista sobre el cual se quiere realizar la inserción (Linkedlist) y el valor del elemento (element) a insertar y la posición (position) donde se quiere insertar.
  #Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.

  if position > length(L) or position < 0:
    return None
  else:
    cont = 0
    currentNode = L.head
    while cont < position-1: # voy hasta la posición anterior a la indicada.
      currentNode = currentNode.nextNode
      cont = cont+1
      if currentNode == None:
        return None
    if position == 0: # si se quiere insertar en al primer posición, directamente agrego el elemento en el primer lugar usando add.
      add(L,element)
      return position
    else: # si la posición es mayor a cero, creo un nuevo nodo, le asigo element en value e inserto el nodo en la posición.
      node1 = Node()
      node1.value = element
      node1.nextNode = currentNode.nextNode
      currentNode.nextNode = node1
      return position
 

def delete(L,element):
  #Descripción: Elimina un elemento de la lista que representa el TAD secuencia.
  #Poscondición: Se debe desvincular el Node a eliminar.
  #Entrada: la lista sobre el cual se quiere realizar la eliminación (Linkedlist) y el valor del elemento (element) a eliminar.
  #Salida: Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.

  position = search(L,element) #busco la posición del elemento con search.
  
  if position != None:
    currentNode = L.head
    if position == 0: #si la posición es 0, desvinculo el primer nodo directamente.
      L.head = currentNode.nextNode
      return position
    for cont in range(0,position-1): #me posiciono en el nodo anterior al que se desea eliminar.
      currentNode = currentNode.nextNode
    currentNode.nextNode = currentNode.nextNode.nextNode #desvinculo el nodo.
    return position
  else:
    return None


def access(L,position):
  #Descripción: Permite acceder a un elemento de la lista en una posición determinada.
  #Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
  #Salida: Devuelve el valor de un elemento en una position de la lista, devuelve None si no existe elemento para dicha posición.

  if length(L) < position or position < 0:
    return None
  else:
    currentNode = L.head
    for i in range(0,position):
      currentNode = currentNode.nextNode
    return currentNode.value


def update(L,element,position):
  #Descripción: Permite cambiar el valor de un elemento de la lista en una posición determinada
  #Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de element.
  #Salida: Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.

  if length(L) < position or position < 0:
      return None
  else:
    currentNode = L.head
    for i in range(0,position):
      currentNode = currentNode.nextNode
    currentNode.value = element
    return position
  

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



def swap(L,pos1,pos2):
  nodo1 = L.head
  for i in range(0,pos1):
    nodo1 = nodo1.nextNode
  nodo2 = L.head
  for j in range(0,pos2):
    nodo2 = nodo2.nextNode
    
  currentNode = L.head
  saveNode1 = nodo1
  saveNode2 = nodo2
  while currentNode != None:
    if currentNode.nextNode == nodo1:
      currentNode.nextNode = nodo2
      nodo2.nextNode = saveNode1.nextNode
    if currentNode.nextNode == nodo2:
      currentNode.nextNode = nodo1
      nodo1.nextNode = saveNode2.nextNode
    currentNode = currentNode.nextNode
  return

def printlist(L, index):
	list_len = length(L)
	if index == 0 or index >= list_len:
		index = list_len
	current_node = L.head
	for i in range(index):
		if current_node.nextNode:
			print(current_node.value,"->", end = " ")
		else: 
			print(current_node.value)
		current_node = current_node.nextNode