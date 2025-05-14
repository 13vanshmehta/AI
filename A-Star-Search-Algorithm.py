import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.g_score = float('inf')  # Cost from start to current node
        self.h_score = 0             # Heuristic (estimated cost to goal)
        self.f_score = float('inf')  # Total score (g + h)
        self.parent = None

class Tree:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by value
    
    def add_edge(self, parent_val, child_val):
        # Create parent node if it doesn't exist
        if parent_val not in self.nodes:
            self.nodes[parent_val] = Node(parent_val)
        
        # Create child node if it doesn't exist
        if child_val not in self.nodes:
            self.nodes[child_val] = Node(child_val)
        
        # Add child to parent's children
        parent_node = self.nodes[parent_val]
        child_node = self.nodes[child_val]
        parent_node.children.append(child_node)
    
    def set_heuristic(self, node_val, h_value):
        if node_val in self.nodes:
            self.nodes[node_val].h_score = h_value
    
    def a_star_search(self, start_val, goal_val):
        if start_val not in self.nodes or goal_val not in self.nodes:
            return None, "Start or goal node not found in the tree"
        
        # Initialize start node
        start_node = self.nodes[start_val]
        start_node.g_score = 0
        start_node.f_score = start_node.h_score
        
        # Priority queue for open set (nodes to be evaluated)
        open_set = [(start_node.f_score, start_val)]
        open_set_hash = {start_val}  # For faster lookup
        
        # Closed set (nodes already evaluated)
        closed_set = set()
        
        # Path tracking
        path_found = False
        
        # For visualization
        steps = []
        
        while open_set:
            # Get node with lowest f_score
            current_f, current_val = heapq.heappop(open_set)
            current_node = self.nodes[current_val]
            
            # Remove from open set
            open_set_hash.remove(current_val)
            
            # Add to closed set
            closed_set.add(current_val)
            
            # Record step for visualization
            steps.append({
                'current': current_val,
                'open_set': [n for _, n in open_set],
                'closed_set': list(closed_set)
            })
            
            # Check if goal reached
            if current_val == goal_val:
                path_found = True
                break
            
            # Explore neighbors (children)
            for child_node in current_node.children:
                child_val = child_node.value
                
                # Skip if already evaluated
                if child_val in closed_set:
                    continue
                
                # Calculate tentative g_score (cost from start to neighbor through current)
                # Assuming each edge has a cost of 1
                tentative_g_score = current_node.g_score + 1
                
                # If this path is better than any previous one
                if tentative_g_score < child_node.g_score:
                    # Update path
                    child_node.parent = current_node
                    child_node.g_score = tentative_g_score
                    child_node.f_score = tentative_g_score + child_node.h_score
                    
                    # Add to open set if not already there
                    if child_val not in open_set_hash:
                        heapq.heappush(open_set, (child_node.f_score, child_val))
                        open_set_hash.add(child_val)
        
        # Reconstruct path if found
        if path_found:
            path = []
            current = self.nodes[goal_val]
            
            while current:
                path.append(current.value)
                current = current.parent
            
            path.reverse()
            return path, steps
        
        return None, "No path found"

def main():
    
    tree = Tree()
    
    # Get number of edges
    try:
        n = int(input("Enter number of edges: "))
        
        print("\nEnter edges (format: 'node1 node2'):")
        print("node1 is parent, node2 is child")
        
        for i in range(n):
            edge = input(f"Edge {i+1}: ").strip().split()
            if len(edge) != 2:
                print("Invalid format. Please enter two values separated by space.")
                i -= 1
                continue
            
            parent_val, child_val = edge
            tree.add_edge(parent_val, child_val)
        
        # Get heuristic values
        print("\nEnter heuristic values (estimated distance to goal):")
        print("Format: 'node h_value'")
        print("Enter 'done' when finished")
        
        while True:
            inp = input("> ").strip()
            
            if inp.lower() == 'done':
                break
                
            parts = inp.split()
            if len(parts) != 2:
                print("Invalid format. Please use 'node h_value'")
                continue
            
            node_val, h_value = parts
            
            try:
                h_value = float(h_value)
                tree.set_heuristic(node_val, h_value)
            except ValueError:
                print("Heuristic value must be a number")
        
        # Get start and goal nodes
        start_val = input("\nEnter start node: ")
        goal_val = input("Enter goal node: ")
        
        # Run A* search
        path, steps = tree.a_star_search(start_val, goal_val)
        
        # Display results
        if isinstance(path, list):
            print("\nPath found:", " -> ".join(path))
            
            print("\nSearch steps:")
            for i, step in enumerate(steps):
                print(f"Step {i+1}:")
                print(f"  Current node: {step['current']}")
                print(f"  Open set: {', '.join(step['open_set']) if step['open_set'] else 'empty'}")
                print(f"  Closed set: {', '.join(step['closed_set'])}")
        else:
            print("\nError:", steps)
            
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()