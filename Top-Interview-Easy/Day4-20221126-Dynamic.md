## 70 Climbing Stairs
### Question
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?
### Notes
- Recursion: Time Limit Exceeded. Two basic cases, so the recursion case is the sum of two
- Recursion + Memorization: Optimize recursion, if the result have been calculate, not do recursion again, stroe it to save time. `Hint`: put the dictionary in class initial instruction otherwise it will be clean every time the function is called.
- Iteration/Dynamic Program: `f(1) + f(2) + f(2) + f(3) = f(5)` `f(1) + f(2) + f(2) + f(3) + f(3) + f(4)= f(6)` 
### Solution
Recursion
```
class Solution:
    def climbStairs(self, n: int) -> int:
        # Recursion
        # base case
        if n == 1:
            return 1
        if n == 2:
            return 2
        # recursion case
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```
Recursion + Memorization
```
class Solution:
    # Recursion
    def __init__(self):
        # Basic case dict
        self.ways_dict = {1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        # Recursion case
        if n not in self.ways_dict:
            self.ways_dict[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.ways_dict[n]
```
Iteration
```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 2
        before_prev = 1
        ans = 0
        for i in range(3, n + 1):
            ans = prev + before_prev
            before_prev = prev
            prev = ans   

        return ans
```

## 198 House Robber
### Notes
- Reference](https://leetcode.wang/leetcode-198-House-Robber.html)
- Recursion: Time Limit Exceeded. 
- Dynamic Program: focus on the definition of dp, previous n shop's money, so should use `n+1` `i-1`
### Solution
Dynamic Programming
```
class Solution():
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range (2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return max(dp)
```
Recursion
```
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursion
        n = len(nums)
        # basic case
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Recursion case
        return max(self.rob(nums[:n-1]), self.rob(nums[:n-2]) + nums[-1])
```


## 53 Maximum Subarray
### Question
### Notes
- Nested Loops: no wrong but Time Limit Exceeded.
- Dynamic Program: `dp[i]` means subarrays with the end-item's index is `i`. [Reference](https://leetcode.com/problems/maximum-subarray/solutions/378937/python-dynamic-programming-solution/?languageTags=python&topicTags=dynamic-programming)
    ![](/Top-Interview-Easy/image/53.png)
### Solution
Nested Loops
```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                ans.append(sum(nums[i:j]))
        return max(ans)
```
Dynamic Programming
```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i]) 
        return max(dp)
```

## 121 Best Time to Buy and Sell Stock
### Question
### Notes
- Nested Loops: no wrong but Time Limit Exceeded.
- Tow pointer (Array): Optimize nested loops. [Reference](https://leetcode.wang/leetcode-121-Best-Time-to-Buy-and-Sell-Stock.html)
- Dynamic program: based on 53. [Reference](https://leetcode.wang/leetcode-121-Best-Time-to-Buy-and-Sell-Stock.html)
### Solution
Dynamic Programming
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [None] * len(prices)
        dp[0] = 0

        for i in range(1, len(prices)):
            num = prices[i] - prices[i - 1]
            dp[i] = max(dp[i - 1] + num, num)

        return max(dp)
```
Two Pointer
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        i = 0  # buy
        j = 1  # sell

        while j < len(prices):
            if prices[j] > prices[i]:
                profit.append(prices[j] - prices[i])
                j += 1
            else:
                i = j
                j += 1

        if len(profit) == 0:
            return 0
        else:
            return max(profit)
```
Nested Loops
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        
        for i in range(len(prices)):
            
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] >= 0:
                    profit.append(prices[j] - prices[i])

        if len(profit) == 0:
            return 0
        else:
            return max(profit)
```


