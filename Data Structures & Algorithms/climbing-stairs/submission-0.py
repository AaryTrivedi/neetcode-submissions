class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def dp(x):
            if x > n:
                return 0
            elif x == n:
                return 1
            elif x in memo:
                return memo[x]
            tot = dp(x + 1) + dp(x + 2)
            memo[x] = tot
            return tot
        
        return dp(0)