import math

# Alpha-Beta Pruning Function
def alpha_beta_pruning(depth, node_index, is_max, scores, alpha, beta, max_depth, path):
    # Base case: return leaf node value
    if depth == max_depth:
        path.append(node_index)
        return scores[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):  # each node has 2 children
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, scores, alpha, beta, max_depth, path)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} (MAX node): alpha={alpha}, beta={beta}")
                break  # Beta cut-off
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, scores, alpha, beta, max_depth, path)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} (MIN node): alpha={alpha}, beta={beta}")
                break  # Alpha cut-off
        return best


# -----------------------------
# Example tree for demonstration
# -----------------------------
# Binary tree leaves (depth = 3)
scores = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = int(math.log(len(scores), 2))

path = []

print("Leaf node values:", scores)
print("Applying Alpha-Beta Pruning...\n")

root_value = alpha_beta_pruning(0, 0, True, scores, -math.inf, math.inf, max_depth, path)

print("\nResult:")
print(f"Value of the root node (best achievable for MAX): {root_value}")
print(f"Nodes explored (leaf indices): {path}")
