class Node:

    def __init__(self):
        self.nextNode = None
        self.previouseNode = None
        self.value = None
        self.index =None

    def  indexvalue(self):
        return self.index



class doubleLinkList:
    __indexincremental = -1
    headNode = Node()
    currentNode = Node()

    #tested
    def __init__(self,value):
        #object attributes

        self.headNode.nextNode =None
        self.headNode.previouseNode = None
        self.headNode.value = value
        self.headNode.index = self.index()
        self.currentNode = self.headNode

    #tested
    def  insert(self,value):
        #inserting when list is empity
        #1st) creating a temperary node
        newNode = Node()
        newNode.value = value
        newNode.nextNode = self.currentNode.nextNode
        newNode.previouseNode = self.currentNode
        newNode.index= self.index()
        #attaching the new created node with current list
        self.currentNode.nextNode = newNode
        self.currentNode = newNode
    #tested
    def insertRandomLocation(self,location:int,value):
        #finding index where to put the new index in between
        newNode = Node()
        newNode.index = location  #providing the index where it has to be inserted
        newNode.value = value
        newtempNode1= Node()
        newtempNode1 = self.findNodebyIndex(location) # storing the node which is already in that index
        if(newtempNode1 == None):
            print("list is not filled till that index")
            return
       # print(newtempNode1.value)
        newNode.previouseNode = newtempNode1.previouseNode
        newNode.nextNode = newtempNode1
        newtempNode1.previouseNode.nextNode = newNode
        newtempNode1.previouseNode = newNode
       #print(newNode.value,newtempNode1.index)
        while(newtempNode1 != self.currentNode):
            newtempNode1.index = newtempNode1.nextNode.index
            newtempNode1 = newtempNode1.nextNode
        self.currentNode.index =self.index()
        #print(newNode.value, n.index)
    def index(self):
        """" increments each time new node is created"""
        self.__indexincremental +=1
        return self.__indexincremental
    def lastNodeIndex(self):
        return  self.__indexincremental

    # tested
    def listDisplay(self):
        """"display in discending order"""
        response=input('do you want to print the list in Desc(D) or Ascending order(A): ').lower()
        #tested
        #display in discending order
        if(response == 'd' or response == 'desc'):
         #printing in descending order
            newNode = Node()
            newNode = self.currentNode
            while(True):
                print(newNode.value,newNode.indexvalue())
                newNode = newNode.previouseNode
                if(newNode == None):
                    break
        #tested
        #display in ascending order
        else:
            newNode = Node()
            newNode = self.headNode
            print(self.headNode.nextNode)
            while(True):
                print(newNode.value,newNode.indexvalue())
                newNode = newNode.nextNode
                if(newNode == None):
                    break
    def findNodebyIndex(self,value:int):
        newtempNode = Node()
        newtempNode = self.headNode
        tempIndex =newtempNode.indexvalue()
        while(True):
            if(tempIndex == value):
                return newtempNode
            else:
                newtempNode = newtempNode.nextNode
                tempIndex =newtempNode.indexvalue()
        return  None
    def getValueByIndex(self,value:int):
        newtempNode = self.findNodebyIndex(value)
        return newtempNode.value


#main test body
list = doubleLinkList(10)
list.insert(11)
list.insert(12)
list.insert(13)
list.insert(14)
index_position=int(input("enter the location where to insert the value: "))
if (index_position > list.lastNodeIndex()) or (index_position<0):
    while(True):
        print("please Enter the vailed index, list last index is ",list.lastNodeIndex())
        index_position = int(input("enter the location where to insert the value: "))
        if (index_position < list.lastNodeIndex()) and (index_position>=0):
            break
index_value=input("Enter the value to be inserted in that index: ")
index_enter=int(input("find value by index: "))
print(list.getValueByIndex(index_enter+1))
list.insertRandomLocation(index_position,index_value)
list.listDisplay()
#print(list.index())
