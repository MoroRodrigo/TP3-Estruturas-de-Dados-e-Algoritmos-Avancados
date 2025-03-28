import heapq

def algoritmo_prim(grafo):
    # Número de torres
    n = len(grafo)
    
    # Inicializando a árvore geradora mínima (MST)
    mst = []
    custos = [float('inf')] * n
    custos[0] = 0
    heap = [(0, 0)] 
    visitado = [False] * n
    
    while heap:
        # Pega a torre com o menor custo
        custo_atual, torre_atual = heapq.heappop(heap)
        
        # Se a torre já foi visitada, ignora
        if visitado[torre_atual]:
            continue
        
        # Marca a torre como visitada
        visitado[torre_atual] = True
        # Adiciona a torre na árvore geradora mínima
        mst.append((torre_atual, custo_atual))
        
        # Verifica os vizinhos da torre atual
        for vizinho, custo in grafo[torre_atual]:
            if not visitado[vizinho] and custo < custos[vizinho]:
                custos[vizinho] = custo
                heapq.heappush(heap, (custo, vizinho))
    
    return mst

# Grafo representando as torres e os custos de conexão entre elas
grafo = {
    0: [(1, 10), (2, 15), (3, 30)],
    1: [(0, 10), (2, 5), (3, 20)],
    2: [(0, 15), (1, 5), (3, 10)],
    3: [(0, 30), (1, 20), (2, 10)]
}

# Executa o algoritmo de Prim
mst = algoritmo_prim(grafo)

# Exibe as torres e os custos das conexões da MST
print("Árvore Geradora Mínima (MST):")
for torre, custo in mst:
    print(f"Torre: {torre}, Custo de conexão: {custo}")
