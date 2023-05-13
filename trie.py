class Node:
    def __init__(self,char):
        self.char=char
        self.isEOW=False
        self.children={}
    def hasChild(self,char)->bool:
        return char in self.children
    def hasChildren(self)->bool:
        return len(self.children) !=0
    def setChild(self,char):
        self.children[char]=Node(char) 
    def getChild(self,char):
        return self.children.get(char)
    def getChildren(self):
        return self.children.values()
    def removeChild(self,char):
        del self.children[char]
    def __repr__(self) -> str:
        return self.char+(":eow" if self.isEOW else "")

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self,word:str):
        current = self.root
        for char in word:
            if not current.hasChild(char):
                current.setChild(char)
            current = current.getChild(char)
        current.isEOW=True

    def contains(self,word:str):
        current = self.root
        for char in word:
            if not current.hasChild(char):
                return False
            current = current.getChild(char)
        return current.isEOW==True
            
    def traverse(self,root:Node):
        for child in root.children.values():
            print(child.char,end=",")
            if child.isEOW==True:
                print()
            self.traverse(child)
           
    def remove(self,root:Node,word:str):
        if not word:
            root.isEOW = False
            return
        char=word[0]
        child =root.getChild(char)
        if not child:return
        self.remove(child,word[1:])
      
        if not child.hasChildren() and not child.isEOW:
            root.removeChild(char)

    def findWords(self,prefix:str):
        if not prefix :return []
        words=[]
        lastNode = self.findLastNodeOf(prefix)
        self.findCompleteWord(lastNode,words,prefix)
        return words
    
    def findLastNodeOf(self,prefix:str)->Node:
        current = self.root
        for char in prefix:
            if not current.hasChild(char):
                break
            current = current.getChild(char)
        return current
        

    def findCompleteWord(self,root:Node,words,prefix):
        if not root: return 
        if root.isEOW:
            words.append(prefix)
        for child in root.getChildren():
            self.findCompleteWord(child,words,prefix+child.char)




if __name__=='__main__':
    trie = Trie()
    trie.insert("bag")
    trie.insert("bagi")
    trie.insert("boy")
    trie.insert("cat")
    trie.insert("catelog")
    trie.insert("bat")
    # trie.traverse(trie.root)
    print(trie.findWords("ca"))
