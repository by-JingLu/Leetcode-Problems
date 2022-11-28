def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        # Last i elements are already in place
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


a = [32, 5, 3, 6, 7, 54, 87]
bubble_sort(a)
print(a)
