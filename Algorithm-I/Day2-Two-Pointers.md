## 977. Squares of a Sorted Array
### Question
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an `O(n)` solution using a different approach?

### Solution
```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        
        while left <= right:
            l_result = nums[left] ** 2
            r_result = nums[right] ** 2
            
            if r_result >= l_result:
                output[index] = r_result
                right -= 1
            else:
                output[index] = l_result
                left += 1
            index -= 1
            
        return output
```
### Notes
- Time complexity: `O(n)`  
  Space complexity: `O(n)`
- Tow points are left and right, compare their results and decide which  one to move.

## 189. Rotate Array
### Question
Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

Follow up: Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with `O(1)` extra space?
### Solution 1, 2
```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n       
        left = 0
        right = n - k
        while right < n:
            nums.insert(left, nums[right])
            nums.pop(right + 1)
            left += 1
            right += 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        for _ in range (k):
            temp = nums[n - 1]
            nums.pop(n - 1)
            nums.insert(0, temp)
```
### Solution 3
```
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        
    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
```
### Notes
- Very important: Real `k` need to be concerned.
- Easiest way is creating a new list.
- Solution 1, 2: Use `nums.pop()` and `nums.insert()`
- Solution 3: (1) reverse all the elements of the array; (2) reverse the first k elements of the array; (3) reverse the rest n-k elements of the array.
```
Let n = 7 and k = 3
- Original List                   : 1 2 3 4 5 6 7
- After reversing all numbers     : 7 6 5 4 3 2 1
- After reversing first k numbers : 5 6 7 4 3 2 1
- After reversing last n-k numbers: 5 6 7 1 2 3 4 
```