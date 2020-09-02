import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx 
from random import random
import string

SmallWolrd = nx.watts_strogatz_graph(110,11,0.03) #Cria a rede de mundo pequeno 

clusttering_zero = nx.transitivity(SmallWolrd) #Coeficiente de agrupamento global
average_path_legth = nx.average_shortest_path_length(SmallWolrd) #Tamanho do caminho médio mais curto

'''
dataSample = open('D:\PIBIC\PIBIC-2020\Watts-strogatz\Data out.csv','w')
print ('p\tC\tL')
dataSample.write('p,C(p)/C(0),L(p)/L(0)\n')

'''

dataSamples = []
for log_exp in np.arange(-40, 1, 1): #Lista de dados
    p = np.power(10, log_exp/10.0)
    g = nx.watts_strogatz_graph(100,10,p)
    
    c = nx.transitivity(g)
    a = nx.average_shortest_path_length(g)

    dataTuple = (p, c/clusttering_zero, a/average_path_legth)

    print(p, c/clusttering_zero, a/average_path_legth)

    dataSamples.append(dataTuple)


prob = []
cluster = []
average = []

for i in dataSamples:
    prob.append(i[0])
    cluster.append(i[1])
    average.append(i[2])

plt.scatter(cluster,prob, label = 'C(p)/C(0)')
plt.scatter(average,prob, label = 'L(p)/L(0)') 
plt.legend()
plt.show()