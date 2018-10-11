import numpy as np

def maxEig(A): #TODO Exceptions?
    """Returns the largest eigenvalue of a symmetric matrix"""
    eigenVals = np.linalg.eigvalsh(A)
    maxEigenVal = np.abs(eigenVals[0])
    minEigenVal = np.abs(eigenVals[len(eigenVals) - 1])
    if (maxEigenVal > minEigenVal):
        return maxEigenVal
    else:
        return minEigenVal

#Definition of input matrix
A = np.array([[0,0,1,0,1],
              [0,0,1,1,0],
              [1,1,0,1,1],
              [0,1,1,0,0],
              [1,0,1,0,0]])


#TODO Assertion symmetric?

print("Matrix:")
print(A)
print("")
print("lamda_1 = " + str(np.round(maxEig(A))))

