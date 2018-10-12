import numpy as np
import scipy as sp
import matplotlib.pyplot as plot
import networkx as ntx

from plotGraph import plotFromMatrix
from fetchData import fileToMatrix, normalizeMatrix, fileToEdgelist, edgelistToMatrix
from calculateLambda import obtainMaxEig, maxEig


print("Largest eigenvalues:")

A = fileToMatrix(".\data\simpleGraph.txt", ',', ',')
print("simpleGraph")
obtainMaxEig(A, True, 2)

B = fileToMatrix(".\data\largeTree.txt", ',', ',')
print("largeTree")
obtainMaxEig(B, True, 2)

C = fileToMatrix(".\data\cities.txt", ',', ',')
print("cities")
obtainMaxEig(C, True, 2)

D = fileToMatrix(".\data\windsurfers.txt", '\n', ' ')
print("windsurfers")
obtainMaxEig(D, True, 2)

E = fileToMatrix(".\data\guineaTribe.txt", '\n', ' ')
print("guineaTribe")
obtainMaxEig(E, True, 2)

plotFromMatrix(B)

#Warning: Large file, takes up to 3 minutes
edges = fileToEdgelist(".\data\edges.csv", ',')
print(maxEig(edgelistToMatrix(edges)))
