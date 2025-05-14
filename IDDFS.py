def get_tree_input():
    tree = {}
    
    # Get number of nodes
    while True:
        try:
            num_edges = int(input("Enter number of edges: "))
            if num_edges >= 0:
                break
            print("Please enter a non-negative number")
        except ValueError:
            print("Please enter a valid number")
    
    print("\nEnter edge pairs (format: 'node1 node2'):")
    for i in range(num_edges):
        while True:
            try:
                edge = input(f"Edge {i+1}: ").strip().split()
                if len(edge) != 2:
                    print("Invalid format. Please enter two nodes separated by space")
                    continue
                
                node1, node2 = edge
                
                # Initialize empty lists for new nodes
                if node1 not in tree:
                    tree[node1] = []
                if node2 not in tree:
                    tree[node2] = []
                
                # Add edges (for directed graph)
                tree[node1].append(node2)
                break
            except Exception as e:
                print(f"Error: {e}. Please try again.")
    
    return tree

def depth_limited_search(tree, current_node, limit, depth, visited, path):
    if depth > limit:
        return False
    
    visited.add(current_node)
    path.append(current_node)
    print(f"Visiting depth {depth}: {current_node}")
    
    if current_node not in tree:
        path.pop()
        return False
    
    for neighbor in tree[current_node]:
        if neighbor not in visited:
            if depth_limited_search(tree, neighbor, limit, depth + 1, visited, path):
                return True
    
    return True

def iterative_deepening_search(tree, root):
    max_depth = len(tree)
    levels = {}
    
    print("\nIDDFS Traversal:")
    for depth in range(max_depth):
        print(f"\nSearching at depth limit: {depth}")
        visited = set()
        path = []
        depth_limited_search(tree, root, depth, 0, visited, path)
        
        if path:
            levels[depth] = path.copy()
    
    print("\nTree Traversal Summary:")
    print(f"Total Levels = {len(levels)}")
    for level, nodes in levels.items():
        print(f"Level {level}: {' -> '.join(nodes)}")

def main():
    # Get the tree structure
    tree = get_tree_input()
    
    # Get starting node
    while True:
        start_node = input("\nEnter start node: ").strip()
        if start_node in tree:
            break
        print("Invalid start node. Please enter an existing node.")
    
    # Perform IDDFS
    iterative_deepening_search(tree, start_node)
    print("\nIDDFS traversal completed.")

if __name__ == "__main__":
    main()