import math
from queue import PriorityQueue
from typing import Dict, List, Set, Tuple
from priorityQueue import Queue
from stack import Stack

class Node:
    def __init__(self,label:str):
        self.label = label
        self.edges:Dict[Node,List[Edge]]={}
    def addEdge(self,to:"Node",weight:int):
        if not self.edges.get(self):
            self.edges[self]=[]
        self.edges.get(self).append(Edge(self,to,weight))

    def getEdges(self)->List["Edge"]:
        return list(self.edges[self])
    def __repr__(self) -> str:
        return self.label
    
class Edge:
    def __init__(self,fromNode:Node,toNode:Node,weight:int):
        self.fromNode = fromNode
        self.toNode = toNode
        self.weight = weight
    def __repr__(self) -> str:
        return f"{self.fromNode}>{self.weight}>{self.toNode}"

class Path:
    def __init__(self):
        self.nodes:List[Node]=[]
    def add(self,node:Node):
        self.nodes.append(node)

class WeightedGraph:
    def __init__(self):
        self.nodes:Dict[str,Node]={}
    
    def add(self,label:str):
        if label in self.nodes: return
        self.nodes[label] =Node(label)
 
    
    def addEdge(self,node1:str,node2:str,weight:int):
        if node1 is None or node2 is  None: return
        if not node1 in self.nodes or not node2 in self.nodes: return

        self.nodes[node1].addEdge(node2,weight)
        self.nodes[node2].addEdge(node1,weight)
    

    def getShortestPath(self,fromNode:str,toNode:str)->Path:
        fromNode = self.nodes.get(fromNode)
        if not fromNode: return
        toNode = self.nodes.get(toNode)
        if not toNode: return

        distances:Dict[Node,int]={}
        for node in self.nodes:
            distances[node]=math.inf
        distances[fromNode] = 0
        
        previousNodes:Dict[Node,Node] = {}
        visited:Set[Node]=set()

        q = Queue()
        q.enqueue(self.nodeEntry(fromNode,0))
        while not q.isEmpty():
            current = q.dequeue().get("node")
            visited.add(current)
            for edge in current.getEdges():
                if edge.toNode in visited: continue
                newDistances = distances.get(current)+edge.weight
                if newDistances<distances.get(edge.toNode):
                    distances[edge.toNode] = newDistances
                    previousNodes[edge.toNode] = current
                    q.enqueue(self.nodeEntry(edge.toNode,newDistances))

        return self.buildPath(previousNodes,toNode)
    
    def buildPath(self,previousNodes:Dict[Node,Node],toNode:Node)->Path:
        stack = Stack
        stack.push(toNode)
        previous =  previousNodes.get(toNode)
        while previous:
            stack.push(previous)
            previous = previousNodes.get(previous)
        path = Path()
        while not stack.isEmpty():
            path.add(stack.pop().label)
        return path

    def nodeEntry(self,node:Node,priority:int)->dict[Node,int]:
        return dict(node=node,priority=priority)
    
    def print(self):
        for node in self.nodes.values():
            print(f"{node.label} is adjacent to {node.getEdges()}")

if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add("A")
    graph.add("B")
    graph.add("C")
    graph.add("D")
    graph.addEdge("A","B",2)
    graph.addEdge("C","D",4)
    graph.addEdge("B","C",4)
    graph.addEdge("D","A",7)
    path = graph.getShortestPath("A","D")
    print(path.nodes)
 



