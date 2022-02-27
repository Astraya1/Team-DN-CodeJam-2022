class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = [] 

    def addEdge(self, src, dest, weight, time):
        self.graph.append([src, dest, weight,time])

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for src, dest, weight, time in self.graph:
                if (dist[src] != float("Inf")) and ((dist[src] + weight) < dist[dest]):
                        dist[dest] = dist[src] + weight
        for src, dest, weight, time in self.graph:
                if (dist[src] != float("Inf")) and ((dist[src] + weight) < dist[dest]):
                        print("Graph contains negative weight cycle")
                        return
                         
        # print all distance
        self.printArr(dist)
        




def main():

    print("Trying bellman ford")

    truckG = Graph(5)
    truckG.addEdge(0, 1, -1, 40)
    truckG.addEdge(0, 2, 4, 50)
    truckG.addEdge(1, 2, 3,30)
    truckG.addEdge(1, 3, 2,50)
    truckG.addEdge(1, 4, 2,50)
    truckG.addEdge(3, 2, 5,20)
    truckG.addEdge(3, 1, 1,50)
    truckG.addEdge(4, 3, -3,60)
 
# Print the solution
    truckG.BellmanFord(0)


main()