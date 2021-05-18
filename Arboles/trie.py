from algo1 import *
from linkedlist import *
#=========================================#
class Trie:
    root = None

class TrieNode:
    parent= None
    children= None
    key= None
    isEndOfWorld= False

#=========================================#
               #INSERT
#=========================================#

def TrieInsert(trie,element):

    parent= trie.root
    node= parent.children    
    
    for idx in range(0,len(element)):
        charInsert= TrieNode()
        charInsert.key= element[idx]
        
        if node:
            currentNode= node.head
            while currentNode:
                if currentNode.value.key== element[idx]:
                    node= currentNode
                    parent= charInsert
                    break
                
                currentNode=currentNode.nextNode
            else:
                add(node,charInsert)
        else:
            
            node=LinkedList()
            add(node,charInsert)
        
        charInsert.parent= parent
        parent.children= node
                
        parent=charInsert
        node=charInsert.children
        
        if idx+1== len(element):
            charInsert.isEndOfWorld= True 

#=========================================#
               #SEARCH
#=========================================#

def searchNode(node,element):
    
    for idx in range (0,len(element)):
        
        if element[idx]== node.value.key and node.value.isEndOfWorld==True and idx+1== len(element):
            return node
        
        while node:
            if node.value.key==element[idx] and node.value.children:
                node= node.value.children.head
                break
            node=node.nextNode
            
            
        else:
            return False

def TrieSearch(trie,element):
    node= trie.root.children.head
    
    result= searchNode(node,element)
    if result:
        return True
    else:
        return False
    
    


#=========================================#
               #DELETE
#=========================================#
def deleteNode(node):
    
    currentNode=node.parent.children.head 
    #print("currentNode.value.key: ",currentNode.value.key)
    if currentNode.nextNode:
        return
    else:
        parent=currentNode.value.parent
        #print("parent.value.key: ",parent.key)
        parent.children=None
        deleteNode(parent)
        
          

def TrieDelete(trie,element):
    
    node=trie.root.children.head
    
    result= searchNode(node,element)
    
    #print("result es: ",result.value.key)
    if result:        
        deleteNode(result.value)
        return True
    else:
        return False

    