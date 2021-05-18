from myavltree import *
from redblacktree import *
from mybinarytree import traverseInPreOrder
from trie import *

if __name__=="__main__":
    """
    print("Main AVLTree")

    avlTree= AVLTree()

    avlInsert(avlTree,10,10)
    avlInsert(avlTree,20,20)
    avlInsert(avlTree,30,30)
    avlInsert(avlTree,4,4)
    avlInsert(avlTree,6,6)
    avlInsert(avlTree,5,5)

    print("==========================================================")
    print("Tree.root: ",avlTree.root.key)

    print("Main RBTree")

    
    RBTree=RedBlackTree()

    print("Se inserto nodo 10")
    RBInsert(RBTree,10,10)

    print("Se inserto nodo 20")
    RBInsert(RBTree,20,20)

    print("Se inserto nodo 5")
    RBInsert(RBTree,5,5)    

    print("Se inserto nodo 1")
    RBInsert(RBTree,1,1)

    print("Se inserto nodo 8")
    RBInsert(RBTree,8,8)

    print("Se inserto nodo 6")
    RBInsert(RBTree,6,6)

    print("Se inserto nodo 25")
    RBInsert(RBTree,25,25)

    print("Se inserto nodo 7")
    RBInsert(RBTree,7,7)


    path= traverseInPreOrder(RBTree)

    node=path.head

    while node:
        print(node.value)
        node=node.nextNode

    print("====================================")    

    """
    print("Main Trie")
    
    print("====================================")    

    trie= Trie()

    trie.root= TrieNode()

    print("Insert: hola")
    TrieInsert(trie,"hola")
    
    print("Insert: galperon")
    TrieInsert(trie,"galperon")
    
    print("====================================")    
    
    value= TrieSearch(trie,"hola")
    
    print("search hola: ",value)
    
    value= TrieSearch(trie,"galperon")
    
    print("search galperon: ",value)
    
    value= TrieSearch(trie,"holu")
    
    print("search holu: ",value)
    
    value= TrieSearch(trie,"holanda")
    
    print("search holanda: ",value)
    
    
    print("====================================") 
    
    TrieDelete(trie,"galperon")
    
    print("====================================") 
    print("despeus del delete de galperon: ")
    
    value= TrieSearch(trie,"galperon")
    
    print("search galperon: ",value)