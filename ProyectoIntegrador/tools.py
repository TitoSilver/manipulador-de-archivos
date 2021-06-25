# -*- coding: utf-8 -*-

from mydictionary import *
from linkedlist import *

def travel_line(line):
    #print("line: ",line)
    count_words= 0
    list_of_words= LinkedList()
    word= ""
    if line== "\n":
        return 0, None
    for element in line:
        element= element.lower()
        
        if ord(element) in range(48, 58) or ord(element) in range(65,91) or ord(element) in range(97,123):
            #Siendo las cifras desde (48,57)
            #Siendo las letras mayusculas (65,90)
            #Siendo las letras minusculas (97,122)
            #se agrega un elemento mas al range para que incluya la cifra.
            word += element
        else:
            if ord(element)== 8217 or ord(element)==39 or ord(element)==45:
                #elemento especial(" ’ ") ; elemento especial (" ' ") ; elemento especial (" - ")
                word += element
            else:
                if word!="":
                    count_words += 1
                    addValue(list_of_words,word)
                    word=""
                else:
                    continue
            
        """
        if (element== " " or element== "\n" or element == "•")and word =="":
            continue
        else:
            if element=="\n" or element=="." or element == "•":
                continue
            if element== " " or element=="," or element==".":
                count_words += 1
                #print("word a agregar: ",word)
                addValue(list_of_words,word)
                word= ""
            else:
                word += element
        """
    if word!= "":
        count_words += 1        
        addValue(list_of_words,word)
        
    return count_words, list_of_words
    
    #retorna la cantidad de palabras y la lista de palabras
    #en la linea
    
    """
    print("count_words: ",count_words)
    
    currentNode= list_of_words.head
    
    while currentNode:
        print("lista de palabras:", currentNode.value)
        currentNode= currentNode.nextNode
    
    """
    

    
"""
travel_line("hola como estas
            yo
            coso
            
            mundo")

"""
