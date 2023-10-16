def longest_increasing_subsequence(nums):
    lis_list = []
    global max_lis_len
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] >= nums[i]:
                sub = [nums[i], nums[j]]
                last_added = nums[j]
                for k in range(j + 1, len(nums)):
                    if nums[k] >= last_added:
                        sub.append(nums[k])
                        last_added = nums[k]
                lis_list.append(sub)
                if len(sub) >= max_lis_len:
                    max_lis_len = len(sub)
    return lis_list


sensor_readings = [10, 22, 9, 33, 21, 50, 41, 60, 80]
max_lis_len = 0
result = longest_increasing_subsequence(sensor_readings)
for sub_list in result:
    if len(sub_list) == max_lis_len:
        print(f"The LIS: {sub_list}\nLength: {max_lis_len}")
