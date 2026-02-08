'''--runs 2 simultaneous searches
--- one forward from the start and one from the backward and stop when they meet'''
# Time = O(b^(d/2))
# Space = O(b^(d/2))

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


def reconstruct_path(meet_node_fwd,meet_node_bwd):
    path_fwd = meet_node_fwd.solution()
    path_bwd = meet_node_bwd.solution()
    return path_fwd + path_bwd[-2::-1]



from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    start_node = Node(start)
    goal_node = Node(goal)

    frontier_fwd = deque([start_node])
    frontier_bwd = deque([goal_node])

    explored_fwd = {start: start_node}
    explored_bwd = {goal: goal_node}

    while frontier_fwd and frontier_bwd:
        
        #forward step
        node_fwd = frontier_fwd.popleft()
        for neighbor in graph[node_fwd.state]:
            if neighbor not in explored_fwd:
                child = Node(neighbor, node_fwd)
                explored_fwd[neighbor] = child
                frontier_fwd.append(child)

                if neighbor in explored_bwd:
                    return reconstruct_path(child, explored_bwd[neighbor])

        #Backward step
        node_bwd = frontier_bwd.popleft()
        for neighbor in graph[node_bwd.state]:
            if neighbor not in explored_bwd:
                child = Node(neighbor, node_bwd)
                explored_bwd[neighbor] = child
                frontier_bwd.append(child)

                if neighbor in explored_fwd:
                    return reconstruct_path(explored_fwd[neighbor], child)

    return None


graph = {
    'A' : ['B','C'],
    'B' : ['D','E''A'],
    'C' : ['F','A'],
    'D' : ['B'],
    'E' : ['F','B'],
    'F' :['C','E']
}

path = bidirectional_search(graph,'A','D')


print("Path: ",path)


    
        