from stack import Stack

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)
    
    def dequeue(self):
        self.stack1ToStack2()
        return self.stack2.pop()
    
    def stack1ToStack2(self):
        if(self.stack2.isEmpty()):
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())

    def front(self):
        self.stack1ToStack2()
        return self.stack2.peek()
    
    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()
    

    
if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(9)
    # q.dequeue()
    print(q.front())    
  
