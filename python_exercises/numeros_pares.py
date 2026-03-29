from functools import reduce

# Lê a linha da entrada padrão como string
linha = input()

# Separa a string pelos espaços em branco e converte cada elemento para inteiro
numeros = list(map(int, linha.split()))

# Filtra somente os números pares usando filter e função lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Ordena a lista de pares em ordem crescente
pares.sort()

# Imprime os números pares separados por espaço em branco
for numero in pares:
    print(numero, end=' ')

# Imprime o pulo de linha após os números pares
print()

# Calcula e imprime a soma dos números pares usando reduce e função lambda
# O terceiro argumento 0 garante que funcione mesmo com lista vazia
soma = reduce(lambda acc, x: acc + x, pares, 0)
print(soma)
