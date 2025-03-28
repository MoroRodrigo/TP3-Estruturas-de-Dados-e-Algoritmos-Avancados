import heapq

def dijkstra(grafo, origem):
    # Dicionário para armazenar a menor distância de origem para cada nó
    distancias = {nó: float('inf') for nó in grafo}
    distancias[origem] = 0  # Distância da origem para ela mesma é sempre zero
    
    # Fila de prioridade para escolher o próximo nó mais próximo a ser explorado
    fila_prioridade = [(0, origem)]  # (distância, nó)
    
    # Dicionário para rastrear o caminho percorrido
    caminho = {}
    
    while fila_prioridade:
        dist_atual, no_atual = heapq.heappop(fila_prioridade)
        
        # Se já encontramos um caminho mais curto, ignoramos
        if dist_atual > distancias[no_atual]:
            continue
        
        for vizinho, peso in grafo[no_atual].items():
            distancia = dist_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias, caminho

# Definição do grafo representando bairros e as distâncias entre eles
grafo = {
    'Centro': {'A': 2, 'B': 5},
    'A': {'Centro': 2, 'C': 3, 'D': 7},
    'B': {'Centro': 5, 'D': 4},
    'C': {'A': 3, 'D': 2, 'E': 6},
    'D': {'A': 7, 'B': 4, 'C': 2, 'E': 1},
    'E': {'C': 6, 'D': 1}
}

# Executando o algoritmo de Dijkstra a partir do Centro
distancias, caminho = dijkstra(grafo, 'Centro')

# Exibindo os resultados
print("Menor distância do Centro para cada bairro:")
for bairro, distancia in distancias.items():
    print(f"{bairro}: {distancia}")
