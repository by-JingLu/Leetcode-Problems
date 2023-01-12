class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros = 0
        left = 0
        res = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                while zeros > k:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1 
            res = max(res, i + 1 - left)
        
        return res

test = Solution()
result = test.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(result)