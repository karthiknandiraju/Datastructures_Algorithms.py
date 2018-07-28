import sys
import heapq

#Creating an Edge
class Edge(object) :
    def __init__(self, weight, startvertex, targetvertex) :
        self.weight = weight #Weight of the edge
        self.startvertex = startvertex  #start vertex connecting the edge
        self.targetvertex = targetvertex #end vertex connecting the edge
#Creating the Node
class Node(object) :
    def __init__(self, name) :
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencylist = []
        self.minDistance = sys.maxsize # Initialize all node distance to infinity or positive max number
    def __cmp__(self, othervertex) :  #for the heapq
        return self.__cmp__(self.minDistance, othervertex.minDistance)
    def __lt__(self,other) :  #for the heapq
        selfpriority = self.minDistance
        otherpriority = other.minDistance
        return selfpriority < otherpriority
 #Dijkstra's Algorithm which gives shortest path from the source node in a graph(positive wieghts only)
class Dijkstra(object) :
    def calcshortestpath(self, vertexlist, startvertex) :
        q = []
        startvertex.minDistance = 0 # set the intital distance of the start node to 0
        heapq.heappush(q,startvertex)
        while len(q) > 0 :
            actualvertex = heapq.heappop(q)
            for edge in actualvertex.adjacencylist : # getting the edges of the popped out vertex
                u = edge.startvertex  # u -> v, u
                v = edge.targetvertex #u -> v, v
                newdistance = u.minDistance + edge.weight # calculating the new distance from u -> v
            if newdistance < v.minDistance : # if the newidstance is less than the min distance of the v
                v.predecessor = u
                v.minDistance = newdistance
                heapq.heappush(q,v)
    def getshortestpathto(self, targetvertex) :
        print("shortest path to vertex is : " , targetvertex.minDistance)
        node = targetvertex
        while node is not None :
            print("%s"%node.name) # Priniting the name of the node
            node = node.predecessor  # getting the predecessor node

# Creating a Graph
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")
edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(7, node8, node3)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

node1.adjacencylist.append(edge1)
node1.adjacencylist.append(edge2)
node1.adjacencylist.append(edge3)
node2.adjacencylist.append(edge4)
node2.adjacencylist.append(edge5)
node2.adjacencylist.append(edge6)
node8.adjacencylist.append(edge7)
node8.adjacencylist.append(edge8)
node5.adjacencylist.append(edge9)
node5.adjacencylist.append(edge10)
node6.adjacencylist.append(edge11)
node6.adjacencylist.append(edge12)
node3.adjacencylist.append(edge13)
node3.adjacencylist.append(edge14)
node4.adjacencylist.append(edge15)

vertexlist = (node1,node2,node3,node4,node5,node6,node7,node8)

dijkstra = Dijkstra()
dijkstra.calcshortestpath(vertexlist,node1)
dijkstra.getshortestpathto(node7)
