class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # origin num is largest int
        # length of dp is amount + 1, because of dp[0]
        dp = [amount + 1] * (amount + 1)
        # Basic case
        dp[0] = 0

        # Cal every value in dp
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1