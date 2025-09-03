def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                target_x = (val-1) // 3
                target_y = (val-1) % 3
                dist += abs(i - target_x) + abs(j - target_y)
    return dist

def ida_star(start):
    def search(path, g, bound):
        state = path[-1]
        f = g + manhattan(state)
        if f > bound:
            return f
        if is_goal(state):
            return "FOUND"
        min_threshold = float("inf")
        for neighbor in get_neighbors(state):
            if neighbor not in path:
                path.append(neighbor)
                result = search(path, g+1, bound)
                if result == "FOUND":
                    return "FOUND"
                if result < min_threshold:
                    min_threshold = result
                path.pop()
        return min_threshold

    bound = manhattan(start)
    path = [start]
    while True:
        result = search(path, 0, bound)
        if result == "FOUND":
            return path
        if result == float("inf"):
            return None
        bound = result
