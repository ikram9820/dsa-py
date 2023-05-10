from Stack import Stack

class Queue:
    def __init__(self):
        self.items = []
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.items.insert(0,item)
        self.stack1.push(item)
    
    def dequeue(self):
        # return self.items.pop()
        self.stack1ToStack2()
        return self.stack2.pop()
    
    def stack1ToStack2(self):
        if(self.stack2.isEmpty()):
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())


    def front(self):
        # return self.items[-1]
        self.stack1ToStack2()
        return self.stack2.peek()
    
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
    print(q.front())    
    # q.reverse()
