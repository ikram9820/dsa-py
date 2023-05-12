class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,data):
        if self.isEmpty():
            self.items.insert(0,data)
        else:
            for index, item in enumerate(self.items):
                if data<item:
                    self.items.insert(index,data)
                    return
            self.items.append(data)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        print("printting Queue...")
        strItems=''
        for item in self.items:
            strItems+= str(item)+", "
        return strItems
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(0)
    q.enqueue(5)
    q.enqueue(9)
    q.enqueue(2)
    q.enqueue(1)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)
 