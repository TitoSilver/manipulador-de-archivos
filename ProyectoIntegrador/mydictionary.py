from algo1 import *
from linkedlist import *
from myarray import *
#=============================================#
class Dictionary:
    head= None    

class DictionaryNode:
    value= None
    key= None

#=============================================#
                #HASH-KEY
#=============================================#
#direccionamiento abierto
    #lineal Probing
    #cuadrating Probing
    #Doble Hashing  k(k,i)= (h1(k) + i*h2(k)) mod m
def doble_hasing_key(key,m):
    
    return
    

#colisiones por encadenamiento
def hash_Key(key,m):
    if type(key)==int:
        return key % m  #retorna la key en el array
    elif type(key)==str:
        return ord(key) % m
        

#=============================================#
                #INSERT
#=============================================#

def dictInsert(dic,key,value):    
    node= DictionaryNode()
    node.key= key
    node.value= value
    dictKey= hash_Key(key, len(dic))
    
    if dic[dictKey]:
        #existe una cabecera creada en posición
        add(dic[dictKey],node)
        
    else:
        #El array esta vacío en esa posición  
        dic[dictKey]= Dictionary()
        add(dic[dictKey],node)
        
#=============================================#
                #SEARCH
#=============================================#

def dictSearch(dic,key):
    
    dictKey= hash_Key(key,len(dic))
    
    if dic[dictKey]:
        currentNode= dic[dictKey].head
    else:
        return None
    
    while currentNode:
        if currentNode.value.key== key:
            return currentNode.value.value
        currentNode= currentNode.nextNode
    
    return None

#=============================================#
                #DELETE
#=============================================#
def dictDelete(dic,key):
    dictKey= hash_Key(key,len(dic))
    
    currentNode= dic[dictKey].head
    prevNode= currentNode
    
    while currentNode:
        if currentNode.value.key==key and prevNode==currentNode:
            dic[dictKey].head= currentNode.nextNode
            return 
        elif currentNode.value.key==key and prevNode!=currentNode:
            prevNode.nextNode= currentNode.nextNode
            return
        else:
            currentNode=currentNode.nextNode
            if prevNode.nextNode!= currentNode:
                prevNode= prevNode.nextNode
                
#=============================================#
                #UPDATE
#=============================================#
def dictUpdate(dic,key,newValue):
    dictKey= hash_Key(key,len(dic))
    
    if dic[dictKey]:
        
        currentNode=dic[dictKey].head
        while currentNode:
            if currentNode.value.key==key:
                currentNode.value.value= newValue
                return 
            currentNode=currentNode.nextNode
    """
    #En caso de no encontrar el nodo a modificar 
    #lo inserta
    insert(dic,key,newValue)
    
    """
    
        
        