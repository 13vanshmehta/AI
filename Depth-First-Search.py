from collections import defaultdict

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # Function to perform DFS traversal from a given source vertex
    def dfs_util(self, vertex, visited):
        # Mark the current node as visited and print it
        visited.add(vertex)
        print(vertex, end=" ")
        
        # Recur for all the adjacent vertices
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
    
    # Function to perform DFS traversal
    def dfs(self, start_vertex):
        # Mark all vertices as not visited
        visited = set()
        
        # Call the recursive helper function
        self.dfs_util(start_vertex, visited)

# Main function
if __name__ == "__main__":
    g = Graph()

    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter edges (format: source destination):")
    for i in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start = int(input("Enter the starting vertex for DFS: "))
    
    print(f"Depth First Traversal (starting from vertex {start}): ")
    g.dfs(start)