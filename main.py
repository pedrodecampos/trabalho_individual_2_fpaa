def max_min_select(arr, left, right):
    """
    Algoritmo de seleção simultânea do maior e menor elemento usando divisão e conquista.
    
    Args:
        arr: Lista de números
        left: Índice inicial
        right: Índice final
        
    Returns:
        Tuple contendo (menor_elemento, maior_elemento)
    """
    # Caso base: quando há apenas um elemento
    if left == right:
        return arr[left], arr[left]
    
    # Caso base: quando há dois elementos
    if right - left == 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        return arr[right], arr[left]
    
    # Divide o problema em duas partes
    mid = (left + right) // 2
    
    # Resolve recursivamente os subproblemas
    min1, max1 = max_min_select(arr, left, mid)
    min2, max2 = max_min_select(arr, mid + 1, right)
    
    # Combina os resultados
    min_val = min(min1, min2)
    max_val = max(max1, max2)
    
    return min_val, max_val

def main():
    # Exemplo de uso
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    print("Lista original:", arr)
    menor, maior = max_min_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {menor}")
    print(f"Maior elemento: {maior}")

if __name__ == "__main__":
    main() 