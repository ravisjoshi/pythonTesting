"""
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once.

Input: x = 2, y = 3, bound = 10  /  Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Input: x = 3, y = 5, bound = 15  /  Output: [2,4,6,8,10,14]

Note:
    1 <= x <= 100
    1 <= y <= 100
    0 <= bound <= 10^6
"""
from math import sqrt
class Solution:
    def powerfulIntegers(self, x, y, bound):
        res = []
        for i in range(int(sqrt(bound))+1):
            for j in range(int(sqrt(bound))+1):
                val = x**i + y**j
                if val <= bound: res.append(val)
                else: break
        return sorted(set(res))


s = Solution()

x, y, bound = 60, 70, 10000
print(s.powerfulIntegers(x, y, bound))

x, y, bound = 2, 3, 10
print(s.powerfulIntegers(x, y, bound))

x, y, bound = 2, 1, 10
print(s.powerfulIntegers(x, y, bound))


