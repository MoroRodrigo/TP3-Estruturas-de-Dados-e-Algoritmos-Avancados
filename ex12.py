import heapq
import random
import time
import sys

# Algoritmo de Dijkstra
def dijkstra(grafo, origem):
    n = len(grafo)
    distancias = [float('inf')] * n
    distancias[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        custo_atual, vertice_atual = heapq.heappop(fila)
        
        # Se o custo atual for maior que o custo conhecido, ignora
        if custo_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, custo in grafo[vertice_atual]:
            distancia = custo_atual + custo
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
    
    return distancias


# Algoritmo de Floyd-Warshall
def floyd_warshall(grafo):
    n = len(grafo)
    distancias = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        distancias[i][i] = 0
    
    for i in range(n):
        for vizinho, custo in grafo[i]:
            distancias[i][vizinho] = custo
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
    
    return distancias


# Função para gerar um grafo aleatório
def gerar_grafo(num_vertices, prob_arestas=0.5):
    grafo = {i: [] for i in range(num_vertices)}
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() < prob_arestas:  
                custo = random.randint(1, 10)  
                grafo[i].append((j, custo))
                grafo[j].append((i, custo)) 
    return grafo


# Função para comparar os algoritmos
def comparar_algoritmos(num_vertices, prob_arestas=0.5):
    grafo = gerar_grafo(num_vertices, prob_arestas)
    
    # Teste do Dijkstra
    origem = random.randint(0, num_vertices - 1)
    print(f"\nTestando Dijkstra a partir do vértice {origem}...")
    start = time.time()
    dijkstra_resultado = dijkstra(grafo, origem)
    dijkstra_tempo = time.time() - start
    print(f"Tempo de execução do Dijkstra: {dijkstra_tempo:.6f} segundos")

    # Teste do Floyd-Warshall
    print("\nTestando Floyd-Warshall...")
    start = time.time()
    floyd_resultado = floyd_warshall(grafo)
    floyd_tempo = time.time() - start
    print(f"Tempo de execução do Floyd-Warshall: {floyd_tempo:.6f} segundos")
    
    return dijkstra_tempo, floyd_tempo


# Função para testar os algoritmos em diferentes cenários
def testar_em_diferentes_tamanhos():
    tamanhos = [10, 20, 30, 50]  # Testar com 10, 20, 30, 50 vértices
    for tamanho in tamanhos:
        print(f"\nTestando grafo com {tamanho} vértices...")
        dijkstra_tempo, floyd_tempo = comparar_algoritmos(tamanho)
        print(f"\nTempo Dijkstra: {dijkstra_tempo:.6f} segundos")
        print(f"Tempo Floyd-Warshall: {floyd_tempo:.6f} segundos")
        

# Chama a função de teste
testar_em_diferentes_tamanhos()
