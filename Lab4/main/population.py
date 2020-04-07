import ast
from random import random

from main.chromosome import Chromosome


class Population:
    def getPopulation(self, size, network):
        return [Chromosome(network) for i in range(size)]

    def bestSolution(self, population, network):
        pop = list(population)
        best = pop[0]
        for community in pop:
            if community.get_total_cost() < best.get_total_cost():
                best = community
        return best

    def getProbabilityList(self, fitness):
        totalFit = float(sum(fitness))
        relativeFitness = [f / totalFit for f in fitness]
        probabilities = [sum(relativeFitness[:i + 1]) for i in range(len(relativeFitness))]
        return probabilities

    def selection(self, generation):
        generation = list(generation)
        probabilities = self.getProbabilityList([individual.get_fitness() for individual in generation])

        r = random()
        for (i, individual) in enumerate(generation):
            if r <= probabilities[i]:
                return individual

    def findPath(self, size, iterations, network):
        population = self.getPopulation(size, network)
        best = self.bestSolution(population, network)
        index = 0
        while index < iterations:
            newPopulation = set()
            newPopulation.add(self.bestSolution(population, network))

            while newPopulation.__len__() < population.__len__():
                first = self.selection(population)
                second = self.selection(population)

                first = first.crossover(second)
                first.mutation()

                newPopulation.add(first)

            # we obtained a new generation
            index += 1
            population = newPopulation
            best = self.bestSolution(population, network)
            print(best)
        return best