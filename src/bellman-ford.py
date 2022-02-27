class load:
    def __init__(self, money):
        self.money = money

    def money(self, m):
        self.money = m

    def money(self):
        return self.money

class node:
    def __init__(self, pickuphour, load):
        self.pickuphour = pickuphour
        self.load = load

    def load(self, l):
        self.load = l

    def load(self):
        return self.load

    def pickuphour(self):
        return self.pickuphour


class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = [] 

    def addEdge(self, src, dest, weight, time):
        self.graph.append([src, dest, weight, time])
    # def editEdge(self, g):

    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src, maxtime, list_node):
        dist = [float("-Inf")] * self.V
        dist[src] = 0

        tim = [float("Inf")]*self.V
        tim[src] = 0


        for _ in range(self.V - 1):
            for src, dest, weight, time in self.graph:
                src_node = list_node[src] 
                dest_node = list_node[dest]
                if (dist[src] != float("-Inf")) and ((dist[src] + weight) > dist[dest]) and (tim[src] + time < maxtime) and (tim[src] + time < dest_node.pickuphour):
                        dist[dest] = dist[src] + weight
                        tim[dest] = tim[src] + time
                        dest_node.load = dest_node-1
                        

        # for src, dest, weight, time in self.graph:
        #         if (dist[src] != float("-Inf")) and ((dist[src] + weight) > dist[dest]):
        #                 print("Graph contains crazy weight cycle")
        #                 return
                         
        # print all distance
        self.printArr(dist)
        




def main():

    print("Trying bellman ford")

    src = node(float("Inf"), 0)
    a = node(float("Inf"), 1)
    b = node(float("Inf"), 0)
    c = node(float("Inf"), 1)
    d = node(float("Inf"), 0)
    node_list = [src, a, b, c, d]

    truckG = Graph(5)
    #start - a
    truckG.addEdge(0, 1, -150, 40)
    #a - start
    truckG.addEdge(1, 0, -150, 40)

    #start - c
    truckG.addEdge(0, 3, -460, 80)
    #c - start
    truckG.addEdge(3, 0, -460, 80)

    #a - d
    truckG.addEdge(1, 4, -400,30)
    #d - a
    truckG.addEdge(4, 1, -400,30)

    #a - b
    truckG.addEdge(1, 2, 700,50)
    #b - a
    truckG.addEdge(2, 1, -300,50)

    #b - c
    truckG.addEdge(2, 3, -275,50)
    #c - b
    truckG.addEdge(3, 2,-275, 50)

    #c - d
    truckG.addEdge(3, 4, 300,20)

    
    # g = Graph(5)
    # g.addEdge(0, 1, -1,1)
    # g.addEdge(0, 2, 4,1)
    # g.addEdge(1, 2, 3,1)
    # g.addEdge(1, 3, 2,1)
    # g.addEdge(1, 4, 2,1)
    # g.addEdge(3, 2, 5,1)
    # g.addEdge(3, 1, 1,1)
    # g.addEdge(4, 3, -3,1)
 
# Print the solution
    truckG.BellmanFord(0,10000,node_list)
    # g.BellmanFord(0)


main()