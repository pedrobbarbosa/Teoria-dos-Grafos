from vertice import Vertice
from grafoerror import GrafoError

class Grafo:
  def __init__(self, nome: str):
    self.nome = nome
    self.vertices = []

  def adicionar_vertice(self, nome: str) -> None:
    self.vertices.append(Vertice(nome))
  
  def adicionar_aresta(self, origem: str, destino: str) -> None:
    pos = []
    for index, vertice in enumerate(self.vertices):
      if vertice.nome == origem or vertice.nome == destino:
        pos.append(index)
        
    if not len(pos):
      raise GrafoError(f'Vértices {origem} e {destino} não existem ou não foram encontrados')
    
    self.vertices[pos[0]].adicionar_aresta(self.vertices[pos[1]])
    self.vertices[pos[1]].adicionar_aresta(self.vertices[pos[0]])

  def ehRegular(self):
    len_adj_vertices = []
    for vertice in self.vertices:
       len_adj_vertices.append(len(vertice.arestas))
    if len(set(len_adj_vertices)) > 1:
      return False
    return 
  
  def ehCompleto(self):
    tamanho_grafo = len(self.vertices)
    print(tamanho_grafo)
    for vertice in self.vertices:
      if len(vertice.arestas) != tamanho_grafo:
        return False
    return True
  
  def busca_em_largura(self, vertice):
    fila = []
    vertice.visitado = True
    fila.append(vertice)
    # print(fila)

    while len(fila):
      u = fila[0]
      # print(fila)

      fila.pop(0)
      # print(fila)

      for w in u.arestas:
        if w.visitado == False:
          w.visitado = True
          fila.append(w)
      print(fila)

  def __repr__(self):
    print(self.nome)
    for vertice in self.vertices:
      print(f'{vertice.nome}: {vertice.arestas}')
    return ''