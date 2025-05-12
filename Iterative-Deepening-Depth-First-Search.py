from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # A function to perform depth-limited search
    def depth_limited_search(self, source, target, max_depth):
        if source == target:
            return True
        
        # If reached the maximum depth, stop recursion
        if max_depth <= 0:
            return False
            
        # Recur for all adjacent vertices
        for neighbor in self.graph[source]:
            if self.depth_limited_search(neighbor, target, max_depth - 1):
                return True
        
        return False
    
    # IDDFS to search if target is reachable from source
    def iterative_deepening_dfs(self, source, target, max_depth):
        # Perform DLS at increasing depths
        for depth in range(max_depth + 1):
            print(f"\nDepth limit: {depth}")
            print(f"Vertices visited: ", end="")
            
            # Reset visited for each depth iteration
            self.visited = set()
            
            if self.depth_limited_search_with_print(source, target, depth):
                print(f"\nTarget {target} found at depth {depth}")
                return True
                
        print(f"\nTarget {target} not found within depth {max_depth}")
        return False
    
    # Modified DLS that prints visited vertices
    def depth_limited_search_with_print(self, source, target, max_depth):
        # Mark current node as visited and print it
        self.visited.add(source)
        print(source, end=" ")
        
        if source == target:
            return True
        
        # If reached the maximum depth, stop recursion
        if max_depth <= 0:
            return False
            
        # Recur for all adjacent vertices
        for neighbor in self.graph[source]:
            if neighbor not in self.visited:
                if self.depth_limited_search_with_print(neighbor, target, max_depth - 1):
                    return True
        
        return False

# Main function
if __name__ == "__main__":
    g = Graph()

    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter edges (format: source destination):")
    for i in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    source = int(input("Enter the source vertex: "))

    target = int(input("Enter the target vertex: "))

    max_depth = int(input("Enter the maximum depth to search: "))
    
    print(f"\nIterative Deepening DFS from {source} to find {target}:")
    g.iterative_deepening_dfs(source, target, max_depth)