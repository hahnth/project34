import networkx as ntx
import matplotlib.pyplot as plot


def plotFromMatrix(A):
    graph = ntx.from_numpy_array(A)
    ntx.draw_networkx(graph)
    # TODO: schönere Plots
    plot.show()


