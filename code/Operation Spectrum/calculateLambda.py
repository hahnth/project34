import numpy as np
import scipy as sp
import networkx as ntx
import sys


def maxEig(A):
    """Returns the largest eigenvalue of a symmetric matrix"""
    eigenVals = sp.sparse.linalg.eigsh(sp.sparse.csr_matrix.asfptype(A), k=1, return_eigenvectors=False, which='LM')
    return eigenVals[0]


def obtainMaxEig(G, out, digits):
    """Returns the largest eigenvalue (absolute value) of the adjacency matrix belonging to the graph G
       if out is True, the result of maxEig is printed with precision digits"""
    A = ntx.adjacency_matrix(G)
    try:
        ret = maxEig(A)
    except np.linalg.LinAlgError:
        print("Cannot calculate eigenvalues!", file=sys.stderr)
        return 0
    if out:
        print(np.round(ret, digits))
    return ret
