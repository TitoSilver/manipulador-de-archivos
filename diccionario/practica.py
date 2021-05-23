from algo1 import *
from mydictionary import *
from myarray import *
from linkedlist import *
#=========================================#
#ejercicio 4
def igualString(text1,text2):
    #función que verifica si dos strings son iguales
    #creamos un dic con los elementos del text2
    if len(text1)==len(text2):
        dict_text2=Array(5,Dictionary() )
        
        for char in text2:
            dictInsert(dict_text2,char,char)
            
        for char in dict_text2:
            if char:
                currentNode= char.head
                while currentNode:
                    print("({0}:{1})".format(currentNode.value.key,currentNode.value.value))
                    currentNode= currentNode.nextNode
                print(",")
            else:
                print("None")
                print(",")

        print("")
        
    
        for char in text1:
            if   char!= dictSearch(dict_text2, char):
                return False
        
        return True
    else:
        return False

#=========================================#
#Ejercicio 5
#función que verifica si existen elementos repetidos
def unicElements(A):
       
    dictElements= Array(5, Dictionary())
    for element in A:
        if dictSearch(dictElements,element):
            return False
        else:
            dictInsert(dictElements,element,element)
    
    return True
        
#=========================================#
#Ejercicio 6
#código postal Argentino
def hash_ISO3166(key):
    """
    Sistema ISO 3166-2:AR
    A cada provincia le corresponde el codigo AR-X
    key= key.upper()
    coso=
    {
        "SALTA":A,
        "PROVINCIA DE BUENOS AIRES":B,
        "CIUDAD AUTONOMA DE BUENOS AIRES":C,
        "SAN LUIS":D,
        "ENTRE RIOS":E,
        "LA RIOJA":F,
        "SANTIAGO DEL ESTERO":G,
        "CHACO":H,
        "SAN JUAN":J,
        "CATAMARCA":K,
        "LA PAMPA":L,
        "MENDOZA":M,
        "MISIONES":N,
        "FORMOSA":P,
        "NEUQUEN":Q,
        "RIO NEGRO":R,
        "SANTA FE":S,
        "TUCUMAN":T,
        "CHUBUT":U,
        "TIERRA DEL FUEGO":V,
        "CORRIENTES":W,
        "CORDOBA":X,
        "JUJUY":Y,
        "SANTA CRUZ":Z        
    }
    
    return coso[key]
    
    """
    return "M"
def codPostal(direccion):
    
    ciudad=""
    direct=""
    coord=""
    for idx in range(0,len(direccion)):
        if direccion[idx]== ",":
            key= direccion[idx+1:]
            ciudad= hash_ISO3166(key)
            break
            
        try:
            int(direccion[idx])
            direct= direct + direccion[idx]
        except ValueError:
            coord= coord + direccion[idx]
    print("direccion: ",direccion)
    print("ciudad: {0}, direct: {1}, cord: {2}".format(ciudad,direct,coord))
    
    return ciudad+direct+"XXX"

#=========================================#
#Ejercicio 7
#Compresion de un String
def comprexString(string):
    dictComprex=Array(len(string),Dictionary())
    dictInsert(dictComprex,string[0],1)
    prevkey=string[0]
    return_comprex_string= ""
    for idx in range(1,len(string)):
        if string[idx]==prevkey:            
            dictUpdate(dictComprex,prevkey,dictSearch(dictComprex,prevkey) + 1)
        else:
            #Al cambiar de valor la key inserta el valor de las veces que se repitio el caracter
            return_comprex_string= return_comprex_string + prevkey + str(dictSearch(dictComprex,prevkey))
            prevkey= string[idx]
            dictInsert(dictComprex,prevkey,1)
    
    #al terminar de recorrer el string inserta lo que quedo en ultimo elemento
    return_comprex_string= return_comprex_string + prevkey + str(dictSearch(dictComprex,prevkey))
    
    return return_comprex_string

#=========================================#
#Ejercicio 9
#Ocurrencia en Strings

def ocurrenceSearch(T1,T2,consecutiveIndex,firstCharEqual):
    #siendo T1: Diccionario con la palabra mayor
    #siendo T2: Diccionario con la palabra a corroborar
    #siendo consecutiveIndex: las veces que se han acertado caracteres
    #siendo firstCharEqual: El indice del primer caracter en tener coinsidencia
    
    currentNode= T1[hash_Key(dictSearch(T2,consecutiveIndex), len(T1))]
    
    
    try:
        currentNode=currentNode.head
        while currentNode:
            if currentNode.value.key== T2[consecutiveIndex].head.value.key and currentNode.value.value==(firstCharEqual+consecutiveIndex): 
                return True
            currentNode=currentNode.nextNode
        
        return False
    except  AttributeError:
        return False
    
        

def nextCharEqual(T1,T2,consecutiveIndex,firstCharEqual):
    
    currentNode= T1[hash_Key(dictSearch(T2,consecutiveIndex), len(T1))]
    
    try:
        currentNode=currentNode.head
        
        while currentNode:
            test=ocurrenceSearch(T1,T2,consecutiveIndex,firstCharEqual)
            
            if consecutiveIndex==len(T2-1) and test:
                return True
            
            if test:
                return nextCharEqual(T1,T2,consecutiveIndex+1,firstCharEqual)
            
            currentNode.nextNode
        
        return False     
    
    except AttributeError:
        return False
    

def funcFirstCharEqual(T1,T2):
    firstChar= T2[0].head.value.value
    
    currentFirstChar= T1[hash_Key(dictSearch(T2,0),len(T1))]
    
    try:
        currentFirstChar=currentFirstChar.head
        
        while currentFirstChar:
            if currentFirstChar.value.key== T2[0].head.value.value:
                testFirstChar= nextCharEqual(T1,T2,0,currentFirstChar.value.value)
            
            if testFirstChar:
                return print("T2 Existe en T1")
            
            if currentFirstChar.nextNode:
                currentFirstChar= currentFirstChar.nextNode
            else:
                return print("T2 no existe en T1")
    except AttributeError:
        return ("T2 no existe en T1")               
        

def ocurrenceString(word1,word2):
    #insertamos en un diccionario word1 (palabra que contiene )
    dictContainerOcurrence=Array(len(word1),Dictionary())
    for idx in range(0,len(word1)):        
        dictInsert(dictContainerOcurrence,idx,word1[idx])
    
    #insertamos en un diccionario word2 (palabra a corroborar)    
    dictOcurrence=Array(len(word2),Dictionary())
    for idx in range(0,len(word1)):        
        dictInsert(dictOcurrence,word1[idx],idx)
        
    funcFirstCharEqual(dictContainerOcurrence,dictOcurrence)

        
    return