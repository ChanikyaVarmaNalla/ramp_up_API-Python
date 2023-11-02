def merge_sorted_lists(list1, list2):
    list3 = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    list3.extend(list1[i:])
    list3.extend(list1[j:])

    return list3

l1 = [1.23, 2.34, 3.45, 4.56, 5.67, 6.78, 7.89, 8.90, 9.01, 10.12, 11.23, 12.34]
l2 = [2.34, 4.56, 6.78, 8.90, 11.23, 13.45, 15.67, 17.89, 20.12, 22.34, 24.56]

l3 = merge_sorted_lists(l1, l2)
print(l3)
