def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i]["price"] < right_half[j]["price"]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# List of products
products = [
    {"name": "Laptop", "price": 999.99, "description": "High-performance laptop with the latest specs."},
    {"name": "Smartphone", "price": 599.99, "description": "Feature-rich smartphone with a sleek design."},
    {"name": "Headphones", "price": 149.99, "description": "Wireless headphones with ANC."},
    {"name": "Smart Watch", "price": 199.99, "description": "A smartwatch with advanced features."},
    {"name": "Camera", "price": 799.99, "description": "Professional DSLR camera with high-resolution."}
]

print("List of Products Before Merge Sort:")
for product in products:
    print(product)

merge_sort(products)

print("\nList of Products After Merge Sort:")
for product in products:
    print(product)
