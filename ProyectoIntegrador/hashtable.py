from algo1 import *
from linkedlist import *

def h1(k,m):
  return k % m

def h2(k,m):
  if m > 2:
    return 1 + (k % (m-2))
  else:
    return k % m-1

def hash(k,i,m):
  return (h1(k,m) + i*h2(k,m)) % m

def gen_key(string,m):
  #genera un key numerico a partir de la string.
  key = 0
  for i in range(0,len(string)):
    j = abs(i-len(string))
    key += ord(string[i])*255^j
  return key % m


def insertHash(T,element):
  #recibe un Array que va a ser la tabla Hash, el tamaño del Array y el string a insertar.
  m = len(T)
  if m > 1:
    key = gen_key(element,m) #genero el key de la string
  elif m ==1:
    key = 0
  else:
    return None
  noInsertado = True
  i=0
  while noInsertado:
    #itera hasta que se encuentra una posicion que este desocupada o que este ocupada por el mismo elemento.
    pos =  hash(key,i,m) #calcula la posicion del slot donde insertar el elemento en la tabla.

    if T[pos] == None: #si la posicion esta vacia, creo una linkedlist en ese slot, agrego el elemento a la lista y coloco en 1 el campo value.
      T[pos] = LinkedList()
      add(T[pos],element)
      T[pos].head.value = 1
      noInsertado = False
    elif T[pos].head.key == element: #si el slot no esta vacio y el elemento que contiene es igual al que se quiere insertar, le sumo 1 al campo value.
      T[pos].head.value += 1
      noInsertado = False
    i += 1
      

def searchHash(T,element):
  #recorre la tabla, si encuentra el elemento que se busca retorna el valor y el key.
    m = len(T)
    key = gen_key(element,m)
    for i in range(0,m):
        pos = hash(key,i,m)
        if T[pos] != None:
            current = T[pos].head
            #print(pos,":",current.key,element)
            if current.key == element: #no se porque con algunas palabras no hace la comparacion.
                print("match")
                return current.key, current.value
    return None


def primo_mayor(numero):
  #retorna el primer número primo mayor que n.
  n = numero
  if n == 0:
    return None
  p = True
  while p:
    if n > 1:
      for i in range(2,n):
        if i == n-1:
          return n
        if n % i == 0:
          break
    n = n+1