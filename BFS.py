from collections import deque

def bfs(graph, start, goal):
    # Create a queue for BFS and add the start node
    queue = deque([start])
    # Set to keep track of visited nodes to avoid cycles
    visited = set()
    # Dictionary to keep track of the path
    parent = {start: None}
    
    while queue:
        # Dequeue a node from the front of the queue
        current = queue.popleft()
        
        # If the goal is found, reconstruct the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        
        # Mark the current node as visited
        visited.add(current)
        
        # Get all the adjacent nodes of the current node
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                # Add the neighbor to the queue
                queue.append(neighbor)
                # Set the parent of the neighbor to reconstruct the path later
                parent[neighbor] = current
    
    return None  # Return None if no path is found

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'J'],
    'G': [],
    'H': ['K'],
    'I': [],
    'J': [],
    'K': []
}

# Start and goal nodes
start_node = 'A'
goal_node = 'K'

# Perform BFS
path = bfs(graph, start_node, goal_node)

# Print the result
print(f"Path from {start_node} to {goal_node}: {path}")

# Output: Path from A to K: ['A', 'D', 'H', 'K']