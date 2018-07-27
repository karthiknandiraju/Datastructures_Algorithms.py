class Node(object) :
    #Initialize the node
    def __init__(self,name) :
        self.name = name  #Name of the node
        self.adjacencylist = [] # A list for the node's neighbours
        self.visited = False # initially set the visit as False
        self.predecessor = None
#Visit every vertex exactly once o(V+E)
class BreadthFirstSearch(object) : #Nodes at the low level of the graph are visisted first
      def bfs(self, startnode) :
            queue = []  # create an empty queue
            queue.append(startnode) #Append the start node
            startnode.visited = True # set the node to visited
            while queue :  #check if queue is not empty
                actualnode = queue.pop(0) #pop the first in node
                print("%s" %actualnode.name) #print the node name
                for n in actualnode.adjacencylist : # for the neighbours of the popped out node
                     if not n.visited :
                            n.visited = True  # if the node is not visited set it as visited
                            queue.append(n) #append the node to the queue
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
bfs = BreadthFirstSearch()
bfs.bfs(node1)
