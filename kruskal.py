import networkx as nx

class Grafo:
    def __init__(self, numero_vertice):
        self.numero_vertice = numero_vertice
        self.grafo = []

    def add_aresta(sef, orig, dest, peso):
        sef.grafo.append([orig, dest, peso])

    def buscar(self, arv, i):
        if arv[i] == i:
            return i

        return self.buscar(arv, arv[i])
    
    def uniao(self, arv, pai, orig, dest):
        xorig = self.buscar(arv, orig)
        ydest = self.buscar(arv, dest)
        if pai[xorig] < pai[ydest]:
            arv[xorig] = ydest
        elif pai[xorig] > pai[ydest]:
            arv[ydest] = xorig
        else:
            arv[ydest] = xorig
            pai[xorig] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        arv = []
        pai = []
        for node in range(self.numero_vertice):
            arv.append(node)
            pai.append(0)
        while e < self.numero_vertice - 1:
            orig, dest, peso = self.grafo[i]
            i = i + 1
            x = self.buscar(arv, orig)
            y = self.buscar(arv, dest)
            if x != y:
                e = e + 1
                result.append([orig, dest, peso])
                self.uniao(arv, pai, x, y)
        print(result)
        for u, v, weight in result:
            print("Aresta:",u, v,end =" ")
            print("-",weight)

grafo = Grafo(5)
grafo.add_aresta(0, 1, 8)
grafo.add_aresta(0, 2, 5)
grafo.add_aresta(1, 2, 9)
grafo.add_aresta(1, 3, 11)
grafo.add_aresta(2, 3, 15)
grafo.add_aresta(2, 4, 10)
grafo.add_aresta(3, 4, 7)
grafo.kruskal()
