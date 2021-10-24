# Calculate shortest path lenght using dijktra algorithm
import networkx as nx

G = nx.Graph()
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

pos = nx.get_node_attributes(G,'pos')
lenght = nx.get_edge_attributes(G,'length')

def path(status, location):
    status_truck = status
    
    
    
    if status_truck == True:
        descargas = ["DESC1", "DESC2", "DESC3"]
        valormenor=[]
        for tgt in descargas:
            valormenor.append(nx.shortest_path_length(G,source=location,target=tgt, weight='length'))    

        tmp = min(valormenor)
        idx = valormenor.index(tmp)
        r = nx.shortest_path(G,source=location,target=descargas[idx], weight='length')
        return r
    else:
        cargas = ["ESC1", "ESC2", "ESC3"]
        valormenor=[]
        for tgt in cargas:
            valormenor.append(nx.shortest_path_length(G,source=location,target=tgt, weight='length'))
               
        tmp = min(valormenor)
        idx = valormenor.index(tmp)
        r = nx.shortest_path(G,source=location,target=cargas[idx], weight='length')
        return r
    