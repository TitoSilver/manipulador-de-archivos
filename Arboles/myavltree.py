from algo1 import *
from mybinarytree import *
from utility import *
#==========================================#
#==========================================#

class AVLTree:
	root = None

class AVLNode:
  parent = None
  leftNode = None
  rightNode = None
  key = None
  value = None
  balanceFactor = None
  height = None

#==========================================#
          #FUNC ROTATE LEFT
#==========================================#

def rotateLeft(Tree,node):

  if node.rightNode and not node.leftNode:
    if node.rightNode.leftNode and not node.rightNode.rightNode:
      rotateRight(Tree,node.rightNode)
  
  newRoot= node.rightNode
  node.rightNode= newRoot.leftNode

  if newRoot.leftNode:
    newRoot.leftNode.parent= node
  
  newRoot.parent= node.parent

  if not node.parent:
    Tree.root= newRoot
  else:
    if node.parent.rightNode == node:
      node.parent.rightNode= newRoot
    else:
      node.parent.leftNode= newRoot


  newRoot.leftNode= node
  node.parent= newRoot

  return newRoot

#==========================================#
          #FUNC ROTATE RIGHT
#==========================================#

def rotateRight(Tree,node):

  if node.leftNode and not node.rightNode:
    if node.leftNode.rightNode and not node.leftNode.leftNode:
      rotateLeft(Tree,node.leftNode)

  newRoot=node.leftNode
  node.leftNode= newRoot.rightNode

  if newRoot.rightNode:
    newRoot.rightNode.parent= node

  newRoot.parent= node.parent

  if not node.parent:
    Tree.root= newRoot
  else:
    if node.parent.rightNode == node:
      node.parent.rightNode= newRoot
    else:
      node.parent.leftNode= newRoot
  
  newRoot.rightNode= node
  node.parent= newRoot

  return newRoot

#==========================================# 
          #BALANCE FACTOR
#==========================================#
def update_bf(Tree,node):

  updateHeight(Tree,node)


#==========================================#
          #avlInsert
#==========================================#

def avlInsert(Tree,element,key):
  node=AVLNode()
  node.value=element
  node.key= key

  if Tree.root==None:
    Tree.root= node
    return node
  else:
    node= recursiveInsert(node,Tree.root)
    
  update_bf(Tree,node)



#==========================================#
          #avlDelete
#==========================================#
def avlDelete(Tree,element):

  node= treeSearch(Tree,element)

  newNode= treeDelete(Tree,node.element)

  update_bf(Tree,newNode)