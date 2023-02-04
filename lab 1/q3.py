#Create two list X and Y with some set of numerical values. 
#Compute Euclidean distance for corresponding values in X and Y. 
#Store the distance values in a separate list and sort them using Bubble sort algorithm.

import math 

x=[]
y=[]
n = int(input('Enter num of values'))

for i in range (n):
    tempX = int(input('Enter X value'))
    tempY = int(input('Enter Y value'))
    x.append(tempX)
    y.append(tempY)
                
print(x)
print(y)



res=[]
for i in range(n):
	temp= math.sqrt(x[i]**2 + y[i]**2)
	res.append(temp)
print(res)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


sorted_list = bubble_sort(res)
print(sorted_list)


# import math

# class node:
# 	def __init__(self,data):
# 		self.data= data
# 		self.next = None

# class linkedList:
# 	def __init__(self):
# 		self.head = None
# 		self.last= None

# 	def add(self,data):
# 		if self.last is None:
# 			self.head = node(data)
# 			self.last= self.head
# 		else:
# 			self.last.next= node(data)
# 			self.last = self.last.next

# 	def display(self):
# 		ptr = self.head
# 		while ptr is not None:
# 			print(ptr.data, end="->")
# 			ptr= ptr.next
# 		print("\n")



# linkedList1 = linkedList()
# n = int(input('Enter number of nodes '))
# for i in range (n):
# 	data= int(input('Enter val to insert '))
# 	linkedList1.add(data)

# print("displaying elements of L1")
# linkedList1.display()


# linkedList2 = linkedList()
# for i in range (n):
# 	temp= int(input('Enter val to insert '))
# 	linkedList2.add(temp)

# print("displaying elements of L2")
# linkedList2.display()



# # creating distance lists
# distanceList = linkedList()
# for i in range (n):
#     temp = math.sqrt((linkedList1.head.data **2) + (linkedList2.head.data **2))
#     distanceList.add(temp)
#     linkedList1.head= linkedList1.head.next
#     linkedList2.head= linkedList2.head.next
    
    
# distanceList.display()
    
 
## sorting using bubble sort



