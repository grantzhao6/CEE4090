import copy

class OrderedCrossover:
    def __init__(self):
        self.parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
        self.child1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.child2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.not_present = []

    def crossover(self):
        lower_bound = 3
        upper_bound = 7

        child1 = copy.deepcopy(self.child1)
        child2 = copy.deepcopy(self.child2)

        child1[lower_bound:upper_bound] = self.parent1[lower_bound:upper_bound]
        child2[lower_bound:upper_bound] = self.parent2[lower_bound:upper_bound]

        for i in range(upper_bound, len(self.parent2)):
            if all(self.parent2[i] != child1[j] for j in range(lower_bound, upper_bound)):
                self.not_present.append(self.parent2[i])

        for i in range(0, upper_bound):
            if all(self.parent2[i] != child1[j] for j in range(lower_bound, upper_bound)):
                self.not_present.append(self.parent2[i])

        count = 0
        for i in range(upper_bound, len(child1)):
            child1[i] = self.not_present[count]
            count += 1

        for i in range(0, lower_bound):
            child1[i] = self.not_present[count]
            count += 1

        self.not_present = []

        for i in range(upper_bound, len(self.parent1)):
            if all(self.parent1[i] != child2[j] for j in range(lower_bound, upper_bound)):
                self.not_present.append(self.parent1[i])

        for i in range(0, upper_bound):
            if all(self.parent1[i] != child2[j] for j in range(lower_bound, upper_bound)):
                self.not_present.append(self.parent1[i])

        count = 0
        for i in range(upper_bound, len(child2)):
            child2[i] = self.not_present[count]
            count += 1

        for i in range(0, lower_bound):
            child2[i] = self.not_present[count]
            count += 1

        return child1, child2

ordered = OrderedCrossover()
child1, child2 = ordered.crossover()
print("Child 1:", child1)
print("Child 2:", child2)