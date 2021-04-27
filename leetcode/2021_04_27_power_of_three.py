import math
from decimal import Decimal, getcontext


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        getcontext().prec = 20
        log = Decimal(n).ln() / Decimal(3).ln()
        return log % 1 == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfThree(243))