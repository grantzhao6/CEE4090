import random

class GeneticAlgorithm:

    def __init__(self,population_size,num_genes):
        self.population = []
        self.fitness = []
        self.population_size = population_size
        self.genes = num_genes

    def generatePopulation(self):
        for i in range(self.population_size):
            
            new = []
            
            for j in range(self.genes):
                new.append(int(random.getrandbits(1)))
                
            self.population.append(new)
        
        return self.population
    
    def fitnessCalc(self):    
        for individual in self.population:
            fitness_count = 0
            for gene in individual:
                if gene == 1:
                     fitness_count += 1
                   
            self.fitness.append(round(fitness_count/self.genes, 2))
        
        return self.fitness