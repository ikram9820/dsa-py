
class CircularQueue:
    def __init__(self, capacity:int):
        self.items = [0]*capacity
        self.capacity =capacity
        self.count= 0
        self.front=-1
        self.rear =-1
    
    def enqueue(self,item):
        if self.isFull():
            raise ValueError("Queue is full")
        if self.isEmpty():
            self.rear +=1
        if not self.isFull() and self.front == self.count:
            self.front =0
        else:
            self.front+=1

        self.items[self.front]=item
        self.count+=1
        

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Empty queue")
        self.items[self.rear] = None
        if not self.isFull() and self.rear == self.count-1 :
            self.rear =0
        elif self.count ==1:
            self.rear = self.front = -1
        else:
            self.rear+=1
        
        self.count-=1
    
    def traverse(self):
        if self.isEmpty():
            return
        i = self.rear
        for _ in range(self.count):
            print(self.items[i],end=", ")
            i+=1
            if (i == self.count and  self.isFull):
                i=0
            

    def isFull(self):
        return self.count >= self.capacity
    
    def isEmpty(self):
        return self.count == 0


if __name__ == '__main__':
    q = CircularQueue(4)
    q.enqueue(34)
    q.enqueue(56)
    q.enqueue(23)
    q.enqueue(23)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(6)
 
    q.enqueue(3)
 
    q.enqueue(5)
    q.dequeue()
    q.enqueue(10)
 
    q.traverse()