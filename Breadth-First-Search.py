from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # Default dictionary to store the graph
        self.graph = defaultdict(list)
    
    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # Function to perform BFS traversal from a given source vertex
    def bfs(self, start_vertex):
        # Mark all vertices as not visited
        visited = set()
        
        # Create a queue for BFS
        queue = deque()
        
        # Mark the source node as visited and enqueue it
        visited.add(start_vertex)
        queue.append(start_vertex)
        
        while queue:
            # Dequeue a vertex from queue and print it
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it
            # visited and enqueue it
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Main function
if __name__ == "__main__":
    g = Graph()

    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter edges (format: source destination):")
    for i in range(num_edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    start = int(input("Enter the starting vertex for BFS: "))
    
    print(f"Breadth First Traversal (starting from vertex {start}):")
    g.bfs(start)