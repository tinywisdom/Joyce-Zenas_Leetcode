class Solution:
    def climbStairs(self, n: int) -> int:
        ways = []
        ways.append(1)
        ways.append(2)
        j = 2
        while j <= n-1:
            ways.append(ways[j-1] + ways[j-2])
            j = j + 1
        return ways[n-1]