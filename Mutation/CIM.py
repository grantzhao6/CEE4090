import numpy as np

class CenterInversionMutation:
    def __init__(self):
        self.chromosome = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def mutate(self):
        center_index = len(self.chromosome) // 2

        part1 = self.chromosome[:center_index]
        part2 = self.chromosome[center_index:]

        # Reverse each part
        part1_reversed = np.flip(part1)
        part2_reversed = np.flip(part2)

        mutated_chromosome = np.concatenate((part1_reversed, part2_reversed))

        return mutated_chromosome

cim = CenterInversionMutation()
mutated_chromosome = cim.mutate()
print("Original chromosome:", cim.chromosome)
print("Mutated chromosome:", mutated_chromosome)