import math


class Solution:
    def searchRange(self, nums, target):
        self.nums = nums
        self.target = target

        if len(nums) == 0:
            return [-1, -1]

        min_index = self._bin_search(0, len(nums) - 1)
        max_index = self._bin_search(0, len(nums) - 1, last=True)

        return [min_index, max_index]

    def _bin_search(self, left, right, last=False):
        if left >= right:
            if self.nums[left] != self.target:
                return -1
            else:
                return left

        center = math.floor((left + right) / 2)

        if self.nums[center] < self.target:
            return self._bin_search(center + 1, right, last)
        elif self.nums[center] > self.target:
            return self._bin_search(left, center - 1, last)
        else:
            if last:
                index = self._bin_search(center + 1, right, last)
            else:
                index = self._bin_search(left, center - 1, last)

            if index == -1:
                index = center

        return index


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
