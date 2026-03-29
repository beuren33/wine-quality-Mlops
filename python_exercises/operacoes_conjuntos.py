"""
Módulo de operações com conjuntos em Python.

Este módulo implementa funções para realizar operações básicas com conjuntos:
- União de dois conjuntos
- Intersecção de dois conjuntos
- Elementos únicos (diferença)
- Teste de pertencimento e inclusão
"""


def uniao(A, B):
    """
    Retorna a união dos dois conjuntos A e B.
    
    A união contém todos os elementos que pertencem a A ou a B (ou ambos).
    
    Args:
        A (set): Primeiro conjunto
        B (set): Segundo conjunto
    
    Returns:
        set: A união de A e B
    
    Exemplo:
        >>> A = {1, 2, 3}
        >>> B = {3, 4, 5}
        >>> uniao(A, B)
        {1, 2, 3, 4, 5}
    """
    return A.union(B)


def interseccao(A, B):
    """
    Retorna a intersecção dos dois conjuntos A e B.
    
    A intersecção contém apenas os elementos que pertencem a ambos os conjuntos.
    
    Args:
        A (set): Primeiro conjunto
        B (set): Segundo conjunto
    
    Returns:
        set: A intersecção de A e B
    
    Exemplo:
        >>> A = {1, 2, 3}
        >>> B = {3, 4, 5}
        >>> interseccao(A, B)
        {3}
    """
    return A.intersection(B)


def unicos(A, B):
    """
    Retorna os elementos de A que não estão em B.
    
    Esta função realiza a diferença entre os conjuntos A e B,
    retornando apenas os elementos exclusivos de A.
    
    Args:
        A (set): Primeiro conjunto
        B (set): Segundo conjunto
    
    Returns:
        set: Elementos de A que não estão em B
    
    Exemplo:
        >>> A = {1, 2, 3}
        >>> B = {3, 4, 5}
        >>> unicos(A, B)
        {1, 2}
    """
    return A.difference(B)


def teste(A, valor):
    """
    Testa se um valor é um subconjunto ou elemento de A.
    
    Comportamento:
    - Se valor for um conjunto (set), retorna True se valor for um subconjunto de A
    - Se valor não for um conjunto, retorna True se valor for um elemento de A
    - Caso contrário, retorna False
    
    Args:
        A (set): Conjunto a ser testado
        valor: Um conjunto ou um elemento individual
    
    Returns:
        bool: True se a condição for atendida, False caso contrário
    
    Exemplos:
        >>> A = {1, 2, 3, 4, 5}
        >>> teste(A, {1, 2})  # valor é um subconjunto
        True
        >>> teste(A, {1, 6})  # valor não é um subconjunto
        False
        >>> teste(A, 3)  # valor é um elemento
        True
        >>> teste(A, 6)  # valor não é um elemento
        False
    """
    if isinstance(valor, set):
        # Se valor é um conjunto, verifica se é um subconjunto de A
        return valor.issubset(A)
    else:
        # Se valor não é um conjunto, verifica se é um elemento de A
        return valor in A


# ============================================================================
# EXEMPLOS DE USO
# ============================================================================

if __name__ == "__main__":
    # Definindo dois conjuntos de exemplo
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    
    print("=" * 60)
    print("OPERAÇÕES COM CONJUNTOS")
    print("=" * 60)
    
    print(f"\nConjunto A: {A}")
    print(f"Conjunto B: {B}")
    
    # Testando a função uniao
    print("\n--- UNIÃO ---")
    resultado_uniao = uniao(A, B)
    print(f"uniao(A, B) = {resultado_uniao}")
    
    # Testando a função interseccao
    print("\n--- INTERSECÇÃO ---")
    resultado_interseccao = interseccao(A, B)
    print(f"interseccao(A, B) = {resultado_interseccao}")
    
    # Testando a função unicos
    print("\n--- ELEMENTOS ÚNICOS DE A ---")
    resultado_unicos = unicos(A, B)
    print(f"unicos(A, B) = {resultado_unicos}")
    
    # Testando a função teste
    print("\n--- TESTES ---")
    
    print("\nTestando com subconjuntos:")
    print(f"teste(A, {{1, 2}}) = {teste(A, {1, 2})}")  # True
    print(f"teste(A, {{1, 6}}) = {teste(A, {1, 6})}")  # False
    print(f"teste(A, {{4, 5}}) = {teste(A, {4, 5})}")  # True
    
    print("\nTestando com elementos individuais:")
    print(f"teste(A, 3) = {teste(A, 3)}")  # True
    print(f"teste(A, 6) = {teste(A, 6)}")  # False
    print(f"teste(A, 1) = {teste(A, 1)}")  # True
    
    print("\nTestando com diferentes tipos:")
    print(f"teste(A, 'string') = {teste(A, 'string')}")  # False
    print(f"teste(A, 5.0) = {teste(A, 5.0)}")  # False (5.0 != 5 em sets)
    
    print("\n" + "=" * 60)
