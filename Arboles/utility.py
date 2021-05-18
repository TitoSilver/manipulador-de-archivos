from algo1 import *
from myavltree import *

"""
En este file se encuentran todas las funciones recursivas que se implementa en myavltree
para dar mas claridad a las funciones.
"""


#==========================================#
          #RE BALANCE
#==========================================#

def reBalance(Tree,node):

  from myavltree import rotateRight, rotateLeft
  
  if node.balanceFactor< -1:
    rotateRight(Tree,node)
  else:
    rotateLeft(Tree,node)

#==========================================#
          #FUNC calculate_bf
#==========================================#


def calculate_bf(node):

  if not node.leftNode and not node.rightNode:
    node.balanceFactor= 0
  
  else:
    if node.leftNode and node.rightNode:

      node.balanceFactor= ( node.rightNode.height + 1 ) - ( node.leftNode.height + 1 )
    else:
      if node.leftNode:        
        node.balanceFactor=  -(node.leftNode.height + 1)
      else:

        node.balanceFactor= node.rightNode.height + 1

#==========================================#
          #FUNC updateHeight 
#==========================================#
def updateHeight(Tree,node):

  #Caso 1: No tiene ningun hijo
  if not node.leftNode and not node.rightNode:
    node.height= 0

  #Caso 2:Solo tiene hijo izq
  if node.leftNode and not node.rightNode:
    node.height= node.leftNode.height + 1
  
  #Caso 3:Solo tiene hijo derecho
  if not node.leftNode and node.rightNode:
    node.height= node.rightNode.height + 1
  
  #Caso 4: Tiene ambos hijos
  if  node.leftNode and node.rightNode:

    if node.leftNode.height > node.rightNode.height:
      node.height= node.leftNode.height + 1
    else:
      node.height= node.rightNode.height + 1

  calculate_bf(node)

  
  if node.balanceFactor < -1 or node.balanceFactor > 1:
    reBalance(Tree,node)
    return 

  #Condición de salida
  if  not node.parent:
    return

  updateHeight(Tree,node.parent)




