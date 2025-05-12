import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic (estimated cost from current to goal)
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f

def heuristic(position, goal):
    # Manhattan distance heuristic
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def get_neighbors(node, grid):
    neighbors = []
    # Define possible movements (up, right, down, left)
    movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    for movement in movements:
        new_position = (node.position[0] + movement[0], node.position[1] + movement[1])
        
        # Check if the new position is valid
        if (0 <= new_position[0] < len(grid) and 
            0 <= new_position[1] < len(grid[0]) and 
            grid[new_position[0]][new_position[1]] != 1):  # 1 represents obstacles
            
            new_node = Node(new_position, node)
            neighbors.append(new_node)
    
    return neighbors

def a_star_search(grid, start, goal):
    # Create start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)
    
    # Initialize open and closed lists
    open_list = []
    closed_list = []
    
    # Add the start node to the open list
    heapq.heappush(open_list, start_node)
    
    # Loop until the open list is empty
    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)
        
        # Print current position being evaluated
        print(f"Evaluating: {current_node.position}")
        
        # Check if we've reached the goal
        if current_node == goal_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path
        
        # Generate neighbors
        neighbors = get_neighbors(current_node, grid)
        
        for neighbor in neighbors:
            # Skip if neighbor is in the closed list
            if neighbor in closed_list:
                continue
            
            # Calculate g, h, and f values
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h
            
            # Skip if neighbor is already in open list with a lower f value
            skip = False
            for open_node in open_list:
                if neighbor == open_node and neighbor.g > open_node.g:
                    skip = True
                    break
            
            if skip:
                continue
            
            # Add neighbor to open list
            heapq.heappush(open_list, neighbor)
    
    # No path found
    return None

def print_grid_with_path(grid, path):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            position = (i, j)
            if position in path:
                if position == path[0]:
                    print("S", end=" ")  # Start
                elif position == path[-1]:
                    print("G", end=" ")  # Goal
                else:
                    print("*", end=" ")  # Path
            elif grid[i][j] == 1:
                print("#", end=" ")  # Obstacle
            else:
                print(".", end=" ")  # Empty space
        print()

if __name__ == "__main__":
    # Get grid dimensions from user
    print("Enter grid dimensions (rows columns):")
    rows, cols = map(int, input().split())
    
    # Initialize grid
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Get obstacles from user
    print(f"Enter number of obstacles (max {rows * cols - 2}):")
    num_obstacles = int(input())
    
    print("Enter obstacle positions (row column), one per line:")
    for _ in range(num_obstacles):
        obstacle_row, obstacle_col = map(int, input().split())
        grid[obstacle_row][obstacle_col] = 1
    
    # Get start and goal positions
    print("Enter start position (row column):")
    start_row, start_col = map(int, input().split())
    start = (start_row, start_col)
    
    print("Enter goal position (row column):")
    goal_row, goal_col = map(int, input().split())
    goal = (goal_row, goal_col)
    
    # Run A* search
    print("\nRunning A* Search...")
    path = a_star_search(grid, start, goal)
    
    # Print results
    if path:
        print("\nPath found!")
        print("Path:", path)
        print("\nGrid with path:")
        print_grid_with_path(grid, path)
    else:
        print("\nNo path found!")