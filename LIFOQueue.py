class LIFOQueue:
    """genereic last in first out basis Queue: accept any type of data"""
    class __Node :
        def __init__(self):
            self.value = None
            self.nextNode = None
            self.previouseNode =None
    __inputOutputPoint = None
    def __init__(self):
        pass
    def   push(self,value):
        newNode = self.__Node()
        newNode.nextNode = None
        newNode.value = value
        #first node in queue
        if  self.__inputOutputPoint ==None :
            newNode.previouseNode = None
            self.__inputOutputPoint =newNode
        else:
            #currentNode will become the previouse node of newNode
            newNode.previouseNode = self.__inputOutputPoint
            self.__inputOutputPoint = newNode
    def  pop(self):
        #Queue is already empity
        if self.__inputOutputPoint == None :
            return None

        #Queue having one or more nodes
        tempNode = self.__inputOutputPoint
        self.__inputOutputPoint = self.__inputOutputPoint.previouseNode
        #separating the node from queue
        tempNode.previouseNode =None
        tempNodevalue = tempNode.value
        #distroying the noe
        tempNode = None
        del tempNode
        return tempNodevalue

    def display(self):
        tempNode = self.__inputOutputPoint
        while(True):
            if tempNode ==None:
                break
            else:
                #iterating the queue in FILO sequence
                print(tempNode.value)
                tempNode = tempNode.previouseNode

#testing
#works fine push,pop() both
#queue = LIFOQueue()
#queue.push(3)
#queue.push(4)
#queue.push(5)
#queue.push(6)
#value = queue.pop()
#print(value)
#queue.display()
