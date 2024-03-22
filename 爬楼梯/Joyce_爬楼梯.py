
class Solution:
    def rec_stairs(n: int, res: dict):
        if n == 1:
            return res[1]
        if n == 2:
            return res[2]
        if not n-1 in res:
            a = Solution.rec_stairs(n-1, res)
            res[n-1] = a
        else:
            a = res[n-1]
        if not n-2 in res:
            b = Solution.rec_stairs(n-2, res)
            res[n-2] = b
        else:
            b = res[n-2]
        
        return a+b
    def climbStairs(self, n: int) -> int:
        return Solution.rec_stairs(n, {1: 1, 2: 2})