from collections import defaultdict

class Tree:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self, start_node):
        if start_node not in self.graph:
            return f"Node {start_node} not found in the tree"
        
        visited = set()
        result = []
        
        def dfs_util(node):
            visited.add(node)
            result.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)
        
        dfs_util(start_node)
        return result

def main():
    tree = Tree()
    
    print("DFS Implementation")
    
    try:
        n = int(input("Number of edges: "))
        
        print("\nEnter edges (format: 'node1 node2'):")
        for i in range(n):
            edge = input(f"Edge {i+1}: ").split()
            if len(edge) == 2:
                u, v = edge
                tree.add_edge(u, v)
        
        start = input("\nStarting node: ")
        result = tree.dfs(start)
        
        if isinstance(result, list):
            print("\nDFS Traversal:", " -> ".join(result))
        else:
            print("\nError:", result)
            
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()