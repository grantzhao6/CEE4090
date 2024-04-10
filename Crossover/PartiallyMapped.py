import numpy as np

class PartiallyMappedCrossover:
    def __init__(self):
        self.parent1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.parent2 = np.array([9, 3, 7, 8, 2, 6, 5, 1, 4])
        self.child = np.zeros(9, dtype=int)
        self.not_present = []

    def crossover(self):
        lower_bound = 3
        upper_bound = 7

        self.child[lower_bound:upper_bound] = self.parent1[lower_bound:upper_bound]

        for i in range(lower_bound, upper_bound):
            if self.parent2[i] not in self.child[lower_bound:upper_bound]:
                self.not_present.append(i)

        for i in self.not_present:
            current_value = self.parent1[i]
            stored_value = self.parent2[i]
            flag = True

            while flag:
                index = np.where(self.parent2 == current_value)[0][0]
                if self.child[index] == 0:
                    self.child[index] = stored_value
                    flag = False
                else:
                    current_value = self.parent1[index]

            print(self.child)

        for i in range(len(self.parent2)):
            if self.child[i] == 0:
                self.child[i] = self.parent2[i]

        print(self.child)

Partial = PartiallyMappedCrossover()

Partial.crossover()