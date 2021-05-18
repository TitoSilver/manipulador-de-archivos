from algo1 import *

#Creamos TAD-Array
#==================================#

def search(array1,element):
  
### Busca un elemento deseado en el array ingresado
### y devuelve el indice donde se encuentra
### caso contrario, devuelve None
  
  for i in range(0,len(array1)):
    if array1[i]==element:
      return i

  return None

#==================================#
#==================================#


def insert(array1,element,position):
  
### Inserta un elemento en una posición dada
### desplaza los demas elementos del array eliminando el de la ultima pos.
### caso contrario, devuelve None

  if position< len(array1): #Usamos como estándar que la posición empieza desde 0

    if position==(len(array1)-1): #Separamos el caso de ser reemplazado el ultimo elemento
      array1[position]= element
      return position

    for i in range(len(array1)-1,position,-1): #se reorganizan los elementos del array
      array1[i]=array1[i-1]
    
    array1[position]=element   #se aplica el elemento sobre el array

    return position  #devuelve la posición el valor ingresado
    
  else:
    return None
  

#==================================#
#==================================#

def delete(array1,element):

  ### Elimina el primer elemento encontrado y desplaza el resto del array
  ### rellena el arreglo con None
  ### caso contrario devuelve None

  position= search(array1,element)
  if position != None:
    for i in range(position,len(array1)-1): 
      array1[i]=array1[i+1]
    array1[len(array1)-1]=None
    return position #Devuelve la posición donde estaba el elemento eliminado
  return None # Devuelve None cuando no se encontro el elemento a eliminar
  
#==================================#
#==================================#

def length(array1):
  ### Calcula el numero de elementos que tiene el array ingresado

  cont= 0

  for i in range(0,len(array1)):
    if array1[i]!=None:
      cont = cont + 1

  return cont
#==================================#  