# Função auxiliar que consulta a memória dado uma chave
# Retorna 0 caso a chave não exista no dicionário
def consultar(memoria, chave):
    if chave in memoria:
        return memoria[chave]
    return 0


# Inicializa o dicionário de memória antes do loop principal
memoria = {}

# Loop principal: lê um comando por linha até encontrar 'fim'
while True:
    cmd = input().split()

    if cmd[0] == 'fim':
        break

    elif cmd[0] == 'set':
        # set <ID> <valor>: armazena em ID o valor inteiro
        memoria[cmd[1]] = int(cmd[2])

    elif cmd[0] == 'get':
        # get <ID>: imprime o valor armazenado em ID (0 se não definido)
        print(consultar(memoria, cmd[1]))

    elif cmd[0] == 'sum':
        # sum <ID1> <ID2> <ID3>: armazena em ID3 a soma de ID1 e ID2
        memoria[cmd[3]] = consultar(memoria, cmd[1]) + consultar(memoria, cmd[2])

    elif cmd[0] == 'mul':
        # mul <ID1> <ID2> <ID3>: armazena em ID3 o produto de ID1 e ID2
        memoria[cmd[3]] = consultar(memoria, cmd[1]) * consultar(memoria, cmd[2])
