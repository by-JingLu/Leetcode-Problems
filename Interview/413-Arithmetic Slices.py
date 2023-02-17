# Brute force
class Solution1:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)

        ans = 0
        slices = []
        for i in range(n - 2):
            for j in range(i + 1, n-1):
                if nums[j + 1] - nums[j] == nums[i + 1] - nums[i]:
                    ans += 1
                    slices.append(nums[i:j+2])
                else:
                    break
        print(slices)
        return ans

test1 = Solution1()
test1.numberOfArithmeticSlices([1, 2, 3, 4])

# Dynamic programming
class Solution2:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                ans += dp[i]
        
        return ans

test2 = Solution2()
print(test2.numberOfArithmeticSlices([2] * 10000))

# Dynamic programming - easy understand
class Solution3:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        dp = [0] * n
        dp[0], dp[1] = 0, 0
        
        # initial first two element diff
        diff = nums[1] - nums[0] 
        
        # record how many diff with same value, 
        # e.g. 1,2,3 -> there are 2 diff with same value "1"cs
        count = 1 
        
        for i in range(2, n):
            if nums[i] - nums[i-1] == diff:
                count += 1
            else:
                # reset count & diff
                diff = nums[i] - nums[i-1]
                count = 1 

            if count >= 2:
                dp[i] = count - 2 + dp[i-1] + 1 
            else: # there is no new slice, reuse previous value 
                dp[i] = dp[i-1]

        return dp[-1]

test3 = Solution3()
print(test3.numberOfArithmeticSlices([2] * 10000))