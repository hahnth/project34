import numpy as np
import networkx as ntx

def fileToMatrix(path, lineSeparator, columnSeparator): # TODO: Exceptions (float(i))
    """reads a matrix from a file into a nbarray
       lines in the file are separated by lineSeparator
       columns are separated by columnSeparator"""

    sourceFile = open(path, "r")
    line = sourceFile.readline()

    # TODO: Kommentare, Spaghetti-Code?

    # first line (File may not be empty!)
    if (line[len(line) - 1] == '\n'):
        line = line[:len(line) - 1]
    if (line[len(line) - 1] == ' ' ):
        line = line[:len(line) - 1]
    if (line[len(line) - 1] == lineSeparator):
        line = line[:len(line) - 1]
    if (line[len(line) - 1] == ' ' ):
        line = line[:len(line) - 1]
    lineElements = line.split(columnSeparator)
    lineElements = [float(i) for i in lineElements]
    A = np.array(lineElements, dtype=float)

    while True:
        line = sourceFile.readline()
        if line == "" or line == "\n":
            break
        if (line[len(line)-1] == '\n'):
            line = line[:len(line) -1]
        if (line[len(line) - 1] == ' '):
            line = line[:len(line) - 1]
        if (line[len(line) - 1] == lineSeparator):
            line = line[:len(line) - 1]
        if (line[len(line) - 1] == ' '):
            line = line[:len(line) - 1]
        lineElements = line.split(columnSeparator)
        lineElements = [float(i) for i in lineElements]
        A = np.vstack([A, lineElements])
    sourceFile.close()
    return A


def fileToEdgelist(path, elementSeparator): #TODO Exceptions (int(i))
    """"""
    sourceFile = open(path, "r")
    edgelist = []
    while True:
        line = sourceFile.readline()
        if line == '' or line == '\n':
            break
        edgelist.append(tuple([int(i) for i in line.split(elementSeparator)]))
    sourceFile.close()
    return edgelist


def normalizeMatrix(A, threshold):
    """Sets all values of a matrix with an absolute value greater than the threshold to 1 and all others to 0"""
    num = len(A)
    for i in range(0,(num)):
        for j in range(0,(num)):
            if np.abs(A[i,j]) > threshold:
                A[i,j] = 1
            else:
                A[i,j] = 0
    return A

def edgelistToMatrix(edgelist):
    """Returns the adjacency matrix of the graph given by the edgelist"""
    graph = ntx.from_edgelist(edgelist)
    return ntx.adjacency_matrix(graph)
