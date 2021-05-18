from algo1 import *
from linkedlist import *
#####################################################
#####################################################
class BinaryTree:
  root= None

class BinaryTreeNode:
  key=None
  value=None
  leftNode=None
  rightNode=None
  parent=None

#####################################################
##################################################### #F U N C I Ó N   S E A R C H
def recursiveSearch(currentNode,element):
  if element== currentNode.value:
    return currentNode
  if currentNode.leftNode!= None:
    result= recursiveSearch(currentNode.leftNode,element)
    if result!= None:
      return result
  
  if currentNode.rightNode!=None:
    result= recursiveSearch(currentNode.rightNode,element)
    if result!=None:
      return result  
  return None


#####################################################
def treeSearch(Tree,element):
  if Tree.root== None:
    return None
  currentNode= Tree.root
  result= recursiveSearch(currentNode,element)

  if result!=None:
    return result

  return None

####################################################
####################################################  #F U N C I Ó N  I N S E R T
def recursiveInsert(node,parent):
  if parent.key< node.key:

    if parent.rightNode== None:
      parent.rightNode= node
      node.parent= parent
      return node
    else:
      return recursiveInsert(node,parent.rightNode)
  elif parent.key> node.key:

    if parent.leftNode== None:
      parent.leftNode= node
      node.parent= parent
      return node
    else:
      return recursiveInsert(node,parent.leftNode)
  else:
    return None
####################################################
def treeInsert(binaryTree,element,key):
  node=BinaryTreeNode()
  node.value=element
  node.key= key

  if binaryTree.root==None:
    binaryTree.root= node
    return node
  else:    
    return recursiveInsert(node,binaryTree.root)
####################################################
####################################################  #F U N C I Ó N  D E L E T E
def higher_minimum(node):

  if not node.leftNode:
    return node

  if node.leftNode:
    higher_minimum(Tree,node.leftNode)
  
####################################################
def treeDelete(Tree,element):
  if Tree.root==None:
    return None
  else:    
    node=recursiveSearch(Tree.root,element)

    if node.value!=None:
      if node.rightNode==None and node.leftNode==None:
        node= node.parent
        if node.rightNode.value==element:
          node.rightNode= None
          return node
        else:
          node.leftNode= None
          return node
      else:
        if not node.leftNode:
          newNode= rightNode

          node.parent.rightNode=newNode
          newNode.parent= node.parent

          return newNode

        if not node.rightNode:
          newNode= node.leftNode

          node.parent.leftNode= newNode
          newNode.parent= node.parent

          return newNode

        newNode= higher_minimum(node.rightNode)
        newNode.rightNode=node.rightNode
        newNode.leftNode= node.leftNode
        if Tree.root== node:
          Tree.root= newNode
          newNode.parent= None

        else:
          node.parent.rightNode= newNode
          newNode.parent= node.parent

        return newNode
    else:
      return None

####################################################
#     #     ##     ##     ##     ##     ##     ##  #  #RECORRIDO DEL ARBOL 
####################################################
def preOrderPath(L,treeNode):
  if treeNode.key!=None:
    n=length(L)
    insert(L,treeNode.key,n)

  if treeNode.leftNode!=None:      
    preOrderPath(L,treeNode.leftNode)

  if treeNode.rightNode!=None:
    preOrderPath(L,treeNode.rightNode)

  return L

####################################################
def traverseInPreOrder(binaryTree):

  L= LinkedList()

  if binaryTree.root==None:
    return None
  else:
    return preOrderPath(L,binaryTree.root)

####################################################
####################################################
def inOrderPath(L,treeNode):

  if treeNode.leftNode!=None:
    inOrderPath(L,treeNode.leftNode)
  
  n=length(L)
  insert(L,treeNode.key,n)

  if treeNode.rightNode!=None:
    inOrderPath(L,treeNode.rightNode)

  return L

####################################################
def traverseInOrder(binaryTree):
  L= LinkedList()

  if binaryTree.root==None:
    return None
  else:
    return inOrderPath(L,binaryTree.root)
####################################################
####################################################
def postOrderPath(L,binaryTree):  #NO TERMINADO
  if treeNode.leftNode!=None:
    postOrderPath(L,binaryTree.leftNode)
    


  pass


####################################################
def traverseInPostOrder(binaryTree):

  if binaryTree.root==None:
    return None
  else:
    L= LinkedList()
    return postOrderPath(L,binaryTree.root)

####################################################
####################################################