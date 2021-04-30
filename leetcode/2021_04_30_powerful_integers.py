class Solution:
    def powerfulIntegers(self, x, y, bound):
        # Compile two lists: x^i, y^j until they reach bound
        self.bound = bound
        pows_of_x = self._get_pows(x)
        pows_of_y = self._get_pows(y)

        # Keep a set of results
        results = set()

        # Compare all solutions until they reach bound, and add them to the set
        for i in pows_of_x:
            for j in pows_of_y:
                curr_sum = i + j
                if curr_sum <= bound:
                    results.add(curr_sum)
                if curr_sum >= bound:
                    break

        return list(results)

    def _get_pows(self, n):
        if n == 1:
            return [1]

        pows = []
        last_pow = 1
        while last_pow < self.bound:
            pows.append(last_pow)
            last_pow *= n
        return pows


if __name__ == "__main__":
    solution = Solution()
    print(solution.powerfulIntegers(2, 1, 10))
