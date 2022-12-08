class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        
        def digits_add(num):
            sum = 0
            for i in str(num):
                sum += int(i)
            return sum
        
        sum_dict = {}
        
        for num in nums:
            digits_sum = digits_add(num)

            if digits_sum in sum_dict:
                sum_dict[digits_sum] += [num]
                
            else :
                sum_dict[digits_sum] = [num]
        
        ans = -1
        for value in sum_dict.values() :
            if  len(value) >= 2:
                # This is sorting in decreasing order
                ans = max(ans, sum(sorted(value, reverse=True)[0:2]))
        return ans

solu = Solution()
solu.maximumSum([42, 33, 60])