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
        if (element== " " or element== "\n" )and word =="":
            continue        
        else:
            if element=="\n" or element==".":
                continue
            if element== " " or element=="," or element==".":
                count_words += 1
                addValue(list_of_words,word)
                word= ""
            else:
                word += element

    count_words += 1
    addValue(list_of_words,word)
    
    #retorna la cantidad de palabras y la lista de palabras
    #en la linea
    
    """
    print("count_words: ",count_words)
    
    currentNode= list_of_words.head
    
    while currentNode:
        print("lista de palabras:", currentNode.value)
        currentNode= currentNode.nextNode
    
    """
    

    return count_words, list_of_words
"""
travel_line("hola como estas
            yo
            coso
            
            mundo")

"""
