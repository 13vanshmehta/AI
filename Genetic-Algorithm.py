import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, population_size, chromosome_length, generations, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()
        
    def initialize_population(self):
        """Initialize a random population of binary chromosomes"""
        return [self.generate_random_chromosome() for _ in range(self.population_size)]
    
    def generate_random_chromosome(self):
        """Generate a random binary chromosome"""
        return [random.randint(0, 1) for _ in range(self.chromosome_length)]
    
    def fitness_function(self, chromosome):
        """
        Fitness function - counts the number of 1's in the chromosome
        This is a simple maximization problem (OneMax problem)
        """
        return sum(chromosome)
    
    def select_parents(self, fitnesses):
        """Select parents using tournament selection"""
        tournament_size = 3
        selected_parents = []
        
        for _ in range(2):  # Select 2 parents
            tournament_indices = random.sample(range(self.population_size), tournament_size)
            tournament_fitnesses = [fitnesses[i] for i in tournament_indices]
            winner_index = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
            selected_parents.append(self.population[winner_index])
            
        return selected_parents
    
    def crossover(self, parent1, parent2):
        """Perform single-point crossover between two parents"""
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.chromosome_length - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        else:
            return parent1.copy(), parent2.copy()
    
    def mutate(self, chromosome):
        """Perform bit-flip mutation on a chromosome"""
        for i in range(self.chromosome_length):
            if random.random() < self.mutation_rate:
                chromosome[i] = 1 - chromosome[i]  # Flip the bit
        return chromosome
    
    def run(self):
        """Run the genetic algorithm"""
        print("Starting Genetic Algorithm...")
        print(f"Initial Population: {self.population}")
        
        best_fitness_history = []
        avg_fitness_history = []
        
        for generation in range(self.generations):
            # Calculate fitness for each chromosome
            fitnesses = [self.fitness_function(chromosome) for chromosome in self.population]
            
            # Track statistics
            best_fitness = max(fitnesses)
            avg_fitness = sum(fitnesses) / self.population_size
            best_fitness_history.append(best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            # Print generation statistics
            print(f"\nGeneration {generation + 1}:")
            print(f"Best Fitness: {best_fitness}")
            print(f"Average Fitness: {avg_fitness:.2f}")
            
            # Create new population
            new_population = []
            
            # Elitism: keep the best chromosome
            elite_index = fitnesses.index(best_fitness)
            new_population.append(self.population[elite_index])
            
            # Create rest of the new population
            while len(new_population) < self.population_size:
                # Select parents
                parent1, parent2 = self.select_parents(fitnesses)
                
                # Crossover
                child1, child2 = self.crossover(parent1, parent2)
                
                # Mutation
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                
                # Add children to new population
                new_population.append(child1)
                if len(new_population) < self.population_size:
                    new_population.append(child2)
            
            # Replace old population with new population
            self.population = new_population
        
        # Final results
        final_fitnesses = [self.fitness_function(chromosome) for chromosome in self.population]
        best_index = final_fitnesses.index(max(final_fitnesses))
        best_chromosome = self.population[best_index]
        best_fitness = final_fitnesses[best_index]
        
        print("\nFinal Results:")
        print(f"Best Chromosome: {best_chromosome}")
        print(f"Best Fitness: {best_fitness}")
        
        # Print simple representation of fitness history
        print("\nFitness History:")
        print("Generation | Best Fitness | Avg Fitness")
        print("-" * 40)
        for i in range(self.generations):
            print(f"{i+1:^10} | {best_fitness_history[i]:^12} | {avg_fitness_history[i]:^11.2f}")
        
        return best_chromosome, best_fitness

def main():
    print("Genetic Algorithm - OneMax Problem")
    print("==================================")
    
    try:
        population_size = int(input("Enter population size: "))

        chromosome_length = int(input("Enter chromosome length: "))

        generations = int(input("Enter number of generations: "))

        mutation_rate = float(input("Enter mutation rate (0.0 to 1.0): " ))

        crossover_rate = float(input("Enter crossover rate (0.0 to 1.0): "))
        
        # Create and run genetic algorithm
        ga = GeneticAlgorithm(
            population_size=population_size,
            chromosome_length=chromosome_length,
            generations=generations,
            mutation_rate=mutation_rate,
            crossover_rate=crossover_rate
        )
        
        best_solution, best_fitness = ga.run()
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()