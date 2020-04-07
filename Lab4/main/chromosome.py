from random import randint, seed


def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm


# permutation-based representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam  # problParam has to store the number of nodes/cities
        self.__repres = generateARandomPermutation(self.__problParam['noNodes'])
        self.__matrix = problParam["mat"]
        self.__cost = self.get_total_cost()
        self.__fitness = 1 / self.__cost

    def get_repres(self):
        return self.__repres

    def get_fitness(self):
        return 1 / self.get_total_cost()

    def get_total_cost(self):
        cost = 0
        for index in range(len(self.__repres)):
            cost += self.__matrix[self.__repres[index]][self.__repres[index - 1]]
        return cost

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if el not in newrepres:
                if len(newrepres) < self.__problParam['noNodes'] - pos1:
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # insert mutation
        pos1 = randint(0, self.__problParam['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['noNodes'] - 1)
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.get_fitness()) + " and cost:" + str(self.get_total_cost())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __hash__(self):
        return hash(self.__repr__())