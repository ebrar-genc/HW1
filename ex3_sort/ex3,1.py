"""bubble sort
kucukten buyuge
lineer karsilastirir
en büyük sayı en sona atilir
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, -8, 12]
bubbleSort(arr)
print ("Sorted array is:", arr)