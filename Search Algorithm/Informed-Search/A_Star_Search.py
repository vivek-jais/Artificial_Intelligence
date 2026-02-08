'''
A* search expands node in order of increasing f(n) = g(n)+h(n)

Complete : Yes
Optimal :Yes
Efficient : Yes
g(n) --> cost so far
h(n) --> estimated cost to goal
'''

class Node:
    def __init__(self,state,parent=None,action=None,path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def solution(self):
        path = []
        node = self
        while node:
            path.append(node.state)
            node= node.parent
        return path[::-1]

import heapq
def a_star_search(graph,start,goal,heuristic):
    fronteir = []
    heapq.heappush(fronteir,(heuristic[start],Node(start,None,None,0)))
    explored = set()

    while fronteir:
        f,node = heapq.heappop(fronteir)

        if node.state == goal:
            return node.solution()
        
        explored.add(node.state)

        for neighbor, cost in graph[node.state]:
            if neighbor not in explored:
                g = node.path_cost + cost
                h = heuristic[neighbor]
                child = Node(neighbor,node,None,g)
                heapq.heappush(fronteir,(g+h,child))
    return None

graph_cost = {
    'A': [('B',1), ('C',1)],
    'B': [('D',1), ('E',1)],
    'C': [('F',1)],
    'D': [],
    'E': [('F',1)],
    'F': []
}

heuristic = {
    'A': 2,
    'B': 2,
    'C': 1,
    'D': 3,
    'E': 1,
    'F': 0
}

result = a_star_search(graph_cost, 'A', 'F', heuristic)
print(result)
