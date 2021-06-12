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
    print("llega aca1")
    path= r"D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\ProyectoIntegrador\test_files"
    print("llega aca2")
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
        print("Por favor ingrese una instrucción valida")
        print (os.getcwd())
        
    elif listArguments[1]== "--create" :
        create("hola")
    
    elif listArguments[1]== "--search":
        print("uwu")
    else:
        print("Por favor ingrese una instrucción valida")

    















            
"""
list_file= LinkedList()

class Node_file:
    def __init__(self,name_file,hash_of_words):
        self.nameFile: name_file
        self.hash_of_words: hash_of_words

path= r"D:\Back up\FACULTAD\Algoritmos y Estructura de Datos II\codigo\ProyectoIntegrador\test_files"

arr_files = os.listdir(path)

print(arr_files)
        
list_prev= LinkedList()

for file in arr_files:
    uwu=file
    if ".txt" in file:
        with open(path+"\\"+file,"r") as file:
            lines= file.readlines()
            count_words= 0
            count_line= 0
            for line in lines:
                count_words_in_line, list_of_words_in_line= travel_line(line)
                count_words += count_words_in_line
    add(list_prev,ContainerWords(uwu,list_of_words_in_line))

currentNode= list_prev.head
while currentNode:
    print("Dentro del archivo: ",currentNode.value.nameFile)
    intoCurrent=currentNode.value.list_of_line_words.head
    while intoCurrent:
        print(intoCurrent.value)
        intoCurrent= intoCurrent.nextNode
    
    currentNode=currentNode.nextNode

"""

    
"""
with open(path+"\\"+file,"r") as path_file:
    size_hash= sum(1 for _ in path_file if _.rstrip("\n"))
    
    hash_of_words= Array(size_hash,Dictionary())
    print("file: {0} y cant_lineas: {1}".format(file,size_hash))

with open(path+"\\"+file,"r") as file:
    lines= file.readlines()
    
    for line in lines:

"""

