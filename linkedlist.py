class LinkedList(object) :
    def __init__(self) :
        self.head = None;
        self.size = 0;
     #o(1) Insert item at the start of the liked list
    def insertStart(self, data) :
        self.size = self.size + 1 ;
        newNode = Node(data);
        if not self.head:
            self.head = newNode;
        else :
            newNode.nextnode = self.head;
            self.head = newNode;
    #Remove data item from the linked list
    def remove(self, data) :
        if self.head is None :
            return;
        self.size = self.size - 1;
        currentnode = self.head;
        prevnode = None;
        while currentnode.data != data :
            prevnode = currentnode;
            currentnode = currentnode.nextnode;
        if prevnode is None :
            self.head = currentnode.nextnode;
        else :
            prevnode.nextnode = currentnode.nextnode;
            currentnode.nextnode = None;

     #o(1) Check the size of the linked list
    def size1(self):
        return self.size ;
    #o(N)
    def size2(self) :
        actualNode = self.head;
        size = 0;
        while actualNode is not None :
            size += 1;
            actualNode = actualNode.nextnode;
        return size;
     #o(N) Insert data item at the end of the linked list
    def insertEnd(self,data) :
        self.size = self.size + 1;
        newNode = Node(data);
        actualNode = self.head;
        while actualNode.nextnode is not None :
            actualNode = actualNode.nextnode;

        actualNode.nextnode = newNode;
      #o(N) Traverse the linked list
    def traverse(self) :
        actualNode = self.head;
        while actualNode is not None :
            print("%d" % actualNode.data);
            actualNode = actualNode.nextnode;
