import random
import math

def objective_function(x):
    """
    Objective function to maximize.
    This is a simple function with a maximum at x = 0.
    You can replace this with any other function.
    """
    return -x**2  # Negative because we're maximizing

def generate_neighbor(current_solution, step_size):
    """Generate a random neighbor within step_size of current solution"""
    return current_solution + random.uniform(-step_size, step_size)

def hill_climbing(max_iterations, step_size, initial_solution):
    """
    Perform hill climbing algorithm to find maximum of objective function
    
    Parameters:
    max_iterations: Maximum number of iterations
    step_size: Size of step to take when generating neighbors
    initial_solution: Starting point for the algorithm
    
    Returns:
    best_solution: The solution with highest value found
    best_value: The value of the best solution
    iterations: Number of iterations performed
    """
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    
    # For tracking progress
    iterations = 0
    progress = []
    
    print(f"Starting at x = {current_solution:.4f}, value = {current_value:.4f}")
    
    for i in range(max_iterations):
        iterations += 1
        
        # Generate a neighbor
        neighbor = generate_neighbor(current_solution, step_size)
        neighbor_value = objective_function(neighbor)
        
        # If the neighbor is better, move to it
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
            print(f"Iteration {iterations}: Moved to x = {current_solution:.4f}, value = {current_value:.4f}")
        else:
            print(f"Iteration {iterations}: Stayed at x = {current_solution:.4f}, value = {current_value:.4f}")
        
        progress.append((current_solution, current_value))
        
        # Optional: Reduce step size over time
        step_size *= 0.95
    
    return current_solution, current_value, iterations, progress

def main():
    print("Hill Climbing Algorithm")
    print("======================")
    
    # Get user input
    try:
        max_iterations = int(input("Enter the maximum number of iterations:"))

        step_size = float(input("Enter the initial step size:"))

        initial_solution = float(input("Enter the initial solution (starting x value):"))
        
        # Run hill climbing
        best_solution, best_value, iterations, progress = hill_climbing(
            max_iterations, step_size, initial_solution
        )
        
        # Print results
        print("\nResults:")
        print(f"Best solution found: x = {best_solution:.6f}")
        print(f"Best value: {best_value:.6f}")
        print(f"Number of iterations: {iterations}")
        
        # Print simple representation of progress
        print("\nProgress Visualization:")
        print("x values: ", end="")
        for i in range(0, iterations, max(1, iterations//10)):
            print(f"{progress[i][0]:.2f}", end=" ")
        print()
        
        print("values: ", end="")
        for i in range(0, iterations, max(1, iterations//10)):
            print(f"{progress[i][1]:.2f}", end=" ")
        print()
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()