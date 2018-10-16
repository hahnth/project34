from plotGraph import plotFromMatrix, plotFromGraph
from fetchData import importMatrixFile, normalizeMatrix, importEdgeListFile
from calculateLambda import obtainMaxEig


print("Largest eigenvalues:")

A = importMatrixFile(".\data\simpleGraph.txt", ',', ',')
print("simpleGraph")
obtainMaxEig(A, True, 2)

B = importMatrixFile(".\data\largeTree.txt", ',', ',')
print("largeTree")
obtainMaxEig(B, True, 2)

C = importMatrixFile(".\data\cities.txt", ',', ',')
print("cities")
obtainMaxEig(C, True, 2)

D = importMatrixFile(".\data\windsurfers.txt", '\n', ' ')
print("windsurfers")
obtainMaxEig(D, True, 2)

E = importMatrixFile(".\data\guineaTribe.txt", '\n', ' ')
print("guineaTribe")
obtainMaxEig(E, True, 2)

plotFromGraph(B)

#Warning: Large file, takes up to 2 minutes
#F = importEdgeListFile(".\data\hyves\edges.csv", ',')
print("hyves")
#obtainMaxEig(F, True, 3)
