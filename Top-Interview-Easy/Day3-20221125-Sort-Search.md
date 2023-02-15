## 88 Merge Sorted Array
### Notes
- Idea: use two pointers, insert the bigger one from the end of the array.
- Pay attension to the edge case: when don't have num in nums1 to campare, still need to modify nums1
### Solution
```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # check the num in nums1 and nums2
        i = m - 1
        j = n - 1
        # pointer of final array
        index = m + n - 1

        while j >= 0:
            # [0,0,0] m=0, [2,3,4] n=3
            if i < 0:
                nums1[index] = nums2[j]
                j -= 1
            else:
                if nums1[i] > nums2[j]:
                    nums1[index] = nums1[i]
                    i -= 1
                else:
                    nums1[index] = nums2[j]
                    j -= 1
            
            index -= 1

        return nums1
```

