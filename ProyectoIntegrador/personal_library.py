#from linkedlist import printlist
from mydictionary import *
from linkedlist import *
from test_files import *
import os
from tools import *
import sys, os
from hashtable import *

"""
class Node_file:
    def __init__(self,name_file,hash_of_words):
        self.nameFile: name_file
        self.hash_of_words: hash_of_words
"""
class Node_file:
    nameFile = None
    hash_of_words = None
        
list_file= LinkedList()
def create (path):
    with os.scandir(path) as it:
        listOfWords=LinkedList()
        for file in it:
            if file.is_file() and ".txt" in file.name:
                fileNameOnly= file
                print(file.name)            
                with open(path+"\\"+file.name,"r") as file:
                    lines= file.readlines()
                    count_words= 0
                    
                    for line in lines:
                        #recorre cada linea y devuelve el número de palabras (en la linea) y una lista con una palabra por nodo.
                        count,newList=travel_line(line)
                        count_words += count
                        if newList:
                            #inserta en la nueva lista la lista con todos los elementos anteriores, devuelve una lista con todas las palabras encontradas hasta el momento.
                            listOfWords= concatenateList(newList,listOfWords)
                    
                    #agrega a la lista final el nodo con (nombre del archivo,hashTable del archivo)
                    #printList(listOfWords,0)
                    
                        #FORMA EN LA QUE DEBE INSERTARSE LOS NODOS 
                    #add(list_file,Node_file(fileNameOnly,listOfWords))
                    
                    print("cant Palabras: ",count_words)       
                    currentNode=listOfWords.head
                    while currentNode:
                        #print("palabra: ",currentNode.value)
                        currentNode=currentNode.nextNode
                    
                    m = primo_mayor(count_words) #encuentra el primo mayor al numero de palabras en el archivo.
                    T = Array(m,LinkedList()) #crea la tabla.
                    current = listOfWords.head 
                    while current: #inserta cada palabra en la tabla.
                        insertHash(T,current.value)
                        current = current.nextNode
                    #creo el nodo que contiene el nombre del archivo y la tabla hash con todas las palabras.     
                    Nodo = Node_file()
                    Nodo.nameFile = fileNameOnly
                    Nodo.hash_of_words = T
                    addValue(list_file,Nodo)#agrega la tabla con las palabras a la LinkedList.
        
            listOfWords.head= None

    current = list_file.head
    while current:
        print(current.value.nameFile)
        element = current.value.hash_of_words
        for i in range(0,len(element)):
            if element[i] != None:
                print(element[i].head.key,end=" ")
                print(element[i].head.value)
            else:
                print(None)
        current = current.nextNode
    return list_file


if __name__ == '__main__':
    listArguments= sys.argv
    print(listArguments)
    if len(listArguments)!= 3:
        if len(listArguments) > 3:
            #En caso de pasar mas de 3 parametros (que el path ingresado tenga espacios en el nombre de los directorios), concatena los argumentos
            #y luego verifica si existe o no ese path.
            #En caso que el path Exista: Envía el path a la función correspondiente
            #en caso que el path NO Exista: Avisa al usuario que el path envíado no existe.
            path=listArguments[2]
            for idx in range(3,len(listArguments)):
                path +=" " +listArguments[idx]
                
            if os.path.exists(path):
                print("el path que pasa como parametro es: ",path)
                create(path)
            else:
                print("El path ingresado no es correcto. Por favor, Intente nuevamente")
        else:
            #Pasa un comando en el que faltan argumentos
            print("Por favor ingrese una instrucción valida")
            
    elif listArguments[1]== "--create" or listArguments[1]== "-create":
        if os.path.exists(listArguments[2]):
            print("el path que pasa como parametro es: ",listArguments[2])
            if os.path.exists(listArguments[2]):
                create(listArguments[2])
    
    elif listArguments[1]== "--search" or listArguments[1]== "-search":
        print("uwu")
    else:
        #Pasa un comando en el que existen todos los argumentos, pero la función que pasa no es correcta
        print("Por favor ingrese una instrucción valida")

    
    #===============================================================================================================================================#
                                    # PATH DE PRUEBA
        #Prueba Path Diego:
    # py personal_library.py --create D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\proyecto-grupo4\ProyectoIntegrador\test_files
    # py personal_library.py -create D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\proyecto-grupo4\ProyectoIntegrador\test_files
    
    # py personal_library.py --create C:\Users\ULTRABYTES\Desktop\test_files
    # py personal_library.py -create C:\Users\ULTRABYTES\Desktop\test_files
        #Prueba Path Luciano:
    # py personal_library.py --create C:\Users\Omen\Documents\FACULTAD\2Ano\1Semestre\Algoritmos_2\proyecto-grupo4\ProyectoIntegrador\test_files
        
    #===============================================================================================================================================#
    