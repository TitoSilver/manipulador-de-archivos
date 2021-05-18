from algo1 import *
from mydictionary import *
from myarray import *
from practica import *

if __name__ == '__main__':
    
    print("=============================")
    print("Hash Table")
    
    A= Array(5,Dictionary())
    
    dictInsert(A,0,10)
    
    dictInsert(A,1,20)
    
    dictInsert(A,2,30)
    
    dictInsert(A,3,40)
    
    dictInsert(A,6,50)
    
    for element in A:
        if element:
            currentNode= element.head
            while currentNode:
                print("({0}:{1})".format(currentNode.value.key,currentNode.value.value))
                currentNode= currentNode.nextNode
            print(",")
        else:
            print("None")

    print("")

    print("=============================")
    print("el valor de la llave 1 es: ",dictSearch(A,1))

    print("=============================")

    dictDelete(A,6)
    
    for element in A:
        if element:
            currentNode= element.head
            while currentNode:
                print("({0}:{1})".format(currentNode.value.key,currentNode.value.value))
                currentNode= currentNode.nextNode
            print(",")
        else:
            print("None")

    print("")
        
    
    print("=============================")
    print("IGUAL STRING")
    
    value= igualString("nanana","naaaan")   #arreglar este caso
    
    print("text1 == text1: ",value)
    
    
    print("=============================")
    print("ELEMENTOS UNICOS")
    
    AA=[1,2,3,4,10,1]
    
    print("El Array: {0} Tiene elementos unicos: {1}".format(AA,unicElements(AA)))
    
    print("=============================")
    print("codigo postal")
    
    iso3166= codPostal("Pringles 1485,Mendoza")
    
    print("iso3166: {}".format(iso3166))
    
    
    print("=============================")
    print("String Comprimida")
    
    valor= comprexString("aabcccccaaa")
    
    print(" el string [aabcccccaaa]: ",valor)