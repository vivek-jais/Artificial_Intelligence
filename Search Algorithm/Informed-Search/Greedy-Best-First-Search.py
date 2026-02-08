'''
Complete: NO,
Optimal :NO,
time : O(b^m)
space: O(b^m)

looks only at heuristic function --> how closest to the goal
'Greedy' -> looks what best now
'''

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
    

import heapq # min heap    
def greedy_best_first_search(graph,start,goal,heuristic):
    frontier =[]
    heapq.heappush(frontier,(heuristic[start],Node(start)))
    explored = set()

    while frontier:
        _,node  = heapq.heappop(frontier)

        if node.state == goal:
            return node.solution()
        
        explored.add(node.state)

        for neighbor in graph[node.state]:
            if neighbor not in explored:
                child = Node(neighbor,node)
                heapq.heappush(frontier,(heuristic[neighbor],child))

    return None


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' :[]
}
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 1,
    'F': 0
}


path = greedy_best_first_search(graph,'A','F',heuristic)
if path:
    print("Path:",path)