from typing import List, overload
from simpleQueue import Queue
from stack import Stack

class Node:
    def __init__(self,label:str):
        self.label = label
        self.visited=False


    def __repr__(self) -> str:
        return self.label



class Graph:
    def __init__(self):
        self.nodes={}
        self.adjacency={}
    
    def add(self,label):
        node = Node(label)
        if not label in self.nodes:
            self.nodes[label]=node
            self.adjacency[node]=[]
    
    def addEdge(self,fromNode,toNode):
        if not (fromNode in self.nodes and toNode in self.nodes):  
            raise ValueError("Not valid params")
        node = self.nodes[fromNode]
        self.adjacency[node].append(self.nodes[toNode])
    
    def remove(self,label):
        if not label in self.nodes:
            return None
        node = self.nodes[label]
        for edges in self.adjacency.values():
            if node in edges:
                edges.remove(node)
        del self.nodes[label]
        return node


    def removeEdge(self, fromNode, toNode):
        node = self.nodes.get(fromNode)
        edges = self.adjacency.get(node)
        if not (node and edges):return
        for edge in edges:
            if toNode == edge.label:
                edges.remove(edge)

    def depthFirst(self,label:str):
        node = self.nodes.get(label)
        if not node or node.visited: return
        print(node.label,end=", ")
        node.visited =True
        edges = self.adjacency.get(node)
        if not edges:
            return
        for edge in edges:
            self.depthFirst(edge.label)
    

    def breadthFirst(self, label):
        q = Queue()
        node = self.nodes.get(label)
        if not node: return
        q.enqueue(node)
        while not q.isEmpty():
            node = q.dequeue()
            if node.visited:continue
            print(node.label,end=", ")
            node.visited = True
            for edge in self.adjacency[node]:
                q.enqueue(edge)

    def topologicalSort(self,stack:Stack,label):
        node = self.nodes.get(label)
        if not node or node.visited: return
        node.visited=True
        neighbors = self.adjacency.get(node,[])
        for neighbor in neighbors:
            self.topologicalSort(stack,neighbor.label,)
        stack.push(node)     

    def hasCycle(self):
        all =list(self.nodes.values())
        visiting =[] 
        visited  =[]
        while all:
            if self.findHasCycle(all[0],all,visiting,visited):
                return True
        return False
 
    def findHasCycle(self,node,all:List,visiting:List,visited:List):
        all.remove(node)
        visiting.append(node)
        for neighbour in self.adjacency.get(node,[]):
            if neighbour in visited:
                continue
            if neighbour in visiting:
                return True
            if (self.findHasCycle(neighbour,all,visiting,visited)):
                return True
        visiting.remove(node)
        visited.append(node)
        return False

      
    def print(self):
        for node in self.nodes.values():
            if self.adjacency.get(node):
                print(f"{node}'s neighbour: {self.adjacency[node]}")

if __name__ == "__main__":
    graph = Graph()
    graph.add("a")
    graph.add("b")
    graph.add("c")
    graph.add("d")
    graph.addEdge("a","b")
    graph.addEdge("a","c")
    graph.addEdge("b","c") 
    graph.addEdge("c","a")
    graph.addEdge("d","a")
    print(graph.hasCycle())
    