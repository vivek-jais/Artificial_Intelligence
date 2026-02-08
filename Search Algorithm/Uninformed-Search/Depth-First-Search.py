'''
Properties:
complete : No
optimal : No,
Time :  b^m
Space:  b^m  m= maximum depth
'''

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' :[]
}

# Node class

class Node:
    def __init__(self,state,parent=None):
        self.state = state
        self.parent = parent

    def solution(self):
        path =[]
        node = self
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]
    
def dfs(graph,start,goal):
    stack = [Node(start)]
    visited = set()

    while stack:
        node = stack.pop()

        if node.state == goal:
            print("Goal Found !")
            return node.solution()
        
        visited.add(node.state)

        for neighbor in reversed(graph[node.state]):
            if neighbor not in visited:
                stack.append(Node(neighbor,node))

    return None


path = dfs(graph,'A',"F")
print("Path",path)

