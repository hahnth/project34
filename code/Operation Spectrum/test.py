import networkx as ntx
import matplotlib.cbook
import matplotlib.pyplot as plot
import warnings

#suppresses warning while creating plot
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

from plotGraph import plotFromGraph
from fetchData import importMatrixFile, normalizeMatrix, importEdgeListFile, normalizeGraph
from calculateLambda import obtainMaxEig, removeCriticalNode, obtainNVM

#initializes the plot counter
plotFromGraph.counter = 1

print("Largest eigenvalues:")

A = importMatrixFile(".\data\simpleGraph.txt", ',', ',')
A = normalizeGraph(A, 0.5)
print("simpleGraph")
obtainMaxEig(A, True, 2)
obtainNVM(A, True, 4)

B = importMatrixFile(".\data\largeTree.txt", ',', ',')
B = normalizeGraph(B, 0.5)
print("largeTree")
obtainMaxEig(B, True, 2)
obtainNVM(B, True, 2)

C = importMatrixFile(".\data\cities.txt", ',', ',')
C = normalizeGraph(C, 0.5)
print("cities")
obtainMaxEig(C, True, 2)
obtainNVM(C, True, 4)

plotFromGraph(C)

D = importMatrixFile(".\data\windsurfers.txt", '\n', ' ')
D = normalizeGraph(D, 0.35)
print("windsurfers")
obtainMaxEig(D, True, 2)
obtainNVM(D, True, 4)

E = importMatrixFile(".\data\guineaTribe.txt", '\n', ' ')
E = normalizeGraph(E, 0.5)
print("guineaTribe")
obtainMaxEig(E, True, 2)
obtainNVM(E, True, 4)

#F = importEdgeListFile('.\data\\terrorist.txt', '\t')
#print("terrorist")
#obtainMaxEig(F, True, 2)

G = importEdgeListFile(".\data\\asgraph\\asgraph.txt", ':')
print('Oregon-AS graph')
#Warning: Can take up to 10 min to plot the graphs and you don't see very much
#plotFromGraph(G)
obtainMaxEig(G, True, 3)
obtainNVM(G, True, 4)


#Warning: Large file, takes up to 2 minutes
#H = importEdgeListFile(".\data\hyves\edges.csv", ',')
#print("hyves")
#obtainMaxEig(H, True, 3)

F = importEdgeListFile('.\data\\terrorist.txt', '\t')
F = normalizeGraph(F, 0.5)
print("terrorist")
obtainMaxEig(F, True, 2)
obtainNVM(F, True, 4)

plotFromGraph(F)
X = removeCriticalNode(F)

# Warning: Large file, takes up to 2 minutes
G = importEdgeListFile(".\data\hyves\edges.csv", ',')
print("hyves")
obtainMaxEig(G, True, 3)
obtainNVM(G, True, 4)

#necessary to avoid blocking of the script execution, plots are displayed when script is done
plot.show()
