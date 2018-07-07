import networkx as nx

with open("aristas_final.txt", "r") as archivo:
    aristas = eval(archivo.read())

G = nx.Graph()
G.add_nodes_from(list(range(1700555)))
G.add_edges_from(aristas)
personas = list(map(list,nx.connected_components(G)))

with open("personas_final.txt", "w+") as archivo:
    archivo.write(str(personas))
