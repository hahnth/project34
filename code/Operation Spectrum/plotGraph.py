import networkx as ntx
import matplotlib.pyplot as plot


def plotFromMatrix(A):
    graph = ntx.from_numpy_array(A)
    plotFromGraph(graph)


def plotFromGraph(G): # TODO: dok (counter erklären)
    # TODO schönere Plots
    plot.figure(plotFromGraph.counter)
    ntx.draw_networkx(G)
    plotFromGraph.counter += 1


