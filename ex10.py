import heapq

def algoritmo_prim(grafo):
    # Número de bairros (vértices)
    n = len(grafo)
    
    # Inicializando a árvore geradora mínima (MST)
    mst = []
    custos = [float('inf')] * n
    custos[0] = 0
    heap = [(0, 0)]
    visitado = [False] * n
    
    while heap:
        # Pega bairro com o menor custo
        custo_atual, bairro_atual = heapq.heappop(heap)
        
        # Se o bairro já foi visitado, ignora
        if visitado[bairro_atual]:
            continue
        
        # Marca o bairro como visitado
        visitado[bairro_atual] = True
        # Adiciona o bairro na árvore geradora mínima
        mst.append((bairro_atual, custo_atual))
        
        # Verifica os vizinhos do bairro atual
        for vizinho, custo in grafo[bairro_atual]:
            if not visitado[vizinho] and custo < custos[vizinho]:
                custos[vizinho] = custo
                heapq.heappush(heap, (custo, vizinho))
    
    return mst

# Grafo representando os bairros e custos de instalação das tubulações
grafo = {
    0: [(1, 10), (2, 15), (3, 30)],
    1: [(0, 10), (2, 5), (3, 20)],
    2: [(0, 15), (1, 5), (3, 10)],
    3: [(0, 30), (1, 20), (2, 10)]
}

# Executa algoritmo de Prim
mst = algoritmo_prim(grafo)

# Exibe os bairros e os custos das tubulações da MST
print("Árvore Geradora Mínima (MST):")
for bairro, custo in mst:
    print(f"Bairro: {bairro}, Custo da tubulação: {custo}")
