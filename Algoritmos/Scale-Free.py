#Criar Scale Free 
import networkx as nx
import matplotlib.pyplot as plt

G  =  nx.scale_free_graph(100)
nx.draw(G)
plt.show()

#Barabasi network 

n=100 #Number of nodes
m=4 #Number of initial links
seed=100
G=nx.barabasi_albert_graph(n, m, seed)
nx.draw(G)
plt.show()


kmax = 1 + (math.log(x)/Alpha)


