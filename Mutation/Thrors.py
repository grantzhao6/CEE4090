import numpy as np

class ThrorsMutation:
    def __init__(self):
        self.chromosome = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def mutate(self):
        if len(self.chromosome) < 3:
            raise ValueError("Chromosome length must be at least 3 for Throas mutation")

        positions = np.random.choice(len(self.chromosome), size=3, replace=False)

        mutated_chromosome = np.copy(self.chromosome)
        mutated_chromosome[positions[0]] = self.chromosome[-1]
        mutated_chromosome[positions[1]] = self.chromosome[0]
        mutated_chromosome[positions[2]] = self.chromosome[1]

        return mutated_chromosome

# Example usage:
thrors = ThrorsMutation()
mutated_chromosome = thrors.mutate()
print("Original chromosome:", thrors.chromosome)
print("Mutated chromosome:", mutated_chromosome)