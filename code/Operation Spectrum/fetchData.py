import numpy as np
import networkx as ntx

# TODO typing?

def importMatrixFile(path, lineSeparator, columnSeparator): # TODO: Exceptions behandeln(float(i))
    """reads a matrix from a file into a nbarray an returns the according graph
       file may not be empty
       each row has to contain the same number of elements
       lines in the file are separated by lineSeparator
       columns are separated by columnSeparator"""

    sourceFile = open(path, "r")
    # first line to create a matrix TODO eleganterer Weg?
    line = sourceFile.readline()
    # Excludes special characters from imported string (typical cases considered)
    if line[len(line) - 1] == '\n':
        line = line[:len(line) - 1]
    if line[len(line) - 1] == ' ':
        line = line[:len(line) - 1]
    if line[len(line) - 1] == lineSeparator:
        line = line[:len(line) - 1]
    if line[len(line) - 1] == ' ':
        line = line[:len(line) - 1]
    lineElements = line.split(columnSeparator)
    # Float array to deal with weighted graphs
    lineElements = [float(i) for i in lineElements]
    A = np.array(lineElements, dtype=float)

    while True:
        line = sourceFile.readline()
        if line == "" or line == "\n":
            break
        if line[len(line)-1] == '\n':
            line = line[:len(line) -1]
        if line[len(line) - 1] == ' ':
            line = line[:len(line) - 1]
        if line[len(line) - 1] == lineSeparator:
            line = line[:len(line) - 1]
        if line[len(line) - 1] == ' ':
            line = line[:len(line) - 1]
        lineElements = line.split(columnSeparator)
        lineElements = [float(i) for i in lineElements]
        # Adds row to existing matrix, assuming same number of elements
        A = np.vstack([A, lineElements])

    sourceFile.close()
    # Converts matrix into networkX graph object
    return ntx.from_numpy_array(A)


def importEdgeListFile(path, elementSeparator): #TODO Exceptions behandeln (int(i))
    """reads a graph from a file containing all edges
       inside a line the two nodes connected by the edge a separated by the elementSeparator"""
    sourceFile = open(path, "r")
    edgelist = []
    while True:
        line = sourceFile.readline()
        if line == '' or line == '\n':
            break
        # Edgelist expects integer values (discrete values of nodes)
        edgelist.append(tuple([int(i) for i in line.split(elementSeparator)]))
    sourceFile.close()
    #Converts edgelist to networkx graph object
    return ntx.from_edgelist(edgelist)


def normalizeMatrix(A, threshold): #TODO: auf graph portieren, funktioniert dieser Ansatz mit sparse matrizen?
    """Sets all values of a matrix with an absolute value greater than the threshold to 1 and all others to 0"""
    num = len(A)
    for i in range(0, num):
        for j in range(0, num):
            if np.abs(A[i, j]) > threshold:
                A[i, j] = 1
            else:
                A[i, j] = 0
    return A
