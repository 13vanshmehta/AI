from collections import defaultdict, deque

class Tree:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start_node):
        if start_node not in self.graph:
            return f"Node {start_node} not found in the tree"
        
        visited = set()
        
        queue = deque([start_node])
        visited.add(start_node)
        
        bfs_traversal = []
        
        while queue:
            current = queue.popleft()
            bfs_traversal.append(current)
            
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return bfs_traversal

def main():
    tree = Tree()
    try:
        n = int(input("Enter the number of edges in the tree: "))
        
        print("\nEnter the edges (format: 'node1 node2'):")
        for i in range(n-1):
            edge = input(f"Edge {i+1}: ").strip().split()
            if len(edge) != 2:
                print("Invalid input format. Please enter two nodes separated by space.")
                continue
            u, v = edge
            tree.add_edge(u, v)
        
        start_node = input("\nEnter the starting node for BFS: ").strip()
        
        result = tree.bfs(start_node)
        
        if isinstance(result, list):
            print("\nBFS Traversal:", " -> ".join(result))
        else:
            print("\nError:", result)
            
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()