def dls(graph, start, goal, depth):
    if depth == 0:
        return start == goal
    if depth > 0:
        for neighbor in graph.get(start, []):
            if dls(graph, neighbor, goal, depth - 1):
                return True
    return False

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        if dls(graph, start, goal, depth):
            print(f"Goal node '{goal}' found at depth {depth}")
            return True
    print(f"Goal node '{goal}' not found up to depth {max_depth}")
    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['G'],
    'F': ['K'],
    'K': []
}

start_node = 'A'
goal_node = 'K'
max_depth = 4

iddfs(graph, start_node, goal_node, max_depth)
