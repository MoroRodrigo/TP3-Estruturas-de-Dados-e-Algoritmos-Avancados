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

# Grafo representando os aeroportos e distâncias diretas entre eles (km)
grafo = {
    'Aeroporto A': {'Aeroporto B': 500, 'Aeroporto C': 700},
    'Aeroporto B': {'Aeroporto A': 500, 'Aeroporto D': 400},
    'Aeroporto C': {'Aeroporto A': 700, 'Aeroporto D': 300, 'Aeroporto E': 800},
    'Aeroporto D': {'Aeroporto B': 400, 'Aeroporto C': 300, 'Aeroporto E': 200},
    'Aeroporto E': {'Aeroporto C': 800, 'Aeroporto D': 200}
}

# Encontrar o menor caminho entre dois aeroportos
origem = 'Aeroporto A'
destino = 'Aeroporto E'
distancias, caminho = dijkstra(grafo, origem, destino)
trajeto = reconstruir_caminho(caminho, origem, destino)

# Exibindo resultados
print(f"Menor distância do {origem} para o {destino}: {distancias[destino]} km")
print(f"Trajeto mais curto: {' -> '.join(trajeto)}")
