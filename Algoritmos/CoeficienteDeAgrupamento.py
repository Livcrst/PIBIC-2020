from scipy.stats import binom # Importe da distribuição binomial 
from scipy.stats import poisson #import da disttribuição poisson
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx 
import math
from Grafos import CriarGrafo,PegarGrausDeVertice
from AnaliseDeDados import tratarDados


dados = open ('D:\PIBIC\PIBIC-2020\Datasets\protein.edgelist.txt','r') 

Graff = tratarDados(dados)
graus = PegarGrausDeVertice(Graff)

mediaDeGraus = 0
soma = 0
for i in graus:
    soma += i
mediaDeGraus = soma/len(graus)
print(mediaDeGraus)
#D = nx.diameter(comp)
                                                   