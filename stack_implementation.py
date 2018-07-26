class Stack :
    #Initialize the stack
    def __init__ (self) :
        self.stack = []
    #Check if the stack is empty o(1)
    def isEmpty(self) :
        return self.stack == [];
    #Push data into the stack  o(1)
    def push(self, data) :
             self.stack.append(data);
    #Pop data from the stack o(1)
    def pop(self) :
          data = self.stack[-1];
          del self.stack[-1];
          return data;
    #Check data item on the top of the stack o(1)
    def peek(self) :
        return self.stack[-1];
    #Check the size of the stack
    def size(self) :
        return len(self.stack);
