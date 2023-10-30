from FIFOQueue import FIFOQueue
from LIFOQueue import LIFOQueue
class Node:
    def __int__(self):
        self.leftchild = None
        self.rightchild = None
        self.value = None
class BineryTree:
    nodesQueue = FIFOQueue()
    rootNode = Node()
    insertionPointNode = None  # node where left or right child  side node will be inserted
    def __init__(self,value1):
        self.rootNode.leftchild = None
        self.rootNode.rightchild = None
        self.rootNode.value = value1
        self.insertionPointNode = self.rootNode
    def  insert(self,value):
        newNode = Node()
        newNode.value = value
        newNode.leftchild = None
        newNode.rightchild = None
        self.nodesQueue.push(newNode)
        #inserting on leftchild or right side of current node
        if self.insertionPointNode.leftchild == None:
            self.insertionPointNode.leftchild = newNode
        elif self.insertionPointNode.rightchild == None  :
            self.insertionPointNode.rightchild = newNode
        else:
            #if insertionpoint has both left and right child then next node which will don't have both lift and right will be selected,and lift child be attacjed
            #print(self.insertionPointNode.value)
            self.insertionPointNode = self.nodesQueue.pop()
            #print(self.insertionPointNode.value)
            self.insertionPointNode.leftchild = newNode
            #print(self.insertionPointNode.value,self.insertionPointNode.leftchild.value)

#tested : ok, debug : ok
    def  LevelWisetraverseTree(self):
        """level wise traversing"""
        traverseTree = FIFOQueue()
        tempNode = self.rootNode
        print(tempNode.value)
        while(True):
            #binery tree is not created yet.
            if tempNode ==None :
                break
            #if node node has no child then jump to ceibling node in tree or next level node
            #if node has child then print the children and jump to next ceibling or new level
            elif tempNode.leftchild != None:
                print(tempNode.leftchild.value)
                traverseTree.push(tempNode.leftchild)
                if tempNode.rightchild != None :
                    print(tempNode.rightchild.value)
                    traverseTree.push(tempNode.rightchild)
                tempNode = traverseTree.pop()
            else:
                #print('called')
                tempNode = traverseTree.pop()
                if tempNode == None:
                    break
                #print(tempNode.value)
    def preOrderTraverse(self):
        """ function with no functional recursive call
         Traversing technique : parentNode -> ParentNode.leftchild -> ParentNode.rightchild"""

        tempNode = self.rootNode
        print(tempNode.value)
        #Lastin and first out queue stores the parent Node for tracing back from depth
        traceParent = LIFOQueue()
        while(True):
            #checking if parent has leftchild then print
            if tempNode.leftchild != None:
                print(tempNode.leftchild.value)
                traceParent.push(tempNode)
                tempNode = tempNode.leftchild
            elif tempNode.rightchild != None:
                print(tempNode.rightchild.value)
                traceParent.push(tempNode)
                tempNode = tempNode.rightchild

            else:
                #beaktracking to the parent node from left child node when it has no sub_children
               tempNode = traceParent.pop()
               if tempNode ==None:
                   break
               #prefix traverse the left child first so now to right child traversing
               if tempNode.rightchild ==None:
                   tempNode = traceParent.pop()
                   #shows all tree is traversed

                   if tempNode == None:
                       break
               tempNode = tempNode.rightchild
               print(tempNode.value)



    def getRootNode(self):
        return self.rootNode

    def    preOrderTraverseByRecursiveCall(self,root):
        """"
        Traversing the tree by recursive call as : preOrderTraverseByRecursiveCall(root,leftChild,rightChild)
        reason of recursive : to trace back to the parent node from depth
        """
        #root is printed
        if root == self.rootNode:
            print(root.value)
        #if left child is not null print it
        if root.leftchild != None:
            print(root.leftchild.value)
            #print root left child of sub left children
            self.preOrderTraverseByRecursiveCall(root.leftchild)
            # print root left child of sub right children
            if root.rightchild != None:
                print(root.rightchild.value)
                self.preOrderTraverseByRecursiveCall(root.rightchild)
        #print the right child sub children
        elif root.rightchild != None:
            print(root.rightchild.value)
            self.preOrderTraverseByRecursiveCall(root.rightchild)
        #return the root when its right and left child is printed
        return

    def postOrderTraverse(self):
        parentNodeTrace = LIFOQueue()
        tempNode = self.rootNode
        lastprintNode =None  # it is used to avoid stucking in infinite loop
        while True:
            if tempNode.leftchild != None:
                parentNodeTrace.push(tempNode)
                tempNode = tempNode.leftchild

            else:
                #i) root left sub tree printing
                #1st) printing the parent left child having no sub children
                print(tempNode.value)
                lastprintNode = tempNode
                #2nd) now iterating the the parent right child sub children
                tempNode = parentNodeTrace.pop()
                # runs till parent all right child sub children is not printed
                if tempNode.rightchild !=None and tempNode.rightchild !=lastprintNode:
                    parentNodeTrace.push(tempNode)
                    tempNode = tempNode.rightchild
                # runs when parent all left and right sub children are printed
                #3rd)left subtree completed last node is not printed
                else:
                     # last sub left tree node is printed
                     print(tempNode.value)
                     lastprint1Node =tempNode
                     #right subtree from root is gonna be printed
                     tempNode = parentNodeTrace.pop()
                     #if all tree is traveresed except rout
                     if tempNode ==None:
                         break
                     #left sub tree of root node is traversed, now ride side of root subtree traversing
                     if tempNode.rightchild !=lastprint1Node:
                        parentNodeTrace.push(tempNode)
                        tempNode = tempNode.rightchild
    def postOrderTraverseByRecursiveCall(self,root):
        #if root has left child
        if root.leftchild != None:
            #1)print left of parent or root node
            self.postOrderTraverseByRecursiveCall(root.leftchild)
            if root.rightchild != None:
            # 2) print right child of parent or root node
                self.postOrderTraverseByRecursiveCall(root.rightchild)
                print(root.value)
            else:
                #3) print the parent or root node
                print(root.value)

        else:
            #otherwise print root as it has no node
            print(root.value)
            return
    def inOrderTraversing(self):
        tempNode = self.rootNode
        parentNodeTrace =LIFOQueue()
        while(True):
            if tempNode.leftchild != None:
                parentNodeTrace.push(tempNode)
                tempNode = tempNode.leftchild
            else:
                print(tempNode.value)
                tempNode = parentNodeTrace.pop()
                if tempNode ==None:
                    break
                if tempNode.rightchild !=None:
                    print(tempNode.value)
                    tempNode = tempNode.rightchild
                else:
                    print(tempNode.value)
                    tempNode = parentNodeTrace.pop()
                    if tempNode ==None:
                        break
                    print(tempNode.value)
                    if tempNode.rightchild !=None:
                        tempNode = tempNode.rightchild
















#tested insertion: okay, debugging: ok:
#tested LevelWisetracerseTree : Ok;
#tested preOrderTraverse : ok, debugging : ok
#tested preOrderTraverseByRecursiveCall :ok, debugging : ok

bitree = BineryTree(1)
#tested for hug data set
for i in range(2,8):
    bitree.insert(i)
print('\n---------level wise traverse ')
bitree.LevelWisetraverseTree()
print('------------prefix traverse-----------')
bitree.preOrderTraverse()
print('----------------prerder traverse using recursive call----------')
bitree.preOrderTraverseByRecursiveCall(bitree.getRootNode())
print('----------postorder traverse using no recursive call---')
bitree.postOrderTraverse()
print('----------post traverse with recursive call-------')
bitree.postOrderTraverseByRecursiveCall(bitree.getRootNode())
print('---------inOrderTraversing-----------------')
bitree.inOrderTraversing()












