import networkx as ntx
import matplotlib.pyplot as plot


def plotFromMatrix(A):
    graph = ntx.from_numpy_array(A)
    plotFromGraph(graph)


def plotFromGraph(G):
    ntx.draw_networkx(G)
    # TODO schönere Plots
    plot.draw()
