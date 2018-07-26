class Queue :
    #Initialize the Queue with the help of an array or list
    def __init__(self) :
        self.queue = []
    #Check if the Queue is empty o(1)
    def isEmpty(self) :
        return self.queue == []
    #Add data to the queue o(1)
    def enqueue(self, data) :
        self.queue.append(data)
    #Remove data from the queue o(N)
    def dequeue(self) :
        data = self.queue[0]
        del self.queue[0]
        return data
    #Check the first in value at the queue o(1)
    def peek(self) :
        return self.queue[0]
    #Check the size of the queue
    def sizequeue(self) :
        return len(self.queue)
