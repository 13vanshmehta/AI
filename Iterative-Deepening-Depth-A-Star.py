import time

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

def manhattan_distance(state, goal):
    """Calculate Manhattan distance heuristic for 8-puzzle problem"""
    distance = 0
    size = int(len(state) ** 0.5)
    
    for i in range(len(state)):
        if state[i] != 0 and state[i] != goal[i]:
            # Find position of this tile in goal
            goal_pos = goal.index(state[i])
            
            # Calculate Manhattan distance
            x1, y1 = i % size, i // size
            x2, y2 = goal_pos % size, goal_pos // size
            distance += abs(x1 - x2) + abs(y1 - y2)
    
    return distance

def get_blank_position(state):
    """Find the position of the blank (0) in the state"""
    return state.index(0)

def get_successors(node):
    """Generate successor states by moving the blank tile"""
    successors = []
    blank_pos = get_blank_position(node.state)
    state = node.state
    size = int(len(state) ** 0.5)
    
    # Possible moves: up, right, down, left
    moves = [
        ('up', -size),
        ('right', 1),
        ('down', size),
        ('left', -1)
    ]
    
    for action, move in moves:
        new_pos = blank_pos + move
        
        # Check if the move is valid
        if (action == 'up' and blank_pos < size) or \
           (action == 'right' and (blank_pos % size) == size - 1) or \
           (action == 'down' and blank_pos >= len(state) - size) or \
           (action == 'left' and (blank_pos % size) == 0):
            continue
        
        # Create new state by swapping blank with adjacent tile
        new_state = list(state)
        new_state[blank_pos], new_state[new_pos] = new_state[new_pos], new_state[blank_pos]
        
        # Create successor node
        successor = Node(
            state=tuple(new_state),
            parent=node,
            action=action,
            path_cost=node.path_cost + 1
        )
        
        successors.append(successor)
    
    return successors

def ida_star_search(initial_state, goal_state):
    """Perform IDA* search"""
    initial_node = Node(state=initial_state)
    
    # Calculate initial threshold as the heuristic value of the initial state
    threshold = manhattan_distance(initial_state, goal_state)
    
    while True:
        # Track the minimum f-value that exceeds the current threshold
        next_threshold = float('inf')
        
        # Perform depth-first search with current threshold
        result, next_t = dfs_contour(initial_node, goal_state, 0, threshold, next_threshold)
        
        if result is not None:
            return result
        
        if next_t == float('inf'):
            return None  # No solution found
        
        threshold = next_t

def dfs_contour(node, goal_state, g, threshold, next_threshold):
    """DFS within the current threshold contour"""
    # Calculate f-value (g + h)
    f = g + manhattan_distance(node.state, goal_state)
    
    # If f exceeds threshold, return None and the minimum f-value for next iteration
    if f > threshold:
        return None, min(f, next_threshold)
    
    # If goal is reached, return the node
    if node.state == goal_state:
        return node, threshold
    
    min_threshold = float('inf')
    
    # Generate and explore successors
    for successor in get_successors(node):
        result, new_threshold = dfs_contour(successor, goal_state, g + 1, threshold, next_threshold)
        
        if result is not None:
            return result, threshold
        
        min_threshold = min(min_threshold, new_threshold)
    
    return None, min_threshold

def get_solution_path(node):
    """Reconstruct the solution path from the goal node"""
    path = []
    while node.parent:
        path.append((node.action, node.state))
        node = node.parent
    
    path.reverse()
    return path

def print_state(state):
    """Print a state in a grid format"""
    size = int(len(state) ** 0.5)
    for i in range(size):
        for j in range(size):
            print(f"{state[i*size+j]:2}", end=" ")
        print()

def main():
    # Get puzzle size from user
    print("Enter puzzle size (e.g., 3 for 8-puzzle):")
    size = int(input())
    total_tiles = size * size
    
    # Get initial state from user
    print(f"Enter the initial state ({total_tiles} numbers, 0 for blank):")
    initial_state = tuple(int(x) for x in input().split())
    
    # Get goal state from user
    print(f"Enter the goal state ({total_tiles} numbers, 0 for blank):")
    goal_state = tuple(int(x) for x in input().split())
    
    # Validate input
    if len(initial_state) != total_tiles or len(goal_state) != total_tiles:
        print("Error: Invalid input size")
        return
    
    print("\nInitial state:")
    print_state(initial_state)
    
    print("\nGoal state:")
    print_state(goal_state)
    
    # Solve the puzzle
    start_time = time.time()
    solution_node = ida_star_search(initial_state, goal_state)
    end_time = time.time()
    
    # Print solution
    if solution_node:
        solution_path = get_solution_path(solution_node)
        
        print("\nSolution found!")
        print(f"Number of moves: {len(solution_path)}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")
        
        print("\nSolution path:")
        current_state = initial_state
        print_state(current_state)
        
        for action, state in solution_path:
            print(f"\nMove: {action}")
            print_state(state)
    else:
        print("\nNo solution found!")

if __name__ == "__main__":
    main()