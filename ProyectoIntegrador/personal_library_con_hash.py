from mydictionary import *
from linkedlist_diego import *
from test_files import *
import os
from tools import *
from hashtable import *

class Node_file:
    def __init__(self,name_file,hash_of_words):
        self.nameFile: name_file
        self.hash_of_words: hash_of_words
        
list_file= LinkedList()
def create (path):

    #path = open(r"D:\Proyecto\Test_files")
    path= r"D:\Proyecto\Test_files"
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
                    
                    #add(list_file,Node_file(fileNameOnly,listOfWords))
                    print("cant Palabras: ",count_words)       
                    currentNode=listOfWords.head
                    while currentNode:
                        print("palabra: ",currentNode.value)
                        currentNode=currentNode.nextNode

                    m = primo_mayor(count_words) #encuentra el primo mayor al numero de palabras en el archivo.
                    T = Array(m,LinkedList()) #crea la tabla.
                    current = listOfWords.head 
                    while current != None: #inserta cada palabra en la tabla.
                      insertHash(T,current.value)

                    add(list_file,T) #agrega la tabla con las palabras a la LinkedList.
            listOfWords.head= None