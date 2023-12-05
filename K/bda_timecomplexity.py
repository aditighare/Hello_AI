import networkx as nx
import time
import heapq

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'C'},
    'E': {'B', 'F'},
    'F': {'C', 'E'},
}

G = nx.Graph(graph)

# Define start and goal nodes
start_node = 'A'
goal_node = 'F'

# Depth-First Search (DFS)
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        for next_node in graph[node] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                stack.append((next_node, path + [next_node]))
    return None

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for next_node in graph[node] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))
    return None

# A* Algorithm
def heuristic(node, goal):
    # Define a simple heuristic function for A*
    return len(set(goal) - set(node))

def astar(graph, start, goal):
    open_list = [(heuristic(start, goal), start, [start])]
    while open_list:
        open_list.sort()  # Sort by heuristic cost
        _, node, path = open_list.pop(0)
        for next_node in graph[node] - set(path):
            if next_node == goal:
                return path + [next_node]
            else:
                new_path = path + [next_node]
                cost = len(new_path) + heuristic(next_node, goal)
                open_list.append((cost, next_node, new_path))
    return None

# Measure execution time of each algorithm
start_time = time.time()
dfs_path = dfs(graph, start_node, goal_node)
dfs_time = time.time() - start_time

start_time = time.time()
bfs_path = bfs(graph, start_node, goal_node)
bfs_time = time.time() - start_time

start_time = time.time()
astar_path = astar(graph, start_node, goal_node)
astar_time = time.time() - start_time

# Print the paths and execution times
print("DFS Path:", dfs_path)
print("DFS Time:", dfs_time)

print("BFS Path:", bfs_path)
print("BFS Time:", bfs_time)

print("A* Path:", astar_path)
print("A* Time:", astar_time)

# Plot the execution times
algorithms = ['DFS', 'BFS', 'A*']
times = [dfs_time, bfs_time, astar_time]
