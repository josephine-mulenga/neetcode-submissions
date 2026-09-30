"""
understand
input = n (number of steps)
output = number of distinct ways to climb steps

PLAN
pattern 1 -> 2 -> 3 -> 5
numbers of ways at i = way at (n-1) + ways at n-2)
use a dictionaly to store the number of ways for each step
base case 

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = n
        memo = {1:1, 2:2}

        def ways(steps):
            if steps in memo:
                return memo[steps]

            memo[steps] = ways(steps - 1) + ways(steps - 2)
            return memo[steps]
        
        return ways(steps)

        