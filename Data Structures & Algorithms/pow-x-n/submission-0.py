class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n > 0:
            while n > 0: 
                res = res*x 
                n -= 1 
        if n < 0: 
            while n < 0: 
                res = res / x 
                n += 1 

        return res
