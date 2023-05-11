import math
class Node:
    def __init__(self,value):
        self.value = value
        self.left:Node = None
        self.right:Node = None
    def __repr__(self):
        return f"{self.value} L:{self.left}, R:{self.right}"

class Tree:
    def __init__(self):
        self.root:Node = None
 
    def insert(self, value):
        node = Node(value)
        if self.empty():
            self.root = node
            return 
        current = self.root
        previous = self.root
        while current:
            previous = current
            if value < current.value:
                current = current.left
            else: current = current.right

        if value < previous.value:
            previous.left =node
        else: previous.right=node
        
    def find(self,value):
        current = self.root
        while current:
            if value < current.value:
                 current = current.left
            elif value > current.value:
                 current = current.right                
            else:return True
        return False
      
    def preorder(self,root):
        if not root: return
        print(root.value,end=",")
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root):
        if not root: return
        self.inorder(root.left)
        print(root.value,end=",")
        self.inorder(root.right)
    def postorder(self,root):
        if not root: return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value,end=",")
    
    def levelorder(self):
        height = self.height(self.root)
        for i in range(height):
            self.printAtKthDistance(self.root,i)
            print()

    def traverse(self,fn):
        fn(self.root)
        print()

    def height(self,root):
        if self.empty(): return -1
        if self.isLeaf(root): return 0
        return (1 + max(self.height(root.left), self.height(root.right)))

    def equals(self, root:Node, other:Node):
        if root == None and other == None:
            return True
        if root is not None and other is not None:
            return (root.value == other.value 
                    and self.equals(root.left, other.left) 
                    and self.equals(root.right, other.right))
        return False
    INF = 10000
    def isBTS(self,root,min=-INF,max=INF):
        if not root:return True
        return ((root.value >= min and root.value < max)
                and self.isBTS(root.left,min,root.value)
                and self.isBTS(root.right,root.value,max))
    
    def printAtKthDistance(self,root,distance):
        if not root: return 

        if distance ==0:
            print(root.value,end=", ")
            return

        self.printAtKthDistance(root.left,distance-1)
        self.printAtKthDistance(root.right,distance-1)


    def min(self):
        if self.empty(): return None
        current = self.root
        while current.left:
            current = current.left
        return current.value
    def max(self):
        if self.empty(): return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    def isLeaf(self,node):
        return bool(node == None or node.left==None and node.right==None) 
    def empty(self):
        return self.root == None
    
if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(9)
    tree.insert(2)
    tree.insert(8)
    tree.insert(4)
    tree.insert(7)
    tree.insert(6)
    tree.insert(1)
    tree.insert(1)
 
    print(tree.height(tree.root))
    tree.levelorder()