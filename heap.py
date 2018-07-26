
class Heap(object) :
      HEAP_SIZE = 10
      #intitalize the heap
      def __init__(self) :
            self.heap = [0]*HEAP_SIZE
            self.current_position = -1
    #insert an item into the heap o(logN)
      def insert(self,item) :
            if self.isFull() :
                print("Heap is Full")
                return
            self.current_position = self.current_position + 1
            self.heap[self.current_position] = item
            self.fixUp(self.current_position)
    #Check if the heap is full
      def isFull(self) :
            if self.current_position == Heap.HEAP_SIZE :
                 return True
            else :
                 return False
    #Ensure heap properties are satisfied by fixing or swapping accordingly
      def fixUp(self, index) :
            while  index >= 0 :
                if self.heap[index] > self.heap[int((index-1)/2)] :
                    temp = self.heap[int((index-1)/2)]
                    self.heap[int((index-1)/2)] = self.heap[index]
                    self.heap[index] = temp
                    self.fixUp(int((index-1)/2))
                if self.heap[index] > self.heap[int((index-2)/2)]   :
                    temp = heap[int((index-2)/2)]
                    self.heap[int((index-2)/2)] = heap[index]
                    self.heap[index] = temp
                    self.fixUp(int((index-2)/2))
 
