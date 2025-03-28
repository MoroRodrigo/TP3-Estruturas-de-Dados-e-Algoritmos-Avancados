import heapq

def dijkstra_modificado(grafo, estacoes_recarga, origem, destino, autonomia):
    distancias = {nó: float('inf') for nó in grafo}
    distancias[origem] = 0
    fila_prioridade = [(0, origem, autonomia)]  # (tempo acumulado, nó atual, bateria restante)
    caminho = {}
    
    while fila_prioridade:
        tempo_atual, no_atual, bateria_restante = heapq.heappop(fila_prioridade)
        
        if no_atual == destino:
            break
        
        if tempo_atual > distancias[no_atual]:
            continue
        
        for vizinho, (tempo, distancia) in grafo[no_atual].items():
            nova_bateria = bateria_restante - distancia
            
            if nova_bateria < 0 and no_atual not in estacoes_recarga:
                continue  # Ignora rotas que superam a autonomia sem possibilidade de recarga
            
            if no_atual in estacoes_recarga:
                nova_bateria = autonomia  # Recarrega a bateria
            
            novo_tempo = tempo_atual + tempo
            
            if novo_tempo < distancias[vizinho]:
                distancias[vizinho] = novo_tempo
                caminho[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (novo_tempo, vizinho, nova_bateria))
    
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

# Grafo representando cruzamentos e ruas da cidade
# Cada aresta contém (tempo estimado de deslocamento, distância da rua)
grafo = {
    'A': {'B': (5, 10), 'C': (10, 20)},
    'B': {'A': (5, 10), 'D': (8, 15)},
    'C': {'A': (10, 20), 'D': (6, 10), 'E': (12, 25)},
    'D': {'B': (8, 15), 'C': (6, 10), 'E': (5, 12)},
    'E': {'C': (12, 25), 'D': (5, 12)}
}

estacoes_recarga = {'C', 'E'}  # Estações de recarga disponíveis
origem = 'A'
destino = 'E'
autonomia = 30  # Autonomia do veículo em km

distancias, caminho = dijkstra_modificado(grafo, estacoes_recarga, origem, destino, autonomia)
trajeto = reconstruir_caminho(caminho, origem, destino)

print(f"Tempo mínimo de deslocamento de {origem} para {destino}: {distancias[destino]} minutos")
print(f"Melhor rota considerando recarga: {' -> '.join(trajeto)}")