matrix = []
n = int(input("Enter the number of nodes:\n"))
for i in range(n):
    matrix.append([0]*n)
adList = {}

for i in range(n):
    print(f"Enter the nodes connected to {i+1}")
    j = int(input())-1
    adList[i+1] = []
    while j>=0:
        print("Enter the weight")
        weight = int(input())
        matrix[i][j] = weight
        adList[i+1].append([j+1,weight])
        print(f"Enter the nodes connected to {i+1}")
        j = int(input())-1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = '\t')
    print()

print(adList)