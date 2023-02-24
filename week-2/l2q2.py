# directed unweighted graph 

class graph:
    def __init__ (self,n):
        adjList = dict()

        for i in range(n):
            adjList[f'{i}']= []

        self.adjList= adjList
        self.n = n

    def addEdge(self,u,v):
        self.adjList[f'{u}'].append(v)

    def display(self):
        print('Printing the adjency List')

        for i in range (self.n):
            l= self.adjList[f'{i}']

            if l:
                for j in range (len(l)):
                    print(f'({i} -> {l[j]}) ', end='')
                print()

# Main functions here
num = int(input('Enter number of nodes '))
edges = int(input('Enter number of edges '))

g = graph(num)

for i in range (edges):
    u = int(input())
    v = int(input())
    g.addEdge(u,v)

    # displaying graph

g.display()