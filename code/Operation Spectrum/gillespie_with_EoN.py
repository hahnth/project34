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
# E = importEdgeListFile("data/asgraph/peer_oregon_010331.txt", ':')
eig = obtainMaxEig(E, False, 2)
print(str(len(E.nodes)) + " nodes")
print("Eigenvalue of the Adjacency-Matrix = " + str(round(eig, 2)))

def s_SIR(eig, beta, delta, digits):
    return round(eig*beta/delta, digits)


def time_evolution_SIR(E, beta, delta, initial_size,
                       start_time, end_time, iterations, label, opt = 'Plot'):
    report_times = scipy.linspace(start_time,end_time,1000)
    Isum = scipy.zeros(len(report_times))
    Rsum = scipy.zeros(len(report_times))
    for i in range(iterations):
        # Selecting initial nodes randomly
	initial_nodes = random.sample(G.nodes, initial_size)
	t, S, I, R = EoN.fast_SIR(G, beta, delta, initial_infecteds = initial_nodes)
        _, newI, newR= EoN.subsample(report_times, t, S, I, R)
        #plt.plot(report_times, newI, linewidth=1, alpha = 0.4)
        Isum += newI
	Rsum += newR
    #Average value of all iterations
    I_average = Isum / float(iterations)
    R_average = Rsum / float(iterations)
    if (opt == 'Plot'):
        plt.loglog(report_times, I_average/(len(E)), label = label, linewidth = 5)
    if (opt == 'number_of_cured_nodes'):
        return R_average[-1]
        

def fig_5_left(G):
    digits = 2
    initial_size = 10# int(float(len(G))/(10**(2)))
    iterations = 100
    start_time = 0
    end_time = 99
    beta1, beta2, beta3, beta4 = 0.15, 0.05, 0.02, 0.01
    delta1, delta2, delta3, delta4 = 1, 1, 1, 1
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
    plt.savefig('fig_5_left.png')
    plt.show()


def fig_5_right():
    initial_size = int(float(len(E))/(10**(2)))
    iterations = 100
    start_time = 0
    end_time = 10
    delta = eig
    number_of_steps = 100
    beta_range = scipy.linspace(10**(-2), 10**2, number_of_steps)
    final_number_of_cured_nodes = scipy.zeros_like(beta_range)
    for i, beta  in enumerate(beta_range):
        final_number_of_cured_nodes[i] = time_evolution_SIR(E, beta, delta, initial_size, start_time, end_time, iterations, "Hi", opt = 'number_of_cured_nodes')
    plt.semilogx(beta_range, final_number_of_cured_nodes)
    plt.grid()
    plt.xlabel(r'Effective Strength of Virus $\lambda_1\beta/\delta$')
    plt.ylabel("Final Number of Cured Nodes")
    plt.grid()
    plt.savefig('fig_5_right.png')
    plt.show()




if __name__ == "__main__":
    fig_5_left()
    fig_5_right()


