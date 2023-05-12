class Node:
    def __init__(self,value):
        self.value = value
        self.height = 0
        self.left:Node=None
        self.right:Node=None
    def __repr__(self) -> str:
        return f"{self.value}:{self.height}"

class AVLTree:
    def __init__(self):
        self.root =None
    
    def inserting(self,root:Node,value):
        if not root:
            return Node(value)
        if  value < root.value:
            root.left =self.inserting(root.left,value)
        else:
            root.right =self.inserting(root.right,value)

        self.setHeight(root)
        return self.balance(root)
    
    def rotateLeft(self, root):
        newroot = root.right
        root.right = newroot.left
        newroot.left = root
        self.setHeight(root)
        self.setHeight(newroot)
        return newroot
    def rotateRight(self, root):
        newroot = root.left
        root.left = newroot.right
        newroot.right = root
        self.setHeight(root)
        self.setHeight(newroot)
        return newroot
    def balance(self,root:Node):
        if self.leftHeavy(root):
            if self.balancefactor(root.left)<0:
                root.left=self.rotateLeft(root.left)
            return self.rotateRight(root)
        elif self.rightHeavy(root):
            if self.balancefactor(root.right)>0:
                root.right=self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root

    def insert(self,value):
        self.root = self.inserting(self.root,value)
    def balancefactor(self,node:Node):
        return self.height(node.left) - self.height(node.right) if node else 0
    def leftHeavy(self,node):
        return self.balancefactor(node)  > 1
    def rightHeavy(self,node):
        return self.balancefactor(node) < -1
    def height(self,root):
        return -1 if not root else root.height
    def setHeight(self,node:Node):
        node.height = 1 + max(self.height(node.left),
                              self.height(node.right))
    def traverse(self,root):
        if not root: return 
        self.traverse(root.left)
        print(root,end="; ")
        self.traverse(root.right)
    def empty(self):
        return self.root == None


if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    avl.insert(6)
    avl.insert(7)
    avl.insert(8)
    avl.insert(8)
    avl.traverse(avl.root)