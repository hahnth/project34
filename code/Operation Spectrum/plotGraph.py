import networkx as ntx
import matplotlib.pyplot as plot


def plotFromMatrix(A): #TODO nötig?
    graph = ntx.from_numpy_array(A)
    plotFromGraph(graph)


def plotFromGraph(G):
    ntx.draw_networkx(G)
    # TODO schönere Plots
    # TODO produziert Warnung
    plot.show()
