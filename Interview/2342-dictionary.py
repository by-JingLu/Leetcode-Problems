class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        s_dict = {}

        for num in nums:
            s = sum([int(i) for i in str(num)])
            if s in s_dict:
                s_dict[s].append(num)
            else:
                s_dict[s] = [num]

        res = []
        for key, value in s_dict.items():
            if len(value) > 1:
                temp = sorted(value)
                res.append(temp[-1] + temp[-2])

        if res:
            return max(res)
        else:
            return -1

solu = Solution()
print(solu.maximumSum([42, 33, 60]))