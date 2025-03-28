import heapq

def algoritmo_prim(grafo):
    # Número de cidades
    n = len(grafo)
    
    # Inicializando a árvore geradora mínima (MST)
    mst = []
    # A lista de custos de conexão com a árvore
    custos = [float('inf')] * n
    # Começas pela cidade 0
    custos[0] = 0
    # Usa uma heap para sempre pegar a cidade com o menor custo
    heap = [(0, 0)]  # (custo, cidade)
    # Conjunto de cidades já incluídas na árvore
    visitado = [False] * n
    
    while heap:
        # Pegao vértice com o menor custo
        custo_atual, cidade_atual = heapq.heappop(heap)
        
        # Se a cidade já foi visitada, ignora
        if visitado[cidade_atual]:
            continue
        
        # Marca a cidade como visitada
        visitado[cidade_atual] = True
        # Adiciona o vértice atual na árvore geradora mínima
        mst.append((cidade_atual, custo_atual))
        
        # Verifica os vizinhos da cidade atual
        for vizinho, custo in grafo[cidade_atual]:
            if not visitado[vizinho] and custo < custos[vizinho]:
                custos[vizinho] = custo
                heapq.heappush(heap, (custo, vizinho))
    
    return mst

# Grafo representando as cidades e custos das linhas de transmissão
grafo = {
    0: [(1, 4), (2, 2)],
    1: [(0, 4), (2, 5), (3, 10)],
    2: [(0, 2), (1, 5), (3, 3)],
    3: [(1, 10), (2, 3)]
}

# Executa o algoritmo de Prim
mst = algoritmo_prim(grafo)

# Exibe as cidades e os custos das linhas de transmissão da MST
print("Árvore Geradora Mínima (MST):")
for cidade, custo in mst:
    print(f"Cidade: {cidade}, Custo da linha de transmissão: {custo}")
