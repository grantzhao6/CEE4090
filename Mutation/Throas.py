import numpy as np

class ThroasMutation:
    def __init__(self):
        self.chromosome = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def mutate(self):
        if len(self.chromosome) < 3:
            raise ValueError("Chromosome length must be at least 3 for Throas mutation")

        mutated_chromosome = np.copy(self.chromosome)
        index = np.random.randint(0, 9)
        mutated_chromosome[index] = self.chromosome[index-1]
        mutated_chromosome[index+1] = self.chromosome[index]
        mutated_chromosome[index-1] = self.chromosome[index+1]

        return mutated_chromosome

# Example usage:
throas = ThroasMutation()
mutated_chromosome = throas.mutate()
print("Original chromosome:", throas.chromosome)
print("Mutated chromosome:", mutated_chromosome)