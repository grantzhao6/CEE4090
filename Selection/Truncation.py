import numpy as np

class TruncationSelection:
    def __init__(self):
        self.population = np.array([8, 7, 6, 5, 4, 3, 2])
        self.selected = np.zeros_like(self.population)

    def select(self):
        percent = 0.5
        self.population.sort()

        percentile = int(np.round(percent * len(self.population)))
        starting = len(self.population) - percentile

        for i in range(len(self.population)):
            if i >= starting:
                self.selected[i] += 1

        for i, (value, count) in enumerate(zip(self.population, self.selected)):
            print(f"{value} was selected {count} times.")

Truncation = TruncationSelection()

Truncation.select()

