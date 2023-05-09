
from typing import List


class Array:
    def __init__(self):
        self.items:List[int] = []
        self.count = 0
    
    def insert(self, item:int):
        self.items.append(item)
        self.count += 1
    
    def removeAt(self, index:int):
        if( index < 0 or index >= self.count):
            raise IndexError("Index out of range while removing")
        self.items.pop(index)
        self.count -= 1

        
    
    def indexOf(self, item:int)->int:
        try:
            return self.items.index(item)
        except(ValueError):
            return -1
    
    def size(self)->int:
        return self.count
    
    def print(self):
        print("printing items...")
        for item in self.items:
            print(item)
        


if __name__ == '__main__':
    array = Array()
    array.insert(10)
    array.insert(20)
    array.insert(30)
    array.insert(40)
    array.print()
    print("array size:",array.size())
    print("index of 110 is",array.indexOf(110))
    array.removeAt(4)
    array.print()
