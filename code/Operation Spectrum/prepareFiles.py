import numpy as np

def fileToMatrix(path):
    A = np.array([])
    #Access file
    fileToModify = open(path, "r");
    #TODO: find \n
    #TODO: add row to array
    #TODO: removing whitespace neceessary?

    fileToModify.close()
    return A

def normalizeMatrix(A):
    #TODO modify all weights to 1
    return A


print(fileToMatrix(".\data\largeTree.txt")) #good test matrix