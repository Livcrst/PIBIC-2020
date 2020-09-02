
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx 
from random import random
from Grafos import CriarGrafo,PegarGrausDeVertice
from AnaliseDeDados import tratarDados

def mean(data):
    Sum = 0
    for i in data:
        Sum += i
    Sum = Sum/len(data)
    return Sum

#Criar a amostra, adotei tamanho 10 
vertices = int(input('Digite N: '))
sample = []
prob = []
for i in range(30):
    p = random()
    prob.append(p)
    graphSample = CriarGrafo(vertices,p)
    sample.append(graphSample)
#print(sample)
#Criar uma matriz com graus 10 X 10
degrees = []
for i in sample:
    degree = PegarGrausDeVertice(i)
    degrees.append(degree)
print(degrees)
#Pegar o Coeficiente de agrupamento globais 
clusterings = []
for i in sample: 
    auxiliary = nx.transitivity(i)
    clusterings.append(auxiliary)
print(clusterings)
#Pegar o Diametro do grafo (media dos graus)
diameters = []
for i in degrees:
    auxiliary = mean(i)
    diameters.append(auxiliary)
print('Diametros:',diameters)

#Calcular o quociente de d(p)/d(0) e c(p)/c(0)
print('Grafo FIXO')
graphFixed = CriarGrafo(vertices,0)

dataGraphDegree = PegarGrausDeVertice(graphFixed)
diameterFixed = mean(dataGraphDegree)

clusteringFixed = nx.transitivity(graphFixed)

quotienteC = []
quotienteD = []

#Quocientes de Clustering

for i in clusterings:
    auxiliary = i/clusteringFixed
    quotienteC.append(auxiliary)
print('Clustering',quotienteC)

for i in diameters:
    auxiliary = i/diameterFixed
    quotienteD.append(auxiliary)
print('Diameters',quotienteD)-


plt.plot(quotienteC,prob,'o')
plt.plot(quotienteD,prob,'o')
plt.show()