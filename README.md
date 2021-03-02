# Teoria-dos-Grafos 🎓

Implementações dos algoritmos e modelos estudados na disciplina de teoria de grafos

> A teoria dos grafos ou de grafos é um ramo da matemática que estuda as relações entre os objetos de um determinado conjunto [Wikipédia](https://pt.wikipedia.org/wiki/Teoria_dos_grafos)

## Linguagem Utilizada 💻
- `Python` 🐍

## Estrutura de Implementação 💭

Dado um grafo G = (V,E), a estrutura de adjacência A é um
conjunto de n listas A(v), uma para cada vértice v pertencente
a V.

• Cada lista A(v) é denominada lista de adjacência do vér7ce v e
contém os vér7ces w adjacentes a v em G. Ou seja:
A(v) = {w | (v,w) pertence a E}

• A estrutura de adjacência é um vetor de n elementos (onde, n
é o número de vértices). Cada elemento i do vetor aponta para
uma lista linear. Essa lista contém os vér7ces adjacentes ao
vértices i.
![Image of Yaktocat](https://media.discordapp.net/attachments/637830778893500436/753691000676941975/unknown.png?width=792&height=587)

## Implementações ✅
- [x] Representação do Grafo
- - [x] Estrutura de adjacência
- [x] . Métodos básicos
- - [x] ehRegular: verifica se um determinado grafo é regular ou não. Deve retornar True ou False a depender do grafo.

- - [x] ehCompleto: verifica se um determinado grafo é completo ou não. Deve retornar True ou False a depender do grafo.

- - [x] ehConexo: verifica se um determinado grafo é conexo ou não. Deve retornar True ou False a depender do grafo. Deve utilizar busca em largura ou busca em profundidade para fazer essa verificação.

- [] Algoritmos
- - [x] Algoritmo de Busca em Largura: deve implementar o algoritmo de busca de largura utilizando uma pilha como estrutura de controle. o método deve receber um vértice para iniciar a busca. Durante a execução do algoritmo deve mostrar o status da pilha e a lista de vértices visistados e explorados.
- - [] Algoritmo de Busca em Profundidade: deve implementar o algoritmo de busca em profundidade utilizando uma fila como estrutura de controle. O método deve receber um vértice para iniciar a busca. Durante a execução do algoitmo deve mostrar o status da fila e a lista de vértices visitados e explorados.
- - Algoritmo de Menor Caminho (Dijkstra): deve implementar o algoritmo de Dijkstra que calcula o menor caminho de um vértice a outro no grafo.
Devem ser implementados duas versões desse algoritmo:
- - 1. A primeira recebe como parâmetro um vértice e o algoritmo retorna o menor caminho deste para todos os demais vértices. Neste caso, deve-se imprimir na tela a menor distância para cada par de vértice e o caminho final entre eles.
- - 2. A segunda recebe como parâmetro dois vértices e o algoritmo retorna o menor caminho somente entre estes dois vértices. Neste caso, deve-se imprimir na tela a menor distância entre eles e o caminho final.
