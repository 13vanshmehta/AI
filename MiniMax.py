def minimax(depth, node_index, is_max, scores, height):
    # If we’ve reached the bottom of the tree
    if depth == height:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, height),
            minimax(depth + 1, node_index * 2 + 1, False, scores, height)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, height),
            minimax(depth + 1, node_index * 2 + 1, True, scores, height)
        )

# Example scores at leaf nodes
scores = [3, 5, 2, 9, 0, -1, 7, 4]
height = 3  # Tree depth

print("Optimal value is:", minimax(0, 0, True, scores, height))
