from mydictionary import *
from linkedlist import *
from test_files import *
import os
from tools import *
import sys, os

class Node_file:
    def __init__(self,name_file,hash_of_words):
        self.nameFile: name_file
        self.hash_of_words: hash_of_words
        
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
                        count,newList=travel_line(line)
                        count_words += count
                        if newList:
                            listOfWords= concatenateList(newList,listOfWords)
                    
                    #agrega a la lista final el nodo con (nombre del archivo,hashTable del archivo)
                    #add(list_file,Node_file(fileNameOnly,listOfWords))
                    
                    print("cant Palabras: ",count_words)       
                    currentNode=listOfWords.head
                    while currentNode:
                        print("palabra: ",currentNode.value)
                        currentNode=currentNode.nextNode
            
            listOfWords.head= None


if __name__ == '__main__':
    listArguments= sys.argv
    print(listArguments)
    if len(listArguments)!= 3:
        if len(listArguments) > 3:
            path=listArguments[2]
            for idx in range(3,len(listArguments)):
                path +=" " +listArguments[idx]
                
            if os.path.exists(path):
                print("el path que pasa como parametro es: ",path)
                create(path)
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

    #PATH DE PRUEBA
    # py personal_library.py --create D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\proyecto-grupo4\ProyectoIntegrador\test_files
    # py personal_library.py -create D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\proyecto-grupo4\ProyectoIntegrador\test_files
    
    # py personal_library.py -create C:\Users\ULTRABYTES\Desktop\test_files
    # py personal_library.py --create C:\Users\ULTRABYTES\Desktop\test_files
