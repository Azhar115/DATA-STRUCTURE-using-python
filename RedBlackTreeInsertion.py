from FIFOQueue import FIFOQueue
class RedBlackTreeInsertion:
    "node color : True(red) false(black)"
    class __Node:
        def __init__(self):
            self.leftchild = None
            self.rightchild = None
            self.parentnode= None
            self.value = None
            self.color = None  # color can only be blue,red or black
    __rootNode =__Node()
    def __init__(self, value):
        self.__rootNode.leftchild =None
        self.__rootNode.rightchild = None
        self.__rootNode.parentnode =None
        self.__rootNode.value = value
        self.__rootNode.color = True # black
    def insert(self,value):
        newNode =self. __Node()
        newNode.leftchild = None
        newNode.rightchild = None
        newNode.value = value
        newNode.color = False
        tempNode = self.__rootNode
        while (True):
            # finding the plae to insert value in left sub tree of root node or parent node
            if tempNode.value >= value:
                # finding insertion point at left subtree of __rootNode
                if tempNode.leftchild == None:
                    # reached to insertion point
                    newNode.parentnode = tempNode
                    tempNode.leftchild = newNode
                    self.checkColorRules(tempNode.leftchild)
                    break
                else:
                    # iteration till we reach to the insertion point
                    tempNode = tempNode.leftchild

            else:
                # finding the insertion point at the right subtree of __rootNode or parent node
                if tempNode.rightchild == None:
                    # reached to insertion point
                    newNode.parentnode = tempNode
                    tempNode.rightchild = newNode
                    self.checkColorRules(tempNode.rightchild)
                    break
                else:
                    #iterating the right sub tree for insertion
                    tempNode = tempNode.rightchild
    def checkColorRules(self,Node):
        call = None
        if Node.color ==False and Node.parentnode.color ==False:
            if Node == Node.parentnode.leftchild:
                call = 'L'
            else:
                call = 'R'
            if Node.parentnode.parentnode.rightchild== Node.parentnode:
                if   Node.parentnode.parentnode.leftchild ==None or Node.parentnode.parentnode.leftchild.color != False: #red
                    call = call+'R'
                    if call =='LR':
                        self.LR_Rotation(Node)
                    elif call == 'RR':
                        self.RR_Rotation(Node)
                else:
                    #just change color parent node  and its children
                     Node.parentnode.color = True
                     if Node.parentnode.parentnode.leftchild !=None:
                         Node.parentnode.parentnode.leftchild.color = True #black
                     if Node.parentnode.parentnode.color ==True and Node.parentnode.parentnode !=self.__rootNode:
                         Node.parentnode.parentnode.color = False
                         self.checkColorRules(Node.parentnode.parentnode)
                     Node.parentnode.parentnode.color ==True

            else:
                if Node.parentnode.parentnode.rightchild == None or Node.parentnode.parentnode.rightchild.color != False:  # red
                    call = call+'L'
                    if call =='LL':
                         self.LL_Rotation(Node)
                    elif call == 'RL':
                         self.RL_Rotation(Node)
                else:
                    # just change color parent node  and its children
                     Node.parentnode.color = True
                     if Node.parentnode.parentnode.rightchild != None:
                         Node.parentnode.parentnode.rightchild.color = True
                     if Node.parentnode.parentnode.color == True and Node.parentnode.parentnode != self.__rootNode:
                         Node.parentnode.parentnode.color = False
                         self.checkColorRules(Node.parentnode.parentnode)
                     Node.parentnode.parentnode.color == True
        else:
            print('stable')

    def LL_Rotation(self,node):
        """
        LL_rotation is performed, where current node's parent parent shifted to right side of current node's parentnode
        :param node:  parent of parent of current node  rotation only
        :return:  None
        """
        #shifting the parentnode rightchild  to the node.parent.parent.leftchild
        if  node.parentnode.rightchild !=None:
            node.parentnode.parentnode.leftchild = node.parentnode.rightchild
            node.parentnode.parentnode.leftchild.parentnode = node.parentnode.parentnode

        #if parent has no rightchild then make parent.parent.left as None
        node.parentnode.parentnode.leftchild = None
        #shifting/making the node.parent.parent node as the node.parent.rightchild
        node.parentnode.rightchild = node.parentnode.parentnode  #as now the parent of node is parent of parent of that node
        #making node.parent.parent as the child of  node.parent.parent.parent
        node.parentnode.parentnode = node.parentnode.parentnode.parentnode
        #making the node.parent.parent as the child of node.parent
        node.parentnode.rightchild.parentnode = node.parentnode
        #now as it is fullfilled the red black tree conditions, change the color as parent node black
        node.parentnode.color = True #black
        node.parentnode.rightchild.color = False #red
        #print(node.value, 'changed')
        # if node.parent becomes root after shifting then make it as root
        if node.parentnode.parentnode == None:
            self.__rootNode = node.parentnode
            #no need to check red black tree anymore
            return
        else:
            # making the parent.parent.leftchild should refrence to new child
            node.parentnode.parentnode.leftchild = node.parentnode
            self.checkColorRules(node)
    def RR_Rotation(self,node):
        """
               RR_rotation is performed, where current node's parent of  parent shifted to left side of current node's parentnode
              :param node:  parent of parent of current node  rotation only
              :return:  None
               """
        #shifting the parent node left child as the parent.parent.rightchild
        if node.parentnode.leftchild !=None:
            node.parentnode.parentnode.rightchild = node.parentnode.leftchild
            node.parentnode.parentnode.rightchild.parentnode = node.parentnode.parentnode
        # parent has no left child than make the rightchild as None of parent.parent
        node.parentnode.parentnode.rightchild = None

        #now making/shifting the parent.parent as the left child of current node's parentnode
        node.parentnode.leftchild = node.parentnode.parentnode
        #making current node's parent of parent as the parent of shifted left child
        node.parentnode.parentnode = node.parentnode.parentnode.parentnode
        #making the shifted node parent as the current node's parent
        node.parentnode.leftchild.parentnode= node.parentnode
        #chaning the colors of parent and children
        node.parentnode.color = True #black
        node.parentnode.leftchild.color = False #red
        #making the parent node as root if no parent.parent node
        if node.parentnode.parentnode == None:
            self.__rootNode = node.parentnode
            return
        else:
            # making current node parent node as new right child of old child which shifted to left of current node parent
            node.parentnode.parentnode.rightchild = node.parentnode
            self.checkColorRules(node)

    def LR_Rotation(self,node):
        """
        first R conflict resolved  between current node and its parent
        second L conflict resolved  between current node and its parent of parent node
        third after conflict resolved current node parent and its children are recolored
        :param self: self.rootnode
        :param node: current node
        :return: none
        """
        # LR_conflic so L was node so make it null and on R was the previouse node parent so make it null

        #1st)solving the L conflict between left child and parent
        node.rightchild = node.parentnode
        node.parentnode.parentnode.rightchild = node
        node.parentnode =node.parentnode.parentnode
        # make the parent node and the parent.parent of node as node's children
        node.rightchild.parentnode = node
        node.rightchild.leftchild = None

        #2nd) solving the R conflict between right child and new parent
        node.leftchild = node.parentnode
        node.parentnode = node.parentnode.parentnode
        # make the parent node and the parent.parent of node as node's children
        node.leftchild.parentnode = node
        node.leftchild.rightchild = None
        #now conflic resolved changing the color as  node is parent to black and its children as red
        node.color = True # black
        node.rightchild.color = False #red
        node.leftchild.color = False # red
        # in last check if the node becomes root node other wise attach it to parent node
        if node.parentnode == None:
            self.__rootNode = node
        else:
            if node.parentnode.leftchild ==node.leftchild:
                node.parentnode.leftchild=node
            else:
                node.parentnode.rightchild=node
                print(node.value, 'changed')
                self.checkColorRules(node)
    def RL_Rotation(self,node):
        """
        first R conflict resolved  between current node and its parent
        second L conflict resolved  between current node and its parent of parent node
        third after conflict resolved current node parent and its children are recolored
        :param self: self.rootnode
        :param node: current node
        :return: none
        """
        #1st) solving the R conflic between node and its parent
        #shifting the parent node as the right child of node
        node.leftchild = node.parentnode
        node.parentnode.parentnode.leftchild = node
        node.parentnode = node.parentnode.parentnode
        node.leftchild.parentnode = node
        node.leftchild.rightchild = None

        #2nd) solving the L conflict betwenn node and its new parent
        node.rightchild = node.parentnode
        node.parentnode = node.parentnode.parentnode
        node.rightchild.parentnode = node
        node.rightchild.leftchild = None

        #changing the color as now node become parent
        node.color = True #black
        node.rightchild.color = False #red
        node.leftchild.color = False #red

        if node.parentnode ==None:
            self.__rootNode = node
            return
        else:
            self.checkColorRules(node)

    def LevelWisetraverseTree(self,root):
        """level wise traversing"""
        print('level wise printing left to right')
        print('True = black', ', False=red in coloring')
        traverseTree = FIFOQueue()
        tempNode = root
        print(tempNode.value,tempNode.color)

        while (True):
            # binery tree is not created yet.
            if tempNode == None:
                break
            # if node node has no child then jump to ceibling node in tree or next level node
            # if node has child then print the children and jump to next ceibling or new level
            if tempNode.leftchild != None:
                print(tempNode.leftchild.value,tempNode.leftchild.color)
                traverseTree.push(tempNode.leftchild)
            if tempNode.rightchild != None:
                    print(tempNode.rightchild.value,tempNode.rightchild.color)
                    traverseTree.push(tempNode.rightchild)
            tempNode = traverseTree.pop()
            if tempNode == None:
                break
                # print(tempNode.value)
    def getroot(self):
        return self.__rootNode

#test 1: insertion
#checked ok: with debuging : ok
#Bst = RedBlackTreeInsertion(6)
#Bst.insert(7)
#Bst.insert(8)
#Bst.insert(3)
#Bst.insert(2)
#Bst.insert(9)
#Bst.insert(10)
#Bst.insert(11)
#Bst.insert(7)
#print('--')
#Bst.LevelWisetraverseTree(Bst.getroot())






