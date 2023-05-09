
from typing import List


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next:Node = next

class LinkedList:
    def __init__(self) -> None:
        self.first:Node=None
        self.last:Node=None
        self.count = 0

    def add_first(self,data):
        self.first = Node(data,self.first)
        if self.is_empty(): 
            self.last = self.first
        self.count += 1
    
    def add_last(self,data):
        node = Node(data)
        if self.is_empty():
            self.first = self.last = node
        else: 
            self.last.next = node 
            self.last = node
        self.count += 1
   
    def delete_first(self):
        if self.is_empty():
            raise ValueError("there is no first")
        if (self.has_only_one()):
            self.first, self.last = None, None
        else:
            next = self.first.next
            self.first.next = None
            self.first = next
        self.count -= 1
    
    def delete_last(self):
        if self.is_empty():
            raise ValueError("there is no first")
        if (self.has_only_one()):
            self.first, self.last = None, None
        else:
            previous = self.getPreviousNode(self.last)
            self.last = previous
            self.last.next = None
        self.count -= 1

    def getPreviousNode(self,node:Node):
        if(self.is_empty() or self.has_only_one()):
            return None
        current = self.first
        while current.next != self.last:
            current = current.next
        return current
    
    def index_of(self,item)->int:
        index =0
        current = self.first
        while current:
            if current.data == item:
                return index
            index += 1
            current = current.next
        return -1   
    
    def contains(self,item)->bool:
        return self.index_of(item) != -1
    
    def size(self)->int:
        return self.count

    def to_array(self)->List:
        list = []
        current = self.first
        while current:
            list.append(current.data) 
            current = current.next
        return list

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
    print("list size: " ,list.size())
    print(list.index_of(4))
    list.traverse()
    array = list.to_array()
    print("array: " ,array)