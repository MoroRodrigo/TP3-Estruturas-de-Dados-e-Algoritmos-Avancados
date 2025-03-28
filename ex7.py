import heapq

def prim(grafo, inicio):
    # Inicialização
    n = len(grafo)
    custo = {v: float('inf') for v in grafo}
    custo[inicio] = 0
    pais = {v: None for v in grafo}
    visitados = set()
    pq = [(0, inicio)]  # (custo, vértice)

    while pq:
        # Seleciona o vértice com o menor custo
        custo_atual, u = heapq.heappop(pq)

        if u in visitados:
            continue
        
        visitados.add(u)

        # Atualiza o custo das arestas adjacentes
        for v, peso in grafo[u].items():
            if v not in visitados and peso < custo[v]:
                custo[v] = peso
                pais[v] = u
                heapq.heappush(pq, (peso, v))

    # Reconstruindo a Árvore Geradora Mínima
    arvore_geradora = []
    for v in grafo:
        if pais[v] is not None:
            arvore_geradora.append((pais[v], v, grafo[pais[v]][v]))  # (vértice de origem, vértice de destino, peso da aresta)

    return arvore_geradora

# Grafo representando bairros e custos de conexão (em milhões)
grafo = {
    'A': {'B': 5, 'C': 10, 'D': 2},
    'B': {'A': 5, 'C': 3, 'D': 6},
    'C': {'A': 10, 'B': 3, 'D': 7},
    'D': {'A': 2, 'B': 6, 'C': 7}
}

# Inicia o algoritmo de Prim a partir do bairro 'A'
arvore_geradora = prim(grafo, 'A')

# Exibe a Árvore Geradora Mínima
print("Árvore Geradora Mínima (Bairros interligados com o menor custo):")
for u, v, custo in arvore_geradora:
    print(f'{u} - {v}: {custo} milhões')
