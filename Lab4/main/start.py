import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings

import os

from main.population import Population
from main.repository import Repository


def run():
    while True:
        repo = Repository()
        population = Population()
        populationSize = int(input('Population size: '))
        numberOfIterations = int(input('Number of iterations: '))

        crtDir = os.getcwd()
        filePath = os.path.join(crtDir, 'net.in')

        cities, network = repo.readNet(filePath)

        warnings.simplefilter('ignore')

        bestSolution = population.findPath(populationSize, numberOfIterations, network)
        print('\nCea mai buna este ' + str(bestSolution))

        A = np.matrix(network["mat"])
        G = nx.from_numpy_matrix(A)
        pos = nx.spring_layout(G)  # compute graph layout
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlGn, node_color='#1f78b4')
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show(G)

run()
