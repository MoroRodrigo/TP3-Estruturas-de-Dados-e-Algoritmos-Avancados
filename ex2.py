import heapq

def dijkstra(grafo, origem, destino=None):
    distancias = {nó: float('inf') for nó in grafo}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]
    caminho = {}
    
    while fila_prioridade:
        dist_atual, no_atual = heapq.heappop(fila_prioridade)
        
        if destino and no_atual == destino:
            break
        
        if dist_atual > distancias[no_atual]:
            continue
        
        for vizinho, peso in grafo[no_atual].items():
            distancia = dist_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias, caminho

def reconstruir_caminho(caminho, origem, destino):
    trajeto = []
    atual = destino
    while atual != origem:
        trajeto.append(atual)
        atual = caminho.get(atual)
        if atual is None:
            return []  # Retorna vazio se não houver caminho
    trajeto.append(origem)
    return trajeto[::-1]

# Grafo representando os bairros e tempo médio de deslocamento (minutos)
grafo = {
    'Centro': {'A': 10, 'B': 15},
    'A': {'Centro': 10, 'C': 20, 'D': 25},
    'B': {'Centro': 15, 'D': 30},
    'C': {'A': 20, 'D': 10, 'E': 35},
    'D': {'A': 25, 'B': 30, 'C': 10, 'E': 15},
    'E': {'C': 35, 'D': 15}
}

# Encontrar o menor caminho entre dois bairros
origem = 'Centro'
destino = 'E'
distancias, caminho = dijkstra(grafo, origem, destino)
trajeto = reconstruir_caminho(caminho, origem, destino)

# Exibindo resultados
print(f"Menor tempo do {origem} para o {destino}: {distancias[destino]} minutos")
print(f"Trajeto mais rápido: {' -> '.join(trajeto)}")
