# Bank problem

class Customer:
    def __init__(self,name,transaction):
        self.name = name
        self.transaction = transaction

class Bank:
    def __init__(self):
        self.queue=[]

    def add_cust(self,cust):
        self.queue.append(cust)

    def serve_cust(self):
        if len(self.queue)==0 :
            print('No one in Queue')
        else :
            cust= self.queue.pop(0)
            print(f'Serving {cust.name}')

# main functions here 

b = Bank()

print('1.Add  2.Serve  -1.Exit')

while True:
    ch = int(input('Enter choice '))

    if(ch==1):
        name = input('Enter name ')
        tr = int(input('Transaction: '))

        curr_cust= Customer(name,tr)

        b.add_cust(curr_cust)

    
    elif ch==2 :
        b.serve_cust()

    elif ch==-1:
        break

    else :
        print('Invalid Choice')


