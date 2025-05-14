import heapq

def input_weighted_tree():
    tree = {}
    n = int(input("Enter number of nodes in the tree: "))
    print("For each node, enter children in format: child:cost (comma-separated), or leave blank if none.")
    for _ in range(n):
        node = input("Node: ")
        children_input = input(f"Children of {node}: ")
        children = []
        if children_input:
            for child_pair in children_input.split(','):
                child, cost = child_pair.strip().split(':')
                children.append((child.strip(), int(cost)))
        tree[node] = children
    return tree

def get_all_nodes(tree):
    # Collect all nodes including children
    all_nodes = set(tree.keys())
    for node in tree:
        for child, _ in tree[node]:
            all_nodes.add(child)
    return all_nodes

def heuristic(a, b):
    # Simple heuristic: difference of ASCII values
    return abs(ord(str(a)) - ord(str(b)))

def a_star(tree, start, goal):
    # Initialize all nodes
    all_nodes = get_all_nodes(tree)
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Initialize scores for all nodes
    g_scores = {node: float('inf') for node in all_nodes}
    g_scores[start] = 0
    
    f_scores = {node: float('inf') for node in all_nodes}
    f_scores[start] = heuristic(start, goal)
    
    came_from = {}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor, cost in tree.get(current, []):
            tentative_g_score = g_scores[current] + cost
            
            if tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_scores[neighbor], neighbor))
    
    return None

def main():
    print("A* Algorithm Implementation")
    print("==========================")
    
    try:
        tree = input_weighted_tree()
        start = input("\nEnter start node: ")
        goal = input("Enter goal node: ")
        
        print("\nSearching for path...")
        path = a_star(tree, start, goal)
        
        if path:
            print("\nPath found!")
            print("Path:", " -> ".join(path))
            print("\nNote: Numbers show the order of nodes visited")
        else:
            print("\nNo path found between", start, "and", goal)
            
    except ValueError as e:
        print("\nError: Please enter valid numeric values for costs")
    except Exception as e:
        print("\nAn error occurred:", str(e))

if __name__ == "__main__":
    main()