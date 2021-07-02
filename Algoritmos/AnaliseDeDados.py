import networkx as nx #para criar o grafo

dados = open ('D:\PIBIC-2020\Datasets\protein.edgelist.txt','r') 

def tratarDados(dados):
    #Percorrendo para salvar os dados do arquivo para 
    TratarDados = []
    for i in dados:
        dado = i.rstrip()
        TratarDados.append(dado)
    print('Fim')
    #Separa os valores pelo \t
    teste = []
    for j in TratarDados:
        valor = j.split('\t')
        teste.append(valor)

    #Para pegar os vertices que li do arquivo 
    vertices = []
    #Para pegar as arestas 
    arestas = []
    for i in range(len(teste)):
        n = teste[i]
        vertice1 = int(n[0])
        vertice2 = int(n[1])
        aresta = (vertice1,vertice2)
        aresta2 = (vertice2,vertice1)
        if vertice1 not in vertices:
            vertices.append(vertice1)
        if aresta or aresta2 not in arestas:
            arestas.append(aresta)
        else:
            pass
    print(vertices)
    print('ARESTAS')
    print(arestas)

    #Criando a rede
    Rede = nx.Graph()
    Rede.add_nodes_from(vertices)
    Rede.add_edges_from(arestas)

    # dados.close()
    return Rede

redeTeste = tratarDados(dados)
betweennessCentrality = nx.betweenness_centrality(redeTeste)
print('BetweennessCentrality')
print(betweennessCentrality)


#Ler meus betweeness 
between = []







































































































































































































































































'''



def PegarGrausDeVertice(grafo): #Função que pega o grau de cada vértice
    graus = []
    Lista_de_Nós = list(grafo.nodes())
    for i in range(len(Lista_de_Nós)): #Com esse for consigo pegar a lista de graus dos vertices
        aux = nx.degree(grafo,i)
        graus.append(aux)
    return graus

def PlotarGraficoDistribuição(grafo): #Essa função está plotando sem transformar em dist binomial.
    GrausParaDist = PegarGrausDeVertice(grafo)
    valorP = poisson.rvs(3, size = 100)
    sn.distplot(valorP, hist = False, label= 'Poisson')
    sn.distplot(GrausParaDist, hist= False, label= 'Graus do grafo' )
    plotar.xscale('log')
    plotar.yscale('log')
    plotar.xlim(xmax= 10**2, xmin= 10**0 )
    plotar.ylim(ymax = 10**0, ymin = 10**-4 )
    plotar.xlabel('k')
    plotar.ylabel('P(X=k)')
    plotar.legend()
    plotar.show()

GrafoUso = tratarDados(dados)
PlotarGraficoDistribuição(GrafoUso) '''