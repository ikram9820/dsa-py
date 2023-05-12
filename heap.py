class Heap:
    def __init__(self):
        self.heap = []

    def insert(self,value):
        self.heap.append(value)
        self.bubbleup()

    def remove(self):
        item = self.heap.pop(0)
        self.heap.insert(0,self.heap.pop())
        self.bubbledown()
        return item
    
    def bubbleup(self):
        index=self.size()-1
        while index>0 and self.heap[index] >\
                          self.heap[self.parentIndex(index)]:
            self.swap(index,self.parentIndex(index))
            index = self.parentIndex(index)
  
    def bubbledown(self):
        index =0
        while index<self.size() and not self.validParent(index):
            largerChildIndex = self.largerChildIndex(index)
            self.swap(index,largerChildIndex)
            index =largerChildIndex

    def validParent(self, index):
        if not self.hasLeft(index):
            return True
        
        isValid = self.heap[index]>=self.left(index)
        if self.hasRight(index): 
            isValid &= self.heap[index]>=self.right(index)
        return isValid
        
    def largerChildIndex(self, index):
        if not self.hasLeft(index):
            return index
        if not self.hasRight(index):
            return self.leftIndex(index)
        
        if self.left(index) >= self.right(index):
            return self.leftIndex(index)
        else:
            return self.rightIndex(index)
        
    def hasLeft(self,index):
        return self.leftIndex(index) < self.size()
    def hasRight(self,index):
        return self.rightIndex(index) < self.size()
    def left(self, index):
        return self.heap[self.leftIndex(index)]
    def right(self, index):
        return self.heap[self.rightIndex(index)]
    def parent(self,index):
        return self.heap[self.parentIndex(index)]
    def rightIndex(self, index):
        return index*2+2
    def leftIndex(self, index):
        return index*2+1
    def parentIndex(self, index:int)->int:
        return (index-1)//2
    def swap(self,index1:int,index2:int):
        self.heap[index1] , self.heap[index2]=\
        self.heap[index2],self.heap[index1]
    def traverse(self,index=0):
        if index>=self.size():return 
        self.traverse(index*2 +1)
        self.traverse(index*2 +2)
        print(self.heap[index],end=", ")
    def size(self)->int:
        return len(self.heap)
    def empty(self)->bool:
        return self.size()==0
    
if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(20)
    heap.insert(15)
    heap.insert(13)
    heap.insert(19)
    heap.insert(11)
    heap.insert(121)
    heap.insert(11)
    heap.insert(11)

   
    print(heap.remove())
    print(heap.remove())
    heap.traverse()

