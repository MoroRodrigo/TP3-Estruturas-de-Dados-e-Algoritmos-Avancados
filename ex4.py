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

# Grafo representando cidades e os custos de transporte entre elas (pedágios + combustível em R$)
grafo = {
    'Cidade A': {'Cidade B': 120, 'Cidade C': 200},
    'Cidade B': {'Cidade A': 120, 'Cidade D': 100},
    'Cidade C': {'Cidade A': 200, 'Cidade D': 150, 'Cidade E': 300},
    'Cidade D': {'Cidade B': 100, 'Cidade C': 150, 'Cidade E': 80},
    'Cidade E': {'Cidade C': 300, 'Cidade D': 80}
}

# Encontra a rota mais econômica entre duas cidades
origem = 'Cidade A'
destino = 'Cidade E'
distancias, caminho = dijkstra(grafo, origem, destino)
trajeto = reconstruir_caminho(caminho, origem, destino)

# Exibindo resultados
print(f"Custo mínimo do transporte de {origem} para {destino}: R${distancias[destino]}")
print(f"Melhor rota: {' -> '.join(trajeto)}")
