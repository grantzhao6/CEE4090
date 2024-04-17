import numpy as np

class PartiallyMappedCrossover:
    def __init__(self):
        self.parent1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.parent2 = np.array([9, 3, 7, 8, 2, 6, 5, 1, 4])
        self.child1 = np.zeros(9, dtype=int)
        self.child2 = np.zeros(9, dtype=int)
        self.not_present = []

    def crossover(self):
        lower_bound = 3
        upper_bound = 7

        child1 = np.copy(self.child1)
        child2 = np.copy(self.child2)

        child1[lower_bound:upper_bound] = self.parent1[lower_bound:upper_bound]
        child2[lower_bound:upper_bound] = self.parent2[lower_bound:upper_bound]

        for i in range(lower_bound, upper_bound):
            if self.parent2[i] not in child1[lower_bound:upper_bound]:
                self.not_present.append(i)

        for i in self.not_present:
            current_value = self.parent1[i]
            stored_value = self.parent2[i]
            flag = True

            while flag:
                index = np.where(self.parent2 == current_value)[0][0]
                if child1[index] == 0:
                    child1[index] = stored_value
                    flag = False
                else:
                    current_value = self.parent1[index]

        for i in range(len(self.parent2)):
            if child1[i] == 0:
                child1[i] = self.parent2[i]

        self.not_present = []

        for i in range(lower_bound, upper_bound):
            if self.parent1[i] not in child2[lower_bound:upper_bound]:
                self.not_present.append(i)

        for i in self.not_present:
            current_value = self.parent2[i]
            stored_value = self.parent1[i]
            flag = True

            while flag:
                index = np.where(self.parent1 == current_value)[0][0]
                if child2[index] == 0:
                    child2[index] = stored_value
                    flag = False
                else:
                    current_value = self.parent2[index]

        for i in range(len(self.parent1)):
            if child2[i] == 0:
                child2[i] = self.parent1[i]

        return child1, child2

partially_mapped = PartiallyMappedCrossover()
child1, child2 = partially_mapped.crossover()
print("Child 1:", child1)
print("Child 2:", child2)