from collections import defaultdict

class Tree:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def depth_limited_search(self, source, target, max_depth):
        if source == target:
            return True
        
        if max_depth <= 0:
            return False
            
        for neighbor in self.graph[source]:
            if self.depth_limited_search(neighbor, target, max_depth - 1):
                return True
        
        return False
    
    def iterative_deepening_dfs(self, source, target, max_depth):
        for depth in range(max_depth + 1):
            print(f"\nDepth limit: {depth}")
            print(f"Vertices visited: ", end="")
            
            self.visited = set()
            
            if self.depth_limited_search_with_print(source, target, depth):
                print(f"\nTarget {target} found at depth {depth}")
                return True
                
        print(f"\nTarget {target} not found within depth {max_depth}")
        return False
    
    def depth_limited_search_with_print(self, source, target, max_depth):
        self.visited.add(source)
        print(source, end=" ")
        
        if source == target:
            return True
        
        if max_depth <= 0:
            return False
            
        for neighbor in self.graph[source]:
            if neighbor not in self.visited:
                if self.depth_limited_search_with_print(neighbor, target, max_depth - 1):
                    return True
        
        return False

def main():
    tree = Tree()
    
    print("Iterative Deepening DFS Implementation")
    
    try:
        n = int(input("Enter the number of edges: "))
        
        print("\nEnter edges (format: 'node1 node2'):")
        
        for i in range(n):
            edge = input(f"Edge {i+1}: ").strip().split()
            if len(edge) != 2:
                print("Invalid format. Please enter two nodes separated by space.")
                i -= 1
                continue
            
            u, v = edge
            tree.add_edge(u, v)
        
        source = input("\nEnter the source vertex: ")
        target = input("Enter the target vertex: ")
        max_depth = int(input("Enter the maximum depth to search: "))
        
        print(f"\nIterative Deepening DFS from {source} to find {target}:")
        tree.iterative_deepening_dfs(source, target, max_depth)
            
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()