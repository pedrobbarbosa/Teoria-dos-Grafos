class Vertice:
  def __init__(self, nome: str):
    self.nome = nome
    self.arestas = []
    self.visitado = False
  
  def adicionar_aresta(self, vertice):
    self.arestas.append(vertice)
    
  def __repr__(self):
    return f'{self.nome}'