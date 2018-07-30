import sys

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

#Bellman Ford Algorithm shortest path from source in a graph(-ve edge weights allowed)
#o(E.V)
class Bellman(object) :
    has_cycle = False
    def calcshortestpath(self, vertexlist, edgelist, startvertex) :
        startvertex.minDistance = 0
        # vertices number of iterations
        for i in range(0,len(vertexlist)-1) :
          for edge in edgelist :
                u = edge.startvertex
                v = edge.targetvertex
                newdistance = u.minDistance + edge.weight #calculating the new distance
                if newdistance < v.minDistance :
                    v.minDistance = newdistance  #updating the minimum distance
                    v.predecessor = u
        for edge in edgelist :
            if self.hascycle(edge) :
                print("Negative cycle detected")
                Bellman.has_cycle = True
                return
#Check if a graph has cycle or not
    def hascycle(self,edge) :
        if (edge.startvertex.minDistance+ edge.weight) < edge.targetvertex.minDistance :
            return True
        else :
            return False
#Get the shortest path to a particular node from source
    def getshortestpathto(self, targetvertex) :
        if not Bellman.has_cycle :
            print("Shortest path exists with value", targetvertex.minDistance)
            node = targetvertex
            while node is not None :
                print("%s"%node.name)
                node = node.predecessor
        else :
            print("Negative cycle detected")

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
edge17 = Edge(1, node1, node2)
edge18 = Edge(1, node2, node3)
edge19 = Edge(-3, node3, node1)


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
edgelist = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,
          edge14,edge15)
#edgelist = (edge17, edge18, edge19)

bellman = Bellman()
bellman.calcshortestpath(vertexlist,edgelist,node1)
bellman.getshortestpathto(node7)

    
