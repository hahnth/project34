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

plotFromGraph(C)

D = importMatrixFile(".\data\windsurfers.txt", '\n', ' ')
print("windsurfers")
obtainMaxEig(D, True, 2)

E = importMatrixFile(".\data\guineaTribe.txt", '\n', ' ')
print("guineaTribe")
obtainMaxEig(E, True, 2)

#F = importEdgeListFile('.\data\\terrorist.txt', '\t')
#print("terrorist")
#obtainMaxEig(F, True, 2)

G = importEdgeListFile(".\data\\asgraph\\asgraph.txt", ':')
print('Oregon-AS graph')
#Warning: Can take up to 10 min to plot the graphs and you don't see very much
#plotFromGraph(G)
#plotFromGraph(G)
obtainMaxEig(G, True, 3)


#Warning: Large file, takes up to 2 minutes
#H = importEdgeListFile(".\data\hyves\edges.csv", ',')
#print("hyves")
#obtainMaxEig(H, True, 3)
