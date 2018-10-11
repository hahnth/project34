import numpy as np

from prepareFiles import fileToMatrix


def maxEig(A): # TODO Exceptions behandeln
    """Returns the largest eigenvalue of a symmetric matrix"""
    eigenVals = np.linalg.eigvalsh(A)
    maxEigenVal = np.abs(eigenVals[0])
    minEigenVal = np.abs(eigenVals[len(eigenVals) - 1])
    if (maxEigenVal > minEigenVal):
        return maxEigenVal
    else:
        return minEigenVal


print("Largest Eigenvalues:")

A = fileToMatrix(".\data\simpleGraph.txt", ',', ',')
print("simpleGraph: " + str(np.round(maxEig(A),2)))

B = fileToMatrix(".\data\largeTree.txt", ',', ',')
print("largeTree: " + str(np.round(maxEig(B),2)))

C = fileToMatrix(".\data\cities.txt", ',', ',')
print("cities: " + str(np.round(maxEig(C),2)))

D = fileToMatrix(".\data\windsurfers.txt", '\n', ' ')

E = fileToMatrix(".\data\guineaTribe.txt", '\n', ' ')
print("guineaTribe: " + str(np.round(maxEig(E),2)))