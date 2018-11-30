# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:16:51 2018

@author: Yannick
"""

import networkx as nx
import EoN
import random
import scipy
import matplotlib.pyplot as plt
from fetchData import importEdgeListFile
from calculateLambda import obtainMaxEig

'''
source for 'as20000102.txt': https://snap.stanford.edu/data/as-733.html
'''

E = importEdgeListFile("data/asgraph/as20000102.txt", '\t')
eig = obtainMaxEig(E, False, 2)
print("Eigenvalue of the Adjacency-Matrix = " + str(round(eig, 2)))


def s_SIR(eig, beta, delta, digits):
    return round(eig*beta/delta, digits)


def time_evolution_SIR(G, beta, delta, initial_size,
                       start_time, end_time, iterations, label):
    report_times = scipy.linspace(start_time,end_time,1000)
    Isum = scipy.zeros(len(report_times))
    for i in range(iterations):
        # Selecting initial nodes randomly
        initial_nodes = random.sample(G.nodes, initial_size)
        t, _, I, _ = EoN.fast_SIR(G, beta, delta, initial_infecteds = initial_nodes)
        newI= EoN.subsample(report_times, t, I)
        #plt.plot(report_times, newI, linewidth=1, alpha = 0.4)
        Isum += newI
    # Average value of all iterations
    I_average = Isum / float(iterations)
    plt.loglog(report_times, I_average/(len(E)), label = label, linewidth = 5)
        

def fig_5_left(G):
    digits = 2
    initial_size = int(float(len(G))/(10**(2)))
    iterations = 10
    start_time = 0
    end_time = 100
    beta1, beta2, beta3, beta4 = 0.5, 0.05,0.01,0.001 
    delta1, delta2, delta3, delta4 = 0.2, 0.2,1,0.2
    label1 = r'over-1, $\beta$ = '+ str(beta1)+', $\delta$ = ' + str(delta1) + ', s = ' + str(s_SIR(eig, beta1, delta1, digits))
    label2 = r'over-2, $\beta$ = '+ str(beta2)+', $\delta = $' + str(delta2)+ ', s = ' + str(s_SIR(eig, beta2, delta2, digits))
    label3 = r'under-1, $\beta$ = '+ str(beta3)+', $\delta = $' + str(delta3)+ ', s = ' + str(s_SIR(eig, beta3, delta3, digits))
    label4 = r'under-2, $\beta$ = '+ str(beta4)+', $\delta = $' + str(delta4)+ ', s = ' + str(s_SIR(eig, beta4, delta4, digits))
    
    time_evolution_SIR(G, beta1, delta1, initial_size, start_time, end_time,
                       iterations, label1)
    time_evolution_SIR(G, beta2, delta2, initial_size, start_time, end_time,
                       iterations, label2)
    time_evolution_SIR(G, beta3, delta3, initial_size, start_time, end_time,
                       iterations, label3)
    time_evolution_SIR(G, beta4, delta4, initial_size, start_time, end_time,
                       iterations, label4)
    plt.legend()
    plt.xlabel("Time ticks")
    plt.ylabel("Fraction of Infected People")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    fig_5_left(E)


