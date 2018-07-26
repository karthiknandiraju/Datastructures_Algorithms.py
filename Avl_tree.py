class AVL(object) :
    def __init__(self) :
        self.root = None
    #Calculate the Height of the Avl tree
    def calcHeight(self, node) :
        if not node :
            return -1
        return node.height
  #Insert a data item into the AVL tree
    def insert(self, data) :
        self.root = self.insertNode(data, self.root)

    def insertNode(self,data,node) :
        if not node :
            return Node(data)
        if data < node.data :
            node.leftchild = self.insertNode(data, node.leftchild)
        else :
            node.rightchild = self.insertNode(data, node.rightchild)
        node.height = max(self.calcHeight(node.leftchild),self.calcHeight(node.rightchild)) + 1
        return self.settleViolation(node, data)
  # Check the balance of the tree
    def settleViolation(self, node, data) :
        balance = self.calcBalance(node)
        # case 1 left left heavy situation
        if balance > 1 and data < node.leftchild.data :
            print("Left Left heavy situtation")
            return self.rotateRight(node)
        # case 2 right right heavy situation
        if balance < -1 and data > node.rightchild.data :
            print("right right heavy situtation")
            return self.rotateLeft(node)
        if balance > 1 and data > node.leftchild.data :
            node.leftchild = self.rotateLeft(node.leftchild)
            return self.rotateRight(node)
        if balance < - 1 and data < node.rightchild.data :
            node.rightchild = self.rotateRight(node.rightchild)
            return self.rotateLeft(node)
        return node
    # > 1 then left heavy tree (right rotation)
    # < -1 then right heavy tree (left rotation)
    def calcBalance(self, node) :
        if not node :
            return 0
        return (self.calcHeight(node.leftchild) - self.calcHeight(node.rightchild))
    def rotateRight(self,node) :
        print("Rotating to the right", node.data)
        templeftchild = node.leftchild
        t = templeftchild.rightchild
        templeftchild.rightchild = node
        node.leftchild = t
        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1
        templeftchild.height = max(self.calcHeight(templeftchild.leftchild), self.calcHeight(templeftchild.rightchild)) + 1
        return templeftchild

    def rotateLeft(node) :
        print("Rotating to the left", node.data)
        temprightchild = node.rightchild
        t = temprightchild.lefttchild
        temprightchild.leftchild = node
        node.rightchild = t
        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1
        templeftchild.height = max(self.calcHeight(templeftchild.leftchild), self.calcHeight(templeftchild.rightchild)) + 1
        return temprightchild
 # Traverse the tree
    def traverse(self) :
        if self.root :
            self.traverseInOrder(self.root)
    def traverseInOrder(self, node) :
        if node.leftchild :
            self.traverseInOrder(node.leftchild)
        print("%s" %node.data)

        if node.rightchild :
                self.traverseInOrder(node.rightchild)
   #Remove a node from the tree
    def removeNode(self, data, node) :
        if not node :
            return node
        if data < node.data :
            node.leftchild = self.removeNode(data, node.leftchild)
        elif data > node.data :
            node.rightchild = self.removeNode(data, node.rightchild)
        else :
            if not node.leftchild and not node.rightchild :
                print("Removing a leaf node")
                del node
                return None
            if not node.leftchild :
                print("Removing a node with a single right child")
                tempnode = node.rightchild
                del node
                return tempnode
            elif not node.rightchild :
                print("Removing a node with a single left child")
                tempnode = node.leftchild
                del node
                return tempnode
            print("Removing node with two children")
            tempnode = self.getPredecessor(node.leftchild)
            node.data = tempnode.data
            node.leftchild = self.removeNode(tempnode.data, node.leftchild)
        node.height = max(self.calcHeight(node.leftchild), self.calcHeight(node.rightchild)) + 1
        balance = self.calcBalance(node)
        # case 1 left left heavy situation
        if balance > 1 and data < node.leftchild.data :
            print("Left Left heavy situtation")
            return self.rotateRight(node)
        # case 2 right right heavy situation
        if balance < -1 and data > node.rightchild.data :
            print("right right heavy situtation")
            return self.rotateLeft(node)
        if balance > 1 and data > node.leftchild.data :
            node.leftchild = self.rotateLeft(node.leftchild)
            return self.rotateRight(node)
        if balance < - 1 and data < node.rightchild.data :
            node.rightchild = self.rotateRight(node.rightchild)
            return self.rotateLeft(node)
        return node
   #Get Predecessor
    def getPredecessor(self, node) :
        if node.rightchild :
            return self.getPredecessor(node.rightchild)
        return node
    # Remove a Node
    def remove(self, data) :
        if self.root :
            self.root = self.removeNode(data, self.root)
