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


def normalizeMatrix(A):
    # Alle Werte ungleich 0 auf 1 setzen
    return A
