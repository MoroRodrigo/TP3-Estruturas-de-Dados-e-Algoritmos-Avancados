def floyd_warshall(grafo):
    # Número de vértices no grafo
    n = len(grafo)
    
    # Inicialização da matriz de distâncias
    dist = [[float('inf')] * n for _ in range(n)]
    
    # A distância de um vértice para ele mesmo é 0
    for i in range(n):
        dist[i][i] = 0
    
    # Preenchendo a matriz de distâncias com as distâncias diretas
    for i in range(n):
        for j in range(n):
            if i in grafo and j in grafo[i]:
                dist[i][j] = grafo[i][j]
    
    # Aplicando o algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Verificando se o caminho passando por k é mais curto
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Grafo representando os bairros e o tempo de deslocamento entre eles
grafo = {
    0: {1: 5, 2: 10},
    1: {0: 5, 2: 3, 3: 6},
    2: {0: 10, 1: 3, 3: 7},
    3: {1: 6, 2: 7}
}

# Executa o algoritmo de Floyd-Warshall
distancias = floyd_warshall(grafo)

# Exibe as distâncias mais curtas entre todos os pares de bairros
print("Matriz de Distâncias Mínimas entre os Bairros:")
for i in range(len(distancias)):
    for j in range(len(distancias[i])):
        print(f"Distância de {i} para {j}: {distancias[i][j]} minutos")
