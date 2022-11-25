## 88 Merge Sorted Array
### Notes
- Idea: use two pointers, insert the bigger one from the end of the array.
- Pay attension to the edge case
### Solution
```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        index = m + n -1
        while j >= 0:
            # edge case [2, 0] m = 1 [1], n = 1
            if i < 0:
                nums1[index] = nums2[j]
                j -= 1
            else:
                if nums2[j] >= nums1[i]:
                    nums1[index] = nums2[j]
                    j -= 1
                else:
                    nums1[index] = nums1[i]
                    i -= 1
            index -= 1
```

