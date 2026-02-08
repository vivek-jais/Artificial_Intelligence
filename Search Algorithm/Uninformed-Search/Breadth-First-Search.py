'''Properties of BFS:
     complete,optimal,b^d,b^d'''

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' :[]
}

#Node class
class Node:
    def __init__(self,state,parent =None):
        self.state =state
        self.parent =parent

    def reconstruct(self):
        path =[]
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]
    
#BFS Function
from collections import deque
def bfs(graph,start,goal):
    frontier = deque([Node(start)])
    visited = set()

    while frontier:
        node = frontier.popleft()

        if node.state == goal:
            print("Goal found!")
            return node.reconstruct()
        
        visited.add(node.state)

        for neighbor in graph[node.state]:
            #to check front dublicatoin, Avoid same state appearing twice
            if neighbor not in visited and all(n.state != neighbor for n in frontier):
                frontier.append(Node(neighbor,node))
    return None

path  = bfs(graph,'A','F')

if path:
    print("Path:",path)
else:
    print("Goal not found")