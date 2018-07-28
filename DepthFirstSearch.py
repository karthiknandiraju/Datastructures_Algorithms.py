#Depth First Search visits the nodes in depth

#Creating a node
class Node(object) :
     def __init__(self, name) :
            self.name = name
            self.adjacencylist = [] # A list of the nodes neighbours
            self.visited = False
            self.predecessor = None
#Depth First Search Algorithm
class DepthFirstSearch(object) :
    def dfs(self,node) :
            node.visited = True  #set the node as visited
            print("%s" %node.name) #printing the node name
            for n in node.adjacencylist :  #get the neighbours of the node
                if not n.visited :  #If the node is not already visited then visit it
                     self.dfs(n) #Recursive call to the dfs function
# Creating a graph
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node1.adjacencylist.append(node2)
node1.adjacencylist.append(node3)
node2.adjacencylist.append(node4)
node4.adjacencylist.append(node5)
dfs = DepthFirstSearch()
dfs.dfs(node1)


                  
