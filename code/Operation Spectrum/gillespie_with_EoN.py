# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:16:51 2018

@author: Yannick
"""

import networkx as nx
import EoN
import matplotlib.pyplot as plt
from fetchData import importEdgeListFile
from calculateLambda import obtainMaxEig

'''
source for 'as20000102.txt': https://snap.stanford.edu/data/as-733.html
'''
E = importEdgeListFile("data/asgraph/as20000102.txt", '\t')
G = nx.Graph(E)

def s_SIR(Edgelist, gamma, tau):
    return obtainMaxEig(E, False, 2)*tau/gamma


def time_evolution_SIR(E, gamma, tau, initial_size, number_of_runs):
    ttot, Stot, Itot, Rtot = [], [], [], []
    for i in range(number_of_runs):
        t, S, I, R = EoN.Gillespie_SIR(G, tau, gamma,
                            initial_infecteds = range(initial_size))
        print(I)
        ttot.append(t)
        Stot.append(S)
        Itot.append(I)
        Rtot.append(R)
    print(ttot)
    print(ttot[1][1])
   # plt.plot(ttot,Stot)
        
        
    
    
    



#nx.draw(G)
initial_size = 10
gamma = 0.2 #rcovery rate? Noch einmal in der Dokumentation nachschauen
tau = 0.05 #transition rate? Noch einmal in der Dokumentation nachschauen
print(s_SIR(E, gamma, tau))
#t, S, I, R = EoN.Gillespie_SIR(G, tau, gamma,
#                            initial_infecteds = range(initial_size))
#
#plt.plot(t, I)
time_evolution_SIR(E, gamma, tau, initial_size, 10)
