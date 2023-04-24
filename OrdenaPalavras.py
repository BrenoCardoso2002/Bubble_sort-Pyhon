def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = ["banana", "abacaxi", "laranja", "maça", "uva"]
print("Lista desordenada:")
print(arr)
bubble_sort(arr)
print("Lista ordenada:")
print(arr)
