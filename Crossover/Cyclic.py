class CyclicCrossover:
    def __init__(self):
        self.parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
        self.child1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.child2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.not_present = []

    def crossover(self):
        cycle_start = 0
        cycle_number = 0
        while True:
            if cycle_number % 2 == 0:
                self.child1[cycle_start] = self.parent1[cycle_start]
                cycle_start = self.parent2.index(self.parent1[cycle_start])
            else:
                self.child2[cycle_start] = self.parent2[cycle_start]
                cycle_start = self.parent1.index(self.parent2[cycle_start])

            if cycle_start == 0:
                cycle_number += 1
                if cycle_number == 2:
                    break

        # Fill in the remaining positions for child 1 with elements from parent 2
        for i in range(len(self.child1)):
            if self.child1[i] == 0:
                self.child1[i] = self.parent2[i]

        # Fill in the remaining positions for child 2 with elements from parent 1
        for i in range(len(self.child2)):
            if self.child2[i] == 0:
                self.child2[i] = self.parent1[i]

        return self.child1, self.child2

crossover = CyclicCrossover()
offspring1, offspring2 = crossover.crossover()
print("Offspring 1:", offspring1)
print("Offspring 2:", offspring2)

crossover = CyclicCrossover()
offspring = crossover.crossover()
print(offspring)