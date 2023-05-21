class Node:
    def __init__(self,val:int,next:"Node"=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val},{self.next}"

class MyLinkedList:

    def __init__(self):
        self.head:Node =None
        self.tail:Node = None
        self.count=0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        curr = self.head
        i =0
        while i < index:
            curr = curr.next
            i+=1
        return curr.val

        

    def addAtHead(self, val: int) -> None:
        self.head = Node(val,self.head)
        if not self.tail:
            self.tail = self.head
        self.count +=1
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.count == 0:
            self.head = node
        else:
            self.tail.next = node 

        self.tail= node
        self.count +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return 
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.count:
            self.addAtTail(val)
            return
     
        curr = self.head
        i =1
        while i< index:
            curr = curr.next
            i+=1
        curr.next = Node(val,curr.next)
        self.count +=1
        
    def deleteAtHead(self)->None:
        if self.head == self.tail:
            self.head,self.tail = None,None
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp 
        self.count -=1

    def deleteAtIndex(self, index: int) -> None:
        if  index >= self.count:
            return
        if index == 0:
            self.deleteAtHead()
            return
        curr = self.head
        i =1
        while i<index and curr:
            curr = curr.next
            i+=1
        curr.next =curr.next.next
        print("curr",curr)
        if index == self.count-1:
            self.tail = curr
        self.count -=1
def main():
        
    list =MyLinkedList()
    list.addAtHead(0)
    list.addAtIndex(1,4)
    list.addAtTail(8)
    list.addAtHead(5)
    list.addAtIndex(4,3)
    list.addAtTail(0)
    list.addAtTail(5)
    list.addAtIndex(6,3)
    list.deleteAtIndex(7)
    list.deleteAtIndex(5)
    list.addAtTail(4)

main()