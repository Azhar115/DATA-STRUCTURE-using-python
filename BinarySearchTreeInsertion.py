from LIFOQueue import LIFOQueue
class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
class BinarySearchTreeInsertion :
    __rootNode =Node()

    def __init__(self,value):
        self.__rootNode.value = value
        self.__rootNode.left = None
        self.__rootNode.right = None

        pass

#debugged:ok
    def insert(self,value):

        newNode = Node()
        newNode.left =None
        newNode.right = None
        newNode.value = value
        tempNode = self.__rootNode
        while(True):
            #finding the plae to insert value in left sub tree of root node or parent node
            if tempNode.value>=value:
                #finding insertion point at left subtree of rootNode
                if tempNode.left==None:
                    #reached to insertion point
                    tempNode.left = newNode
                    break
                else:
                    #iteration till we reach to the insertion point
                    tempNode = tempNode.left

            else:
                #finding the insertion point at the right subtree of rootNode or parent node
                if tempNode.right==None:
                    #reached to insertion point
                    tempNode.right = newNode
                    break
                else:
                    tempNode = tempNode.right
    def inOrderRecursiveTraverse(self,root):
        """"Irorder traverse : leftnode ->rootnode->rightNode:
        it is sorting in ascending order traverse of bst """
        #traverse left subtree first
        if root.left!=None:
            self.inOrderRecursiveTraverse(root.left)
            print(root.value)
            if root.right == None:
                return
            else:
                self.inOrderRecursiveTraverse(root.right)
                return
        else:
            print(root.value)
            if root.right == None:
                return
            else:
                self.inOrderRecursiveTraverse(root.right)
                return

# inOrderTraverse: space complexity issue
# requires to store all nodes that is traversed before for avoiding stucking loop, and same values store also issue for checking if node already traversed
    def inOrderTraverse(self):
        tempNode = self.__rootNode
        traceParentTrverse = LIFOQueue() # for backtracking
        traceParentTrverse.push(tempNode)
        while(True):
            if tempNode.left != None:
                tempNode = tempNode.left
                traceParentTrverse.push(tempNode)

            else:
                print(tempNode.value)
                if tempNode.right ==None:
                    tempNode = traceParentTrverse.pop()
                    if tempNode==None:
                        break
                else:
                    tempNode = tempNode.right
                    traceParentTrverse.push(tempNode)



    def getroot(self):
         return self.__rootNode

#tested and debugged
BST = BinarySearchTreeInsertion(5)
for i in range(2,5):
    BST.insert(i)
for i in range(5,10):
    BST.insert(i)
BST.insert(4)
BST.insert(7)
BST.inOrderRecursiveTraverse(BST.getroot())
