import warnings
import matplotlib.cbook
import matplotlib.pyplot as plot

from plotGraph import plotFromGraph
from fetchData import importMatrixFile, importEdgeListFile, normalizeGraph
from calculateLambda import obtainMaxEig, removeCriticalNode

# suppresses warning while creating plot
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

# initializes the plot counter
plotFromGraph.counter = 1

print("Largest eigenvalues:")

A = importMatrixFile(".\data\simpleGraph.txt", ',', ',')
print("simpleGraph")
obtainMaxEig(A, True, 2)

B = importMatrixFile(".\data\largeTree.txt", ',', ',')
B = normalizeGraph(B, 0.5)
print("largeTree")
obtainMaxEig(B, True, 2)

C = importMatrixFile(".\data\cities.txt", ',', ',')
C = normalizeGraph(C, 0.5)
print("cities")
obtainMaxEig(C, True, 2)

D = importMatrixFile(".\data\windsurfers.txt", '\n', ' ')
D = normalizeGraph(D, 0.35)
print("windsurfers")
obtainMaxEig(D, True, 2)

E = importMatrixFile(".\data\guineaTribe.txt", '\n', ' ')
E = normalizeGraph(E, 0.5)
print("guinea tribe")
obtainMaxEig(E, True, 2)

G = importEdgeListFile(".\data\\asgraph\\asgraph.txt", ':')
print('Oregon-AS graph')
# Warning: Can take up to 10 min to plot the graphs and you don't see very much
# plotFromGraph(G)
obtainMaxEig(G, True, 3)

# TODO: s.removeCriticalNode
# G1 = removeCriticalNode(G)
# print('Oregon-AS graph vaccinated')
# obtainMaxEig(G1, True, 3)

F = importEdgeListFile('.\data\\terrorist.txt', '\t')
print("terrorist")
obtainMaxEig(F, True, 2)
plotFromGraph(F)

X = removeCriticalNode(F)
print("terrorist vaccinated")
obtainMaxEig(X, True, 2)
plotFromGraph(X)

X2 = removeCriticalNode(X)
print("terrorist twice vaccinated")
obtainMaxEig(X2, True, 2)
plotFromGraph(X2)

# Warning: Large file, takes up to 2 minutes
# G = importEdgeListFile(".\data\hyves\edges.csv", ',')
# print("hyves")
# obtainMaxEig(G, True, 3)

# necessary to avoid blocking of the script execution, plots are displayed when script is done
plot.show()
