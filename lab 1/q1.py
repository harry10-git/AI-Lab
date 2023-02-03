# Implement queue using 2 stacks

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enqueue(self,item):
        self.s1.append(item)

    def dequeue(self):
        x=-1
        if(len(self.s1) == 0):
            print("Queue is Empty")
            return x
        else:
            while(len(self.s1)!=0):
                self.s2.append(self.s1.pop())

            x = self.s2.pop() # x stores the result

            while(len(self.s2)!=0):
                self.s1.append(self.s2.pop())
        return x

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())













# class stack: 
#     def init(self):
#         self.items=[]

#     def push(self):
#         item = input('Enter ele to push')
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop if self.items else None

#     def peek(self):
#         return self.items[-1] if self.items else None

#     def isEmpty(self):
#         return not self.items
    
# class queue:
#     def initQ(self):
#         s1 = stack()
#         s1.init()
#         s2 = stack()
#         s2.init()

#     def enqueue(self,item):
#         if(self.s1.isEmpty() and self.s2.isEmpty()):
#             self.s1.push(item)


# q = queue()
# q.initQ()
# q.enqueue(5)