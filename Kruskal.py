#Kruskal Algorithm to find the minimum spanning tree o(logV)
#Creating a vertex
class vertex(object) :
    def __init__(self,name) :
        self.name = name
        self.node = node
#Creating a node
class Node(object) :
    def __init__(self,height, nodeId, parentnode) :
        self.height = height
        self.nodeId = nodeId
        self.parentnode = parentnode
#Creating an Edge
class Edge(object)  :
    def __init__(self, weight, startvertex, targetvertex) :
        self.weight = weight
        self.startvertex = targetvertex
    def __cmp__(self, otheredge) :
        return self.cmp(self.weight, otheredge.weight)
    def __lt__(self,other) :
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority
#Creating a union data structure or disjoint set
class Disjointset(object) :
    def __init__(self, vertexlist) :
        self.vertexlist = vertexlist
        self.rootnodes = []
        self.nodecount = 0
        self.setcount = 0
        self.makesets(vertexlist)
#Find the set id or the set to which the node belongs to
    def find(self, node) :
        currentnode = node
        while currentnode.parentnode is not None :
            currentnode = currentnode.parentnode
        root = currentnode
        currentnode = node
        while currentnode is not root :
            temp = currentnode.parentnode
            currentnode.parentnode = root
            currentnode = temp
        return root.nodeId
#Merging two nodes or disjoint sets together
    def merge(self, node1, node2) : # merging the two vertices
        index1 = self.find(node1)
        index2 = self.find(node2)
        if index1 == index2 :
            return # The two are in the same so no merging
        root1 = self.rootnodes[index1]
        root2 = self.rootnodes[index2]
        if root1.height < root2.height :
            root1.parentnode = root2
        elif root1.height > root2.height :
            root2.parentnode = root1
        else :
            root2.parentnode = root1
            root1.height = root1.height + 1
#Making disjoint sets from the vertex list
    def makesets(self, vertexlist) :
        for v in vertexlist :
            self.makeset(v)
    def makeset(self, vertex) :
        node = Node(0, len(self.rootnodes), None)
        vertex.node = node
        self.rootnodes.append(node)
        self.setcount = self.setcount + 1
        self.nodecount =  self.nodecount + 1
#Kruskal Algorithm using the union data structure
class KruskalAlgorithm(object) :
      def spanningtree(self, vertexlist, edgelist) :
            disjoinset = Disjointset(vertexlist)
            spanningtree = []
            edgelist.sort()
            for edge in edgelist :
                u = edge.startvertex
                v = edge.targetvertex
                if disjoinset.find(u.node) is not disjoinset.find(v.node) :
                    spanningtree.append(edge)
                    disjoinset.merge(u.node, v.node)
            for edge in spanningtree :
                print(edge.startvertex.name, "-",edge.targetvertex.name)
