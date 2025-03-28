import heapq

def dijkstra_voos(grafo, escalas_obrigatorias, tempos_conexao_maximos, origem, destino):
    distancias = {aeroporto: float('inf') for aeroporto in grafo}
    distancias[origem] = 0
    fila_prioridade = [(0, origem, 0)]
    caminho = {}

    while fila_prioridade:
        custo_atual, aeroporto_atual, tempo_conexao = heapq.heappop(fila_prioridade)

        if aeroporto_atual == destino:
            break

        if custo_atual > distancias[aeroporto_atual]:
            continue

        for vizinho, (custo_voo, tempo_escala) in grafo[aeroporto_atual].items():
            novo_custo = custo_atual + custo_voo
            novo_tempo_conexao = tempo_conexao + tempo_escala

            # Verificar se a conexão excede o tempo máximo permitido
            if novo_tempo_conexao > tempos_conexao_maximos.get(aeroporto_atual, float('inf')):
                continue  # Ignora conexões que excedem o tempo máximo

            # Verificar escalas obrigatórias
            if aeroporto_atual in escalas_obrigatorias:
                novo_custo += escalas_obrigatorias[aeroporto_atual]

            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                caminho[vizinho] = aeroporto_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho, novo_tempo_conexao))

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

# Grafo representando aeroportos e voos entre eles
# Cada aresta contém (custo do voo, tempo de escala)
grafo = {
    'A': {'B': (500, 2), 'C': (700, 3)},
    'B': {'A': (500, 2), 'C': (400, 1), 'D': (600, 2)},
    'C': {'A': (700, 3), 'B': (400, 1), 'D': (300, 1)},
    'D': {'B': (600, 2), 'C': (300, 1)}
}

# Escalas obrigatórias com custo adicional
escalas_obrigatorias = {'B': 100, 'C': 150}

# Tempo máximo de conexão permitido entre voos
tempos_conexao_maximos = {'A': 4, 'B': 3, 'C': 5}

origem = 'A'
destino = 'D'

distancias, caminho = dijkstra_voos(grafo, escalas_obrigatorias, tempos_conexao_maximos, origem, destino)
trajeto = reconstruir_caminho(caminho, origem, destino)

print(f"Menor custo da viagem de {origem} para {destino}: {distancias[destino]}")
print(f"Melhor rota: {' -> '.join(trajeto)}")
