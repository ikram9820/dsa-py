
class Node:
    def __init__(self,value):
        self.value = value
        self.left:Node = None
        self.right:Node = None

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
            if value <= current.value:
                current = current.left
            else: current = current.right

        if value <= previous.value:
            previous.left =node
        else: previous.right=node
        
    def find(self,value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else: current = current.right
        return False
    
    # def inorder(self,node):
    #     if not node:
    #         return
    #     inorder(node.left)
    #     print(node.value)
    #     inorder(node.right)

    # def traverse(self):
    #     current= self.root
    #     while current:
    #         print(current.value)
    #         if current.left and current.value <= current.left.value:
    #             current = current.left
    #         elif current.right and current.value > current.right.value: 
    #             current = current.right
    #         else: break 

    def empty(self):
        return self.root == None
    
if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(9)
    tree.insert(2)
    tree.insert(8)
    tree.insert(1)
    tree.insert(4)
    print(tree.find(9))