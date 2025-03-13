class implementQueue:
    
    def __init__(self):
        self.stackpop=[]
        self.stackpush=[]

    def enqueue(self,x):
        self.stackpush.append(x)

    
    def dequeue(self):
        if not self.stackpop:
            while self.stackpush:
                item=self.stackpush.pop()
                self.stackpop.append(item)
        
        if self.stackpop:
            return self.stackpop.pop()
        else:
            return -1
    
    def front(self):
        if not self.stackpop:
            while self.stackpush:
                item=self.stackpush.pop()
                self.stackpop.append(item)
        
        if self.stackpop:
            return self.stackpop[-1]
        else:
            return -1



n = int(input())  # Number of operations
queue = implementQueue()

for _ in range(n):
    operation = input().split(" ")
    if operation[0] == '1':
        # Enqueue operation
        queue.enqueue(int(operation[1]))
    elif operation[0] == '2':
        # Dequeue operation
        print(queue.dequeue())
    elif operation[0] == '3':
        # Front operation
        print(queue.front())