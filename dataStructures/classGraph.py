class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {
        }

    def addVertex(self, node):
        keys = self.adjacentList.keys()
        
        if node in keys:
            return False
        else:
            self.adjacentList[node] = []
            self.numberOfNodes += 1
            return True


    def addEdge(self, node1, node2):
        if node2 not in self.adjacentList[node1] and node1 not in self.adjacentList[node2]:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)


    def showConnections(self):
        keys = self.adjacentList.keys()
        for key in keys:
            string = '{} -> {}'.format(key, self.adjacentList[key])
            print(string)


graph = Graph()

graph.addVertex(0)
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 4)
graph.addEdge(3, 4)
graph.addEdge(4, 5)
graph.addEdge(5, 6)

graph.showConnections()