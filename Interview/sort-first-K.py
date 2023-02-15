# Sort first K elements and last elements (check thepicture)
# 1. Bubble sort times: O(k^2 + n^2)
def solution1(n, nums, k):
    # sort first k in increasing
    for i in range(k):
        for j in range(k-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    # sort rest (n-k) in decreasing
    for i in range(k, n):
        for j in range(k, n - (i-k) -1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


print(solution1(8, [11,7,5,10,46,8,16,23], 3))
print(solution1(9, [5, 4, 6, 2, 1, 3, 8, 9, -1], 4))

# 2. Use other space, O(klognk + (n-k)log(n-k))
def solution2(n, nums, k):
    a1 = []
    a2 = []
    for i in range(k):
        a1.append(nums[i])
    for i in range(k, n):
        a2.append(nums[i])
    a1 = sorted(a1)
    a2 = sorted(a2)

    i = 0
    j = len(a2) - 1
    while i <= j:
        a2[i], a2[j] = a2[j], a2[i]
        i += 1
        j -= 1
    
    return a1 + a2

print(solution2(8, [11,7,5,10,46,8,16,23], 3))
print(solution2(9, [5, 4, 6, 2, 1, 3, 8, 9, -1], 4))
