import networkx as nx
import matplotlib.pyplot as plt


#Initializing the Graph Class
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self, result):

        G = nx.Graph() 
        E = []
        for s, d, w in result:
            E.append((s, d, w))
            # print("%s - %s: %s" % (s, d, w))

        G.add_weighted_edges_from(E)
        pos=nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
        plt.show()
    
    def kruskalAlgo(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(self.MST)

#Implementing Disjoint Set data structure and its functions
class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


g = Graph(8)

for i in range(1, 9):
    g.addNode(i)
   
g.addEdge(1, 2, 240)
g.addEdge(1, 3, 210)
g.addEdge(1, 4, 340)
g.addEdge(1, 5, 280)
g.addEdge(1, 6, 200)
g.addEdge(1, 7, 345)
g.addEdge(1, 8, 120)

g.addEdge(2, 3, 265)
g.addEdge(2, 4, 175)
g.addEdge(2, 5, 215)
g.addEdge(2, 6, 180)
g.addEdge(2, 7, 185)
g.addEdge(2, 8, 155)

g.addEdge(3, 4, 260)
g.addEdge(3, 5, 115)
g.addEdge(3, 6, 350)
g.addEdge(3, 7, 435)
g.addEdge(3, 8, 195)

g.addEdge(4, 5, 160)
g.addEdge(4, 6, 330)
g.addEdge(4, 7, 295)
g.addEdge(4, 8, 230)

g.addEdge(5, 6, 360)
g.addEdge(5, 7, 400)
g.addEdge(5, 8, 170)

g.addEdge(6, 7, 175)
g.addEdge(6, 8, 205)

g.addEdge(7, 8, 305)

g.printSolution(g.graph)
# g.kruskalAlgo()