from vertice import Vertice
from grafo import Grafo

G = Grafo('G1')

vertices = ['V1','V2','V3','V4','V5','V6']

for vertice in vertices:
  G.adicionar_vertice(vertice)

G.adicionar_aresta('V1','V2')
G.adicionar_aresta('V1','V3')

G.adicionar_aresta('V2','V3')
G.adicionar_aresta('V2','V4')
G.adicionar_aresta('V2','V5')

G.adicionar_aresta('V3','V4')

G.adicionar_aresta('V5','V6')

# Representação do grafo
# print(G) 

# print(G.ehRegular())
# print(G.ehCompleto())
print(G.busca_em_largura(G.vertices[0]))