def quick_sort(arr, low, high):
    if low < high:
        k = a[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < k:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        partition_index = i + 1
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
    return arr

a = [24, 9, 29, 14, 19, 27]
print("Unsorted List:", a)
res = quick_sort(a, 0, len(a) - 1)
print("Sorted List:", res)
