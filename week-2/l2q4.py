# adjacency list and adjacency matrix for Undirected graph

class graph:
    def __init__(self,n):
        adjList= dict()

        for i in range(n):
            adjList[f"{chr(65+i)}"]=[]

        adjMat =[]
        for i in range(n):
            l = [0 for i in range (n)]
            adjMat.append(l)

        self.adjList= adjList
        self.adjMat = adjMat

    def addEdge(self,u,v):
        self.adjList[f'{u}'].append(v)
        self.adjList[f'{v}'].append(u)
        self.adjMat[ord(u)-65][ord(v)-65] = 1
        self.adjMat[ord(v)-65][ord(u)-65] = 1

    def display(self):
        print('Adjency List')
        print(self.adjList)
        print('Adjency Matrix')
        print(self.adjMat)

# main functions here 

num = int(input('Num of nodes'))
edges = int(input('Num of edges'))

g = graph(num)

print('Enter values')

for i in range(edges):
    u = input()
    v = input()
    g.addEdge(u,v)

# displaying
g.display()