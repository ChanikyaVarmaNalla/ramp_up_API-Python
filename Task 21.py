def quick_sort(arr, low, high):
    if low < high:
        k = stock_prices[high]
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

stock_prices = [35.6, 38.5, 40.2, 41.0, 42.0, 45.2]
print("sorted List:", stock_prices)
while True:
    con = input("Do you wish to continue (Y/N): ")
    if con == "n":
        break
    elif con == "y":
        stock_price = float(input("New Price: "))
        stock_prices.append(stock_price)
        res = quick_sort(stock_prices, 0, len(stock_prices) - 1)
        print("Sorted List:", res)
    else:
        print("Enter a valid response")
