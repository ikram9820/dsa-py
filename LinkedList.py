
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next:Node = next

class LinkedList:
    def __init__(self) -> None:
        self.first:Node=None
        self.last:Node=None

    def add_first(self,data):
        self.first = Node(data,self.first)
        if self.is_empty(): 
            self.last = self.first
    
    def add_last(self,data):
        node = Node(data)
        if self.is_empty():
            self.first = self.last = node
            return 
        self.last.next = node 
        self.last = node

    
    def delete_first(self):
        if self.is_empty():
            raise ValueError("there is no first")
        if (self.has_only_one()):
            self.first, self.last = None, None
            return
        self.first = self.first.next
    
    def delete_last(self):
        if self.is_empty():
            raise ValueError("there is no first")
        if (self.has_only_one()):
            self.first, self.last = None, None
            return
        current = self.first
        while current.next != self.last:
            current = current.next
        self.last = current
        self.last.next = None

    def contains(self,item)->bool:
        if(self.is_empty()):
            return False
        current = self.first
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def index_of(self,item)->int:
        if self.is_empty():
            return -1
        current = self.first
        index =0
        while current:
            if current.data == item:
                return index
            index += 1
            current = current.next
        return -1
    
        
    def has_only_one(self)->bool:
        return bool(self.first == self.last)

    def is_empty(self)->bool:
        return bool((self.first is None)or(self.last is None))
    
    def traverse(self):
        current = self.first
        print("printting linked list...")
        while current:
            print(current.data,end=", ")
            current = current.next
        print()


if __name__ == "__main__":
    list = LinkedList()
    list.add_last(5)
    list.add_last(4)
    list.add_last(9)
    list.add_last(6)
    list.traverse()

    print(list.index_of(4))
    list.traverse()