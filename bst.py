class BinarySearchTree(object) :
    def __init__(self) :
        self.root = None
    #Insert a node in BST
    def insert(self, data) :
        if not self.root :
            self.root = Node(data)
        else :
            self.insertnode(data, self.root)
    # o(logN) #Insert a node with data to BST
    def insertnode(self, data, node):
        if data < node.data :
            if node.leftchild :
                insertnode(data, node.leftchild)
            else :
                node.leftchild = Node(data)
        else :
                if node.rightchild :
                    insertnode(data, node.rightchild)
                else :
                    node.rightchild = Node(data)
    #Get minimum value from the bst
    def getMinValue(self) :
          if self.root :
                return self.getMin(self.root)

    def getMin(self, node) :
        if node.leftchild :
             return self.getMin(node.leftchild)
        return node.data
    #Get maximum value from the bst
    def getMaxValue(self) :
          if self.root :
                return self.getMax(self.root)

    def getMax(self, node) :
        if node.rightchild :
            return getMax(node.rightchild)

        return node.data
    #Inorder traversal in the BST
    def traverse(self) :
        if self.root :
            self.traverseInOrder(self.root)
    def traverseInOrder(self, node) :
        if node.leftchild :
            self.traverseInOrder(node.leftchild)
        print("%s" %node.data)

        if node.rightchild :
                self.traverseInOrder(node.rightchild)
