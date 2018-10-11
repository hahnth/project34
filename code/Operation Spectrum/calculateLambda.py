import numpy as np


def maxEig(A): # TODO Exceptions behandeln
    """Returns the largest eigenvalue of a symmetric matrix"""
    eigenVals = np.linalg.eigvalsh(A)
    maxEigenVal = np.abs(eigenVals[0])
    minEigenVal = np.abs(eigenVals[len(eigenVals) - 1])
    if (maxEigenVal > minEigenVal):
        return maxEigenVal
    else:
        return minEigenVal

