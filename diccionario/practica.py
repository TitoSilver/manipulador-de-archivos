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
            
            
    
    return 