## 283. Move Zeroes
### Question
Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
### Solution
```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            
            right += 1
            
        for i in range(left, len(nums)):
            nums[i] = 0
```
### Notes:
- Two pointers are `left` and `right`. 
  - `right` always move 1 to iterate the array.
  - `left` to record the item not equal to zero: when right not equal to zero, assign to left and left move 1

## 26. Remove Duplicates from Sorted Array
### Question
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of nums should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
### Solution
```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 0
        right = 0
        
        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
             
            right += 1
            
        return left + 1
```
### Notes:
- Very same as 283.
- Not `move zeros` should be `non-decreasing` to use two pointers!

## 350. Intersection of Two Arrays II
### Question
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
### Solution
```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        output = []
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                output.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return output
```
### Notes:
- We think using two pointers to check two arrays should work at first.
- Secondly `nums1` and `nums2` should be `sorted in non-decreasing`.
- Then it becomes same as 283 and 26.

## 167. Two Sum II - Input Array Is Sorted
### Question
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
### Solution
```
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        
        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
```
### Notes:
- The tricky is `sorted in non-decreasing`, so two pointers is the perfect way. Compare sum with target:  
  - if sum > target, max is too big, thus should not be used.  
  - if sum < target, min is too small, thus should not be used.
