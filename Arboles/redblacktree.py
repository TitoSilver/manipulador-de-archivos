from algo1 import *
from myavltree import *

#=================================#

class RedBlackTree:
    root= None

class RedBlackNode:
    parent= None
    leftNode= None
    rightNode= None
    key= None
    value= None
    color = None

#=================================#

def RBInsertNode(Tree,node):
    parent= Tree.root
    new_parent= None
    while parent:
        new_parent= parent
        if node.key < parent.key:
            parent= parent.leftNode
        else:
            parent= parent.rightNode
    
    node.parent= new_parent

    if not new_parent:
        Tree.root= node
    elif node.key < new_parent.key:
        new_parent.leftNode= node
    else:
        new_parent.rightNode= node

def RBInsertFixup(Tree,node):

    while node!= Tree.root and node.parent.color== "RED":
        if node.parent== node.parent.parent.leftNode: #Analiza el caso del padre izq
            uncle=node.parent.parent.rightNode
            
            if uncle and uncle.color== "RED":           #Caso 1
                node.parent.color= "BLACK"                #
                uncle.color= "BLACK"                      #
                node.parent.parent.color= "RED"                 #
                node= node.parent.parent                #Caso 1
            else:
                if node== node.parent.rightNode:          #Caso 2
                    node= node.parent                       #
                    rotateLeft(Tree,node)                 #Caso 2
            
                node.parent.color= "BLACK"                  #Caso 3
                node.parent.parent.color= "RED"               #
                rotateRight(Tree,node.parent.parent)        #Caso 3
        else:
            uncle= node.parent.parent.leftNode

            if uncle and uncle.color== "RED":
                node.parent.color= "BLACK"
                uncle.color= "BLACK"
                node.parent.parent.color= "RED"
                node= node.parent.parent
            else:
                if node== node.parent.leftNode:
                    node.node.parent
                    rotateRight(Tree, node)
                
                node.parent.color= "BLACK"
                node.parent.parent.color= "RED"
                rotateLeft(Tree, node)

    Tree.root.color= "BLACK"

def RBInsert(Tree,value,key):

    node=RedBlackNode()
    node.key= key
    node.value= value
    node.leftNode= None
    node.rightNode= None
    node.color= "RED"

    RBInsertNode(Tree,node)

    RBInsertFixup(Tree,node)

#=================================#

def RBTransplant( Tree,oldNode,newNode):
    if not oldNode.parent:
        Tree.root= newNode
    elif oldNode == oldNode.parent.leftNode:
        oldNode.parent.leftNode= newNode
    else:
        oldNode.parent.rightNode= newNode
    newNode.parent= oldNode.parent

def RBDeleteFixup(Tree,node):
    while node != Tree.root and node.color== "BLACK":
        if node==node.parent.leftNode:  #nodo izquierdo
            newNode=node.parent.rightNode
            if newNode.color == "RED":
                newNode.color= "BLACK"
                node.parent.color= "RED"
                rotateLeft(Tree,node.parent)
                newNode= node.parent.rightNode
            if newNode.color =="BLACK" and newNode.rightNode.color== "BLACK":
                newNode.color= "RED"
                node= node.parent
            elif newNode.rightNode.color== "BLACK":
                newNode.leftNode.color= "BLACK"
                newNode.color= "RED"
                rotateRight(Tree,newNode)
            newNode.color= node.parent.color
            node.parent.color= "BLACK"
            newNode.rightNode.color= "BLACK"
            node= Tree.root
        else:
            newNode=node.parent.leftNode
            if newNode.color== "RED":
                newNode.color= "BLACK"
                node.parent.color= "RED"
                rotateRight(Tree, node.parent)
                newNode= node.parent.leftNode
            if newNode.color== "BLACK" and newNode.leftNode.color== "BLACK":
                newNode.color= "RED"
                node= node.parent
            elif newNode.leftNode.color== "BLACK":
                newNode.rightNode.color= "BLACK"
                newNode.color= "RED"
                rotateLeft(Tree, newNode)
            newNode.color= node.parent.color
            node.parent.color= "BLACK"
            newNode.leftNode.color= "BLACK"
            node= Tree.root
        
    node.color= "BLACK"

def RBDelete (tree, node):
    flag= node
    flagColor= flag.color
    if not node.leftNode:
        newNode= node.rightNode
        RBTransplant(Tree,node,newNode)
    elif not node.rightNode:
        newNode= node.leftNode
        RBTransplant(Tree,node,newNode)
    else:
        flag= TreeMinimum(node.rightNode) #Crear Minimum
        flagColor= flag.color

        newNode=flag.rightNode #None

        if flag.parent == node:
            newNode.parent= flag
        else:
            RBTransplant(Tree,flag,flag.rightNode)
            flag.rightNode= node.rightNode
            flag.rightNode.parent= flag
        
        RBTransplant(Tree,node,flag)
        flag.leftNode= node.leftNode
        flag.leftNode.parent= flag
        flag.color= node.color
    
    if flagColor == "BLACK":
        RBDeleteFixup(Tree,newNode)

        