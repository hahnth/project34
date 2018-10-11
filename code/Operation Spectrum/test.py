import numpy as np
import matplotlib.pyplot as plot

from plotGraph import plotFromMatrix

from fetchData import fileToMatrix, normalizeMatrix
from calculateLambda import maxEig

print("Largest eigenvalues:")

A = fileToMatrix(".\data\simpleGraph.txt", ',', ',')
print("simpleGraph: " + str(np.round(maxEig(A),2)))

B = fileToMatrix(".\data\largeTree.txt", ',', ',')
print("largeTree: " + str(np.round(maxEig(normalizeMatrix(B,0)),2)))

C = fileToMatrix(".\data\cities.txt", ',', ',')
print("cities: " + str(np.round(maxEig(normalizeMatrix(C,0)),2)))

D = fileToMatrix(".\data\windsurfers.txt", '\n', ' ')
print("windsurfers: " + str(np.round(maxEig(normalizeMatrix(D,0.5)),2))) # arbitrary threshold

E = fileToMatrix(".\data\guineaTribe.txt", '\n', ' ')
print("guineaTribe: " + str(np.round(maxEig(E),2)))

plotFromMatrix(E)
plot.show()