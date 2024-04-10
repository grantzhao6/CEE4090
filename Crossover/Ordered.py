import copy

class OrderedCrossover:
    def __init__(self):
        self.parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
        self.child = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.not_present = []

    def crossover(self):
        print(self.parent1)
        print(self.parent2)

        lower_bound = 3
        upper_bound = 7

        self.child[lower_bound:upper_bound] = self.parent1[lower_bound:upper_bound]

        for i in range(upper_bound, len(self.parent2)):
            if all(self.parent2[i] != self.child[j] for j in range(lower_bound, upper_bound)):
                self.not_present.append(self.parent2[i])

        for i in range(0, upper_bound):
            if all(self.parent2[i] != self.child[j] for j in range(lower_bound, upper_bound)):
                self.not_present.append(self.parent2[i])

        print(self.not_present)

        count = 0
        for i in range(upper_bound, len(self.child)):
            self.child[i] = self.not_present[count]
            print(self.child)
            count += 1

        for i in range(0, lower_bound):
            self.child[i] = self.not_present[count]
            print(self.child)
            count += 1

Ordered = OrderedCrossover()

Ordered.crossover()