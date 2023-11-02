def quicksort(arr, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

a = [24, 9, 29, 14, 19, 27]
quicksort(a, 0, len(a) - 1)
print(a)
