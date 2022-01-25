class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        temp = x
        ans = 1
        while n > 0:
            if n & 1:
                ans = ans * temp

            temp = temp * temp
            n = n >> 1

        return ans
