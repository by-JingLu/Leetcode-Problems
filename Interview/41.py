class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:

        nums = sorted(nums)
        insert_zero = False

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
                insert_zero = True
        
        # Catch the exception such as [5, 6, 7]
        if nums[0] > 1 and insert_zero == False:
            return 1

        i = 0
        j = 1
        ans = None
        while j < len(nums):
            if nums[j] - nums[i] <= 1:
                i += 1
                j += 1
            else:
                ans = nums[i] + 1
                break

        if ans is None:
            return nums[-1] + 1
        else:
            return ans

test = Solution()
print(test.firstMissingPositive([5, 6, 7]))