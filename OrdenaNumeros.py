import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Últimos i elementos já estão ordenados
        for j in range(0, n-1):
            # Troca elementos se estiverem fora de ordem
            if arr[j] > arr[j+1]:
                # troca os elementos
                arr[j], arr[j+1] = arr[j+1], arr[j]

def createList():
    list = []
    for i in range(15):
        numero = random.randint(1, 1000)
        list.append(numero)
    return list

# Exemplo de uso:
arr = createList()
print("Lista desordenada:")
print(arr)
bubble_sort(arr)
print("Lista ordenada:")
print(arr)
