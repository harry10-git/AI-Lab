# directed unweighted graph with weight

class graph:
    def __init__ (self,n):
        adjList = dict()

        for i in range(n):
            adjList[f'{i}']= []

        self.adjList= adjList
        self.n = n

    def addEdge(self,u,v,wt):
        self.adjList[f'{u}'].append([v,wt])

    def display(self):
        print('Printing the adjency List')

        for i in range (self.n):
            l= self.adjList[f'{i}']

            if l:
                for j in range (len(l)):
                    print(f'({i} -> {l[j][0]},{l[j][1]}) ', end='')
                print()

# Main functions here
num = int(input('Enter number of nodes '))
edges = int(input('Enter number of edges '))

g = graph(num)

for i in range (edges):
    u = int(input())
    v = int(input())
    w = int(input())
    
    g.addEdge(u,v,w)

    # displaying graph

g.display()