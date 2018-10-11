import numpy as np

def fileToMatrix(path, lineSeperator, columnSeperator):
    """reads a matrix from a file into a nbarray
       lines in the file are seperated by lineSeperator
       columns are seperated by columnSeperator"""

    sourceFile = open(path, "r")
    line = sourceFile.readline()

    # TODO: Dokumentation

    # first line (File may not be empty!)
    if (line[len(line) - 1] == '\n'):
        line = line[:len(line) - 1]
    if (line[len(line) - 1] == ' ' ):
        line = line[:len(line) - 1]
    if (line[len(line) - 1] == lineSeperator):
        line = line[:len(line) - 1]
    if (line[len(line) - 1] == ' ' ):
        line = line[:len(line) - 1]
    lineElements = line.split(columnSeperator)
    lineElements = [float(i) for i in lineElements]
    A = np.array(lineElements, dtype=float)

    while True:
        line = sourceFile.readline()
        if(line == ""):
            break
        if (line[len(line)-1] == '\n'):
            line = line[:len(line) -1]
        if (line[len(line) - 1] == ' '):
            line = line[:len(line) - 1]
        if (line[len(line) - 1] == lineSeperator):
            line = line[:len(line) - 1]
        if (line[len(line) - 1] == ' '):
            line = line[:len(line) - 1]
        lineElements = line.split(columnSeperator)
        lineElements = [float(i) for i in lineElements]
        A = np.vstack([A, lineElements])
    sourceFile.close()
    return A


def normalizeMatrix(A, threshold):
    num = len(A)
    for i in range(0,(num)):
        for j in range(0,(num)):
            if(np.abs(A[i,j]) > threshold):
                A[i,j] = 1
            else:
                A[i,j] = 0
    return A
