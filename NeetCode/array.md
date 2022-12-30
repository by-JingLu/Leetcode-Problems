## 27 Remove Element
### Notes
- Two pointer, same as 26
### Solution
```
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
```


## 1470 Shuffle the Array
### Notes
- Use extra space: space: O(2n), time: O(n)
- No extra time: space: O(1), time: O(2n) `[1,2,3,7,8,9]` -> `[1,2,3,(1,7),(2,8)(3,9)]`->`[1,7,2,8,3,9]`
### Solution
Use extra time
```
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i = 0
        j = n
        while j < 2*n:
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        return ans
```
No extra time
```
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        while j < 2*n:
            nums[j] = (nums[i], nums[j])
            i += 1
            j += 1
        i = 0
        j = n
        while j < 2*n:
            temp = nums[j]
            nums[i] = temp[0]
            nums[i+1] = temp[1]
            i += 2
            j += 1      
        return nums
```


## 15 3Sum
### Notes
- Two pointer based on [167. Two Sum II - Input Array Is Sorted](/Algorithm-I/Day3-Two-Pointers.md)
- Sort the array, then iterate the array, find `num1 + num2 == 0 - num[i]`
- When the num duplicate with previous one, move to next num
- Time: O(n2)
### Solution
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                elif k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k -= 1
                else:
                    if nums[j] + nums[k] == target:
                        ans.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] < target:
                        j += 1
                    else:
                        k -= 1
        return ans
```


## 11 Container With Most Water
### Notes
- Brute force: time O(n2), can't pass
- Two pointer O(n): move the smaller one
- [Important: how to understand the problem and two pointer deeply!](https://leetcode.wang/leetCode-11-Container-With-Most-Water.html)
### Solution
Brute
```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                contain = min(height[i], height[j]) * (j - i)
                ans = max(ans, contain)
        return ans
```
Two pointer
```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            contain = min(height[i], height[j]) * (j - i)
            ans = max(ans, contain)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ans
```
## 
### Notes
- 
### Solution
```

```