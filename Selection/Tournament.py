import random

class TournamentSelection:
    def __init__(self):
        self.population = [8, 7, 6, 5, 4, 3, 2]
        self.selected = [0, 0, 0, 0, 0, 0, 0]
        self.tournament_size = 4
        self.tournament = [0] * self.tournament_size

    def select(self):
        self.population.sort()

        tournaments = 100
        for _ in range(tournaments):
            for i in range(self.tournament_size):
                self.tournament[i] = self.population[random.randint(0, len(self.population) - 1)]

            max_value = max(self.tournament)
            for i, value in enumerate(self.population):
                if value == max_value:
                    self.selected[i] += 1

        for i, value in enumerate(self.population):
            print(f"{value} was selected {self.selected[i]} times.")

Tournament = TournamentSelection()

Tournament.select()

