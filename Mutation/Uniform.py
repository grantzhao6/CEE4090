import numpy as np

class UniformMutation:
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def mutate(self, chromosome):
        mutated_chromosome = np.copy(chromosome)
        for i in range(len(chromosome)):
            if np.random.rand() < self.mutation_rate:
                mutated_chromosome[i] = np.random.randint(1, 10)  # Assuming genes are integers from 1 to 9
        return mutated_chromosome

# Example usage:
mutation_rate = 0.2  # Mutation rate
chromosome = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
mutator = UniformMutation(mutation_rate)
mutated_chromosome = mutator.mutate(chromosome)
print("Original chromosome:", chromosome)
print("Mutated chromosome:", mutated_chromosome)