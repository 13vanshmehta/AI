import random
import math

def calculate_total_distance(tour, distances):
    """
    Calculate the total distance of a tour
    
    Parameters:
    tour: List of cities in the order they are visited
    distances: 2D matrix of distances between cities
    
    Returns:
    total_distance: Total distance of the tour
    """
    total_distance = 0
    num_cities = len(tour)
    
    for i in range(num_cities):
        from_city = tour[i]
        to_city = tour[(i + 1) % num_cities]  # Return to starting city
        total_distance += distances[from_city][to_city]
    
    return total_distance

def generate_neighbor(current_tour):
    """
    Generate a neighbor solution by swapping two cities
    
    Parameters:
    current_tour: Current tour
    
    Returns:
    neighbor_tour: A new tour with two cities swapped
    """
    neighbor_tour = current_tour.copy()
    num_cities = len(neighbor_tour)
    
    # Select two random positions to swap
    i, j = random.sample(range(num_cities), 2)
    
    # Swap the cities
    neighbor_tour[i], neighbor_tour[j] = neighbor_tour[j], neighbor_tour[i]
    
    return neighbor_tour

def hill_climbing_tsp(distances, max_iterations):
    """
    Perform hill climbing algorithm to find a solution to the TSP
    
    Parameters:
    distances: 2D matrix of distances between cities
    max_iterations: Maximum number of iterations
    
    Returns:
    best_tour: The best tour found
    best_distance: The distance of the best tour
    iterations: Number of iterations performed
    """
    num_cities = len(distances)
    
    # Generate a random initial tour
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    
    current_distance = calculate_total_distance(current_tour, distances)
    
    # For tracking progress
    iterations = 0
    progress = []
    
    print(f"Starting tour: {current_tour}")
    print(f"Starting distance: {current_distance:.2f}")
    
    for i in range(max_iterations):
        iterations += 1
        
        # Generate a neighbor
        neighbor_tour = generate_neighbor(current_tour)
        neighbor_distance = calculate_total_distance(neighbor_tour, distances)
        
        # If the neighbor is better, move to it
        if neighbor_distance < current_distance:
            current_tour = neighbor_tour
            current_distance = neighbor_distance
            print(f"Iteration {iterations}: Improved distance to {current_distance:.2f}")
        
        progress.append((current_tour.copy(), current_distance))
        
        # Optional: Early stopping if no improvement for a while
        if iterations > 100 and progress[-100][1] == current_distance:
            print(f"No improvement for 100 iterations. Stopping early.")
            break
    
    return current_tour, current_distance, iterations, progress

def main():
    print("Hill Climbing Algorithm for Traveling Salesman Problem")
    print("=====================================================")
    
    try:
        # Get user input
        num_cities = int(input("Enter the number of cities: "))
        
        # Generate random distances between cities
        print("\nGenerating random distances between cities...")
        distances = []
        for i in range(num_cities):
            row = []
            for j in range(num_cities):
                if i == j:
                    row.append(0)  # Distance to self is 0
                else:
                    row.append(random.randint(1, 100))  # Random distance
            distances.append(row)
        
        # Display distance matrix
        print("\nDistance Matrix:")
        for i in range(num_cities):
            for j in range(num_cities):
                print(f"{distances[i][j]:4}", end=" ")
            print()
        
        max_iterations = int(input("\nEnter the maximum number of iterations: "))
        
        # Run hill climbing
        best_tour, best_distance, iterations, progress = hill_climbing_tsp(
            distances, max_iterations
        )
        
        # Print results
        print("\nResults:")
        print(f"Best tour found: {best_tour}")
        print(f"Best distance: {best_distance:.2f}")
        print(f"Number of iterations: {iterations}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()