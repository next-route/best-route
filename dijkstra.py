#importando as bibliotecas dedicadas a TEORIA DE GRAFO.
import networkx as nx
import matplotlib.pyplot as plt

#Cria um novo Grafo
G = nx.Graph()

#Adiciona nós com atributo de posição na imagem.
G.add_nodes_from([
    ("ESC1", dict(pos=(60,420))),
    ("ESC2", dict(pos=(840,245))),
    ("ESC3", dict(pos=(435,460))),
    ("DESC1", dict(pos=(160,85))),
    ("DESC2", dict(pos=(650,85))),
    ("DESC3", dict(pos=(885,460))),
    ("INT1", dict(pos=(180,170))),
    ("INT2", dict(pos=(310,220))),
    ("INT3", dict(pos=(150,265))),
    ("INT4", dict(pos=(125,330))),
    ("INT5", dict(pos=(265,300))),
    ("INT6", dict(pos=(340,300))),
    ("INT7", dict(pos=(425,350))),
    ("INT8", dict(pos=(485,230))),
    ("INT9", dict(pos=(650,240))),
    ("INT10", dict(pos=(690,170))),
    ("INT11", dict(pos=(765,275))),
    ("INT12", dict(pos=(780,400))),
    ("INT13", dict(pos=(605,335))),
    ])

#Adiciona arestas entre os nós com atributo da distância entre eles.
G.add_edges_from([
    ("ESC1","INT4",{'length':200}),
    ("ESC2","INT11",{'length':160}),
    ("ESC3","INT7",{'length':190}),
    ("DESC1","INT1",{'length':180}),
    ("DESC2","INT10",{'length':140}),
    ("DESC3","INT12",{'length':190}),
    ("INT1","INT2",{'length':270}),
    ("INT1","INT3",{'length':200}),
    ("INT2","INT3",{'length':250}),
    ("INT2","INT8",{'length':280}),
    ("INT3","INT4",{'length':120}),
    ("INT4","INT5",{'length':200}),
    ("INT5","INT6",{'length':100}),
    ("INT6","INT7",{'length':120}),
    ("INT7","INT8",{'length':210}),
    ("INT7","INT13",{'length':260}),
    ("INT8","INT9",{'length':250}),
    ("INT9","INT10",{'length':130}),
    ("INT9","INT11",{'length':130}),
    ("INT9","INT13",{'length':90}),
    ("INT11","INT12",{'length':170}),
    ("INT12","INT13",{'length':300})
    ])

#Reúne os atributos da posição do nó em uma variável "pos"
pos = nx.get_node_attributes(G,'pos')

#Reúne os atributos da distância das arestas em uma variável "lenght"
lenght = nx.get_edge_attributes(G,'length')

#Imprime as distâncias das arestas no gráfico gerado "Caso utilize comando plt.show()"
nx.draw_networkx_edge_labels(G,pos,edge_labels=lenght)

#Imprime os nós existentes no gráfico gerado "Caso utilize comando plt.show()"
nx.draw(G,pos, with_labels=True)

#Imprime rota mais curta conforme os parâmetros do nx.shortest_path(GRAFO UTILIZADO, LOCALIZAÇÃO ATUAL, DESTINO, PARÂMETRO PARA CÁLCULO)
print(nx.shortest_path(G,source="ESC1",target="DESC3", weight='length'))

#Gera mapa do Grafo
plt.show()
