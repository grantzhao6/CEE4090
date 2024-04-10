#Problems: collapse of population diversity early on

import random

class StochasticUniversalSampling:
    def __init__(self):
        self.population = [8, 7, 6, 5, 4, 3, 2]
        self.selected = [0, 0, 0, 0, 0, 0, 0]
        self.probabilities = [0] * len(self.population)
        self.random = random.Random()

    def select(self):
        total = sum(self.population)
        self.probabilities = [p / total for p in self.population]

        samples = 10000
        f_of_n = 1.0 / samples
        total_prob = 0.0
        selected_value = self.random.random() * f_of_n

        count = 0
        total_samples = 0
        flag = True

        while flag:
            if selected_value <= total_prob:
                self.selected[count] += 1
                selected_value += f_of_n
                total_samples += 1
            else:
                total_prob += self.probabilities[count]
                if count != 6:
                    count += 1

            if total_samples == samples:
                flag = False

        for i, value in enumerate(self.population):
            print(f"{value} was selected {self.selected[i]} times.")

sus = StochasticUniversalSampling()

sus.select()