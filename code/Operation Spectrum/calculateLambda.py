import numpy as np
import scipy as sp
import sys


CONST_TOLERANCE = 1e-6 # Defines tolerance for comparisons, only modify here


def maxEig(A): # TODO Exceptions behandeln
    """Returns the largest eigenvalue of a symmetric matrix"""
    eigenVals = sp.sparse.linalg.eigsh(sp.sparse.csr_matrix.asfptype(A), k=1, return_eigenvectors=False)
    return eigenVals[0]


def obtainMaxEig(A, out, digits):
    """Exception handling for maxEig(A)
       if out is True, the result of maxEig is printed with precision digits"""
    try:
        ret = maxEig(A)
    except np.linalg.LinAlgError:
        print("Cannot calculate eigenvalues!", file=sys.stderr)
        return 0
    if out:
        print(np.round(ret, digits))
    return ret
