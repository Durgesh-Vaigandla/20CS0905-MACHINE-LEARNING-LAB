import heapq

class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name
        self.g = g  # Cost from start to this node
        self.h = h  # Heuristic cost from this node to goal
        self.f = g + h  # Total cost
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def a_star(graph, start, goal, h):
    open_list = []
    closed_list = set()
    
    start_node = Node(start, 0, h[start])
    goal_node = Node(goal)
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.name == goal_node.name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]
        
        closed_list.add(current_node.name)
        
        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue
            
            g = current_node.g + cost
            h_cost = h[neighbor]
            neighbor_node = Node(neighbor, g, h_cost)
            neighbor_node.parent = current_node
            
            if any(open_node for open_node in open_list if open_node.name == neighbor and open_node.g <= g):
                continue
            
            heapq.heappush(open_list, neighbor_node)
    
    return None

def rbfs(node, goal, f_limit, graph, h):
    if node.name == goal:
        return [node.name], node.g
    
    successors = []
    for neighbor, cost in graph[node.name].items():
        g = node.g + cost
        h_cost = h[neighbor]
        successor = Node(neighbor, g, h_cost)
        successor.parent = node
        successors.append(successor)
    
    if not successors:
        return None, float('inf')
    
    for s in successors:
        s.f = max(s.f, node.f)
    
    while True:
        successors.sort(key=lambda x: x.f)
        best = successors[0]
        
        if best.f > f_limit:
            return None, best.f
        
        alternative = successors[1].f if len(successors) > 1 else float('inf')
        result, best.f = rbfs(best, goal, min(f_limit, alternative), graph, h)
        
        if result is not None:
            return [node.name] + result, best.f

def memory_bounded_a_star(graph, start, goal, h):
    start_node = Node(start, 0, h[start])
    path, _ = rbfs(start_node, goal, float('inf'), graph, h)
    return path

# Example graph represented as an adjacency list with edge weights
graph = {
    'A': {'B': 1, 'C': 4, 'D': 2},
    'B': {'E': 2, 'F': 3},
    'C': {'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 1, 'J': 4},
    'G': {},
    'H': {'K': 3},
    'I': {},
    'J': {},
    'K': {}
}

# Heuristic values for each node (example heuristic, could be any appropriate values)
heuristic = {
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 4,
    'E': 3,
    'F': 6,
    'G': 0,
    'H': 2,
    'I': 3,
    'J': 4,
    'K': 0
}

start_node = 'A'
goal_node = 'K'

# Perform A* Search
a_star_path = a_star(graph, start_node, goal_node, heuristic)
print(f"A* Path from {start_node} to {goal_node}: {a_star_path}")

# Perform Memory-Bounded A* Search
mb_a_star_path = memory_bounded_a_star(graph, start_node, goal_node, heuristic)
print(f"Memory-Bounded A* Path from {start_node} to {goal_node}: {mb_a_star_path}")

# Output
# A* Path from A to K: ['A', 'D', 'H', 'K']
# Memory-Bounded A* Path from A to K: ['A', 'D', 'H', 'K']