'''it is version of depth first search in which the search is cut off at the predefined depth'''

# depth limit
# cutoff is a special result
'''
Complete : NO
Optimal : NO
Time : O(b^l)
Space : O(bl)
'''

class Node:
    def __init__(self,state,parent=None):
        self.state = state
        self.parent = parent
    
    def solution(self):
        path =[]
        node =self
        while node:
            path.append(node.state)
            node = node.parent
        return path[::-1]
        

def depth_limited_search(graph,node,goal,limit):
    if node.state == goal:
        return node
    
    if limit == 0:
        return "cutoff"
    
    cutoff_occurred = False

    for neighbor in graph[node.state]:
        child = Node(neighbor,node)
        result = depth_limited_search(graph,child,goal,limit-1)

        if result == "cutoff":
            cutoff_occurred = True
        elif result is not None:
            return result
        
    if cutoff_occurred:
        return "cutoff"
    
    else:
        return None


# ITERATIVE DEEPENING SEARCH
def iterative_deepening_search(graph,start,goal):
    depth=0
    while True:
        result = depth_limited_search(graph,start,goal,depth)

        if result != "cutoff":
            return result
        
        depth+=1

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' :[]
}

start_node = Node('A')
result = depth_limited_search(graph,start_node,'D',limit=10)
result1 = iterative_deepening_search(graph,start_node,'D')

if result == "cutoff":
    print("Cutoff occurred")
elif result:
    print("Path:",result.solution())
else:
    print("Failure")

#Iterative deepening search
if result1 == "cutoff":
    print("Cutoff occurred")
elif result1:
    print("Path:",result1.solution())
else:
    print("Failure")

