class FIFOQueue:
    """ generic first in and first out basis Queue: can get any type of data """

    #def __int__(self,value):
    class __Node:
        def __init__(self):
            value = None
            nextNode = None
    #class attributes
    __outputPoint = None
    __lastinputPoint = None
    def __init__(self):
        pass

    def push(self,value):
        newNode = self.__Node()
        newNode.value = value
        newNode.nextNode = None
        # at the start of the queue
        if self.__lastinputPoint == None and self.__outputPoint == None:
            self.__lastinputPoint = newNode
            self.__outputPoint = newNode
        else:
            # each time new node is added
            self.__lastinputPoint.nextNode = newNode
            self.__lastinputPoint = newNode

    def  pop(self):
        """it returns the node of top first node value and deletes it from queue"""
        #when no node in queue
        if self.__outputPoint == None:
            return None
        #when only one node is in queue
        elif self.__outputPoint == self.__lastinputPoint:
            # getting value of firstnode
            temppointNode = self.__outputPoint
            temppointNodeValue = temppointNode.value
            # distroying the pop node
            temppointNode.nextNode = None
            del temppointNode
            # if temppointNode.nextNode == self.__outputPoint:
            #   print('yes')
            self.__outputPoint = None
            self.__lastinputPoint = None
            return temppointNodeValue

        #when more then one node in queue
        else:
            # getting value of firstnode
            temppointNode = self.__outputPoint
            # shifting to next node as first node to be output
            self.__outputPoint = self.__outputPoint.nextNode
            temppointNodeValue = temppointNode.value
            #distroying the pop node
            temppointNode.nextNode = None
            del temppointNode
            #if temppointNode.nextNode == self.__outputPoint:
            #   print('yes')
            return temppointNodeValue

    #printing lastnode value
    def  gettop(self):
        return self.__lastinputPoint.value

    def display_queue(self):
        temppoint = self.__outputPoint
        #printing values from queue till it reach last node
        while(temppoint != self.__lastinputPoint):
            tempvalue = temppoint.value
            temppoint = temppoint.nextNode
            print(tempvalue)
        #lastnode value is printed as it is not printed in while loop
        print(temppoint.value)

 #tested
#queue = FIFOQueue()
#queue.push(11)
#queue.push(12)
#queue.push(13)
#node = queue.pop()
#print(node)
#queue.display_queue()

