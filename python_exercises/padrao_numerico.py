# Lê o número de linhas da entrada padrão
n = int(input())

# Para cada linha i (de 1 até n)
for i in range(1, n + 1):
    # Para cada elemento j da linha i (de 0 até i-1)
    for j in range(i):
        # Padrão: primeiro elemento é i², cada próximo aumenta 2
        # Elemento j da linha i: i² + j*2
        print(i * i + j * 2, end=' ')
    # Pula a linha ao terminar cada linha do padrão
    print()
