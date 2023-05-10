from Stack import Stack

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items==[]
    
    def reverse(self):
        stack = Stack()
        while not self.isEmpty():
            stack.push(self.dequeue())
        
        while not stack.isEmpty():
            self.enqueue(stack.pop())

    def __str__(self):
        print("printting Queue...")
        strItems=''
        for item in self.items:
            strItems+= str(item)+", "
        return strItems
    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(9)
    # q.dequeue()
    print(q)    
    q.reverse()
    print(q)