
from random import random,randrange
import networkx as nx
import math
import numpy as np 
import seaborn as sn 
from math import factorial
def CriarGrafo(N,P):
    Numero_Max = (N*(N-1))/2 

    Lista_de_Nós = []
    for i in range(N):
        Lista_de_Nós.append(i)
    print(Lista_de_Nós)
    #
    Lista_de_Arestas = []
    Num_Max_index = int(Numero_Max)
    for j in range(Num_Max_index):
        numero = random() #Essa função retorna os numeros entre 0 e 1  
        index_1 = randrange(N)
        index_2 = randrange(N)
        if index_1 == index_2:
            while index_1 == index_2:
                index_1 = randrange(N)
                index_2 = randrange(N)

        if numero > P:
            aresta1 = Lista_de_Nós[index_1]
            aresta = Lista_de_Nós[index_2]
            Conj_aresta = (aresta1,aresta)
            Conj_aresta2 = (aresta,aresta1)
            if len(Lista_de_Arestas) <= Numero_Max:
                if not (Conj_aresta or Conj_aresta2) in Lista_de_Arestas:
                    Lista_de_Arestas.append(Conj_aresta)
                else:
                    
                    pass
            else: 
                print('Não é possível pôr mais arestas')
                pass
        else:
            pass
    print(Lista_de_Arestas)
    #
    grafo = nx.Graph()
    grafo.add_nodes_from(Lista_de_Nós)
    grafo.add_edges_from(Lista_de_Arestas)
    return grafo
#
def PegarGrausDeVertice(grafo): #Função que pega o grau de cada vértice
    graus = []
    Lista_de_Nós = list(grafo.nodes())
    for i in range(len(Lista_de_Nós)): #Com esse for consigo pegar a lista de graus dos vertices
        aux = nx.degree(grafo,i)
        graus.append(aux)
    return graus
#
def PlotarGrafo(grafo):
    impressão = nx.spring_layout(grafo)
    nx.draw_networkx_nodes(grafo,impressão,node_size=20,node_color='#836FFF',) #Referencia dos parametros da função
    nx.draw_networkx_edges(grafo,impressão) 
    plotar.show()
#
def PlotarGraficoDistribuição(grafo): #Essa função está plotando sem transformar em dist binomial.
    GrausParaDist = PegarGrausDeVertice(grafo)
    valorB = binom.rvs(100,0.6,size = 80)
    valorP = poisson.rvs(60, size = 80)
    #
    sn.distplot(valorB, hist = False, label= 'Binomial')
    sn.distplot(valorP, hist = False, label= 'Poisson')
    sn.distplot(GrausParaDist, hist= False, label= 'Graus do grafo' )
    plotar.xlim([0,80])
    plotar.xlabel('k')
    plotar.ylabel('P(X=k)')
    plotar.legend()
    plotar.show()


# Chamadas de função 
'''GrafoUso = CriarGrafo()
PlotarGraficoDistribuição(GrafoUso)
print('Plot de grafo')
#PoissonPlot(GrafoUso)
#PlotarGrafo(GrafoUso)



'''




