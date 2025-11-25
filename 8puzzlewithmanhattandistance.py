def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                target_x = (val - 1) // 3
                target_y = (val - 1) % 3
                dist += abs(i - target_x) + abs(j - target_y)
    return dist


def is_goal(state):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    return state == goal


def get_neighbors(state):
    neighbors = []
    # find zero tile
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    # 4 possible moves
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            # swap
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def ida_star(start):
    def search(path, g, bound):
        state = path[-1]
        f = g + manhattan(state)

        # prune using f > current bound
        if f > bound:
            return f

        # goal check
        if is_goal(state):
            return "FOUND"

        min_threshold = float("inf")

        # explore neighbors
        for neighbor in get_neighbors(state):
            if neighbor not in path:    # avoid revisiting path states
                path.append(neighbor)
                result = search(path, g + 1, bound)

                if result == "FOUND":
                    return "FOUND"

                min_threshold = min(min_threshold, result)
                path.pop()

        return min_threshold

    bound = manhattan(start)
    path = [start]

    while True:
        result = search(path, 0, bound)

        if result == "FOUND":
            return path

        if result == float("inf"):
            return None  # unsolvable

        bound = result   # <-- FIXED (your syntax error)


start = [[1,2,3],[4,0,6],[7,5,8]]
print(ida_star(start))

