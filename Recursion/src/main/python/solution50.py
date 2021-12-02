class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(x, n):
            if n == 0:
                return 1
            temp = recur(x, n // 2)
            if n % 2 == 0:
                return temp * temp
            else:
                return temp * temp * x

        return recur(x, n) if n > 0 else 1 / (recur(x, -n))

        # res = 1
        # new_n = n if n>0 else -n

        # for i in range(0, new_n):
        #     res = res * x

        # return res if n>0 else 1/res

        # 都超时了
        ############################################

        # if n == 0:
        #     return 1

        # if n%2 == 0:
        #     if n > 0:
        #         return self.myPow(x, n//2) * self.myPow(x, n//2)
        #     else:
        #         return 1/(self.myPow(x, -n//2) * self.myPow(x, -n//2))

        # else:
        #     if n > 0:
        #         return self.myPow(x, n//2) * self.myPow(x, n//2) * x
        #     else:
        #         return 1/(self.myPow(x, -n//2) * self.myPow(x, -n//2) * x)