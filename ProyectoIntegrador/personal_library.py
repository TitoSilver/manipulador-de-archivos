# -*- coding: utf-8 -*-

from mydictionary import *
from linkedlist import *
from test_files import *
import os
from tools import *
import sys, os
from hashtable import *
import pickle
from priorityqueue import *
from pathlib import Path

class Node_file:
    nameFile = None
    hash_of_words = None
        
list_file= LinkedList()
def create (path):
    with os.scandir(path) as it:
        listOfWords=LinkedList()
        for file in it:
            if file.is_file() and ".txt" in file.name:
                fileNameOnly= file.name
                print("=================")
                print("file name: ",fileNameOnly)
                print("=================")
                pathDirectory= Path(path)      
                with open(pathDirectory.joinpath(file.name),"r",encoding='utf-8') as file:
                    lines= file.readlines()
                    count_words= 0
                    
                    for line in lines:
                        #recorre cada linea y devuelve el número de palabras (en la linea) y una lista con una palabra por nodo.
                        count,newList=travel_line(line)
                        count_words += count
                        #printList(newList,0)
                        if newList and newList.head:
                            #inserta en la nueva lista la lista con todos los elementos anteriores, 
                            # devuelve una lista con todas las palabras encontradas hasta el momento.
                            listOfWords= concatenateList(newList,listOfWords)
                    print(count_words)
                    
                    #agrega a la lista final el nodo con (nombre del archivo,hashTable del archivo)
                    #printList(listOfWords,0)
                    
                        #FORMA EN LA QUE DEBE INSERTARSE LOS NODOS 
                    #add(list_file,Node_file(fileNameOnly,listOfWords))    
                    
                    m = primo_mayor(count_words) #encuentra el primo mayor al numero de palabras en el archivo.
                    T = Array(m,LinkedList()) #crea la tabla.
                    current = listOfWords.head
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
            
    return list_file

def search(list_file,key):
    Q = PriorityQueue() #crea una cola de prioridad.
    current = list_file.head
    while current:
        #recorre la lista que contiene las tablas hash de cada archivo.
        table = current.value.hash_of_words
        elemento, ocurrencias = searchHash(table,key) #busca la palabra "key" en la tabla hash y devuelve el nombre del elemento y las ocurrencias en ese archivo.
        if elemento!=None  and ocurrencias != None:
            #agrega a la cola de prioridad el nombre del archivo donde se encontró y las ocurrencias
            # (este va a ser el parametro que de la prioridad en la cola).
            enqueue_priority(Q,current.value.nameFile,ocurrencias)
        current = current.nextNode
    return Q

def modulCreatePickle (list_files,path_bin):
    with  open(os.path.join(path_bin, "binFile"),"bw") as binFile:
        pickle.dump(list_files,binFile)
    
def modulReadPickle (path_bin):
    with  open(os.path.join(path_bin, "binFile"),"br") as binFile:
        list_files = pickle.load(binFile)
    return list_files  #retorna el hashtable con todas las palabras


if __name__ == '__main__':
    listArguments= sys.argv
    
    value= True
    if len(listArguments)!= 3:
        if len(listArguments) > 3:
            #En caso de pasar mas de 3 parametros (que el path ingresado tenga espacios en el nombre de los directorios), concatena los argumentos
            #y luego verifica si existe o no ese path.
            #En caso que el path Exista: Envía el path a la función correspondiente
            #en caso que el path NO Exista: Avisa al usuario que el path envíado no existe.
            path=listArguments[2]
            
            for idx in range(3,len(listArguments)):
                path +=" " +listArguments[idx]
        else:
            #Pasa un comando en el que faltan argumentos
            print("Por favor ingrese una instrucción valida")
            value= False
    else:
        path= listArguments[2]
    
    if (listArguments[1]=="--create" or listArguments[1]=="-create") and value:
        if os.path.exists(path):
            print("el path que pasa como parametro es: ",path)
            list_file = create(path)
            
            #despues de crear la lista la retornamos. Para luego crear el binario y que el código sea mas legible
            #dirBin= os.getcwd()+ "\\bin"   #obtenemos el path de la carpeta bin
            dirBin= os.path.join("bin")
            dirBin=Path(dirBin)
            listaCompleta= os.listdir(dirBin)
            print("ListaCompleta: ",listaCompleta)
            
            if os.scandir(dirBin):  #verificamos su existencia
                if len(os.listdir(dirBin))!=0: 
                    #Elimina los archivos de la carpeta bin para crear el nuevo binario
                    
                    for element in os.listdir(dirBin):
                        os.remove(os.path.join(dirBin,element))
                    
            modulCreatePickle (list_file,dirBin)
        
            print("library created successfully")
            
        else:
            print("El path ingresado no es correcto. Por favor, Intente nuevamente")
    elif (listArguments[1]== "--search" or listArguments[1]== "-search") and value:
        #dirBin= os.getcwd()+ "\\bin"   #obtenemos el path de la carpeta bin
        dirBin= os.path.join("bin")
        list_file = modulReadPickle (dirBin)
        listArguments[2] = listArguments[2].lower()

        Q= search(list_file,listArguments[2])
        if Q.head == None:
            print("\t"*4,"no document found")
        else:
            print("\t"*3,"PRINT PRIORITY QUEUE")
            current= Q.head
            while current:
                print("(",current.value,":",current.priority,")")
                current = current.nextNode
            print("\t"*4,"end")
        """
        print("====================================")
        print("\t"*4,"HASH_TABLE")
        print("====================================")
        #hace un print del contenido de las tablas.        
        current = list_file.head
        while current:
            print("Nombre del archivo: ",current.value.nameFile)
            element = current.value.hash_of_words
            print("{",end="")
            for i in range(0,len(element)):            
                if element[i] != None:
                    print("(",end="")
                    print(element[i].head.key,end=":")
                    print(element[i].head.value,end="")
                    print(")",end="\n")
                else:
                    print(None,end="\n")
            print("}")
            current = current.nextNode
        """
    else:
        print("El path ingresado no es correcto. Por favor, Intente nuevamente")
            
    #===============================================================================================================================================#
                                    # PATH DE PRUEBA
        #Prueba Path Diego:
    # py personal_library.py --create D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\proyecto-grupo4\ProyectoIntegrador\test_files
    # py personal_library.py -create D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\proyecto-grupo4\ProyectoIntegrador\test_files 
    
    # py personal_library.py --create C:\Users\ULTRABYTES\Desktop\test_files
    # py personal_library.py -create C:\Users\ULTRABYTES\Desktop\test_files
    
    # py personal_library.py -create C:\Users\ULTRABYTES\Desktop\prueba-exp-char
    
    # py personal_library.py -search can
    
    # py personal_library.py -create C:\Users\ULTRABYTES\Downloads\Test-Dataset

    # python3 personal_library.py -create "/home/titosilver/Descargas/Test-Dataset"

    
    
        #Prueba Path Luciano:
    # py personal_library.py --create C:\Users\Omen\Documents\FACULTAD\2Ano\1Semestre\Algoritmos_2\proyecto-grupo4\ProyectoIntegrador\Test-Dataset
        
    #===============================================================================================================================================#
    