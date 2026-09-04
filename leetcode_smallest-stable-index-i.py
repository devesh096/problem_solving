"""
LeetCode 3903. Smallest Stable Index I
Difficulty: Easy
Link: https://leetcode.com/problems/smallest-stable-index-i/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        # Time: O(n), Space: O(n)
        # suffix_min[i] = min of nums[i..n-1]
        # prefix_max while scanning left to right = max of nums[0..i]
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            # instability score = prefix_max - suffix_min[i]
            if prefix_max - suffix_min[i] <= k:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([5, 0, 1, 4], 3, 3),
        ([3, 2, 1], 1, -1),
        ([0], 0, 0),
        ([5, 5, 5], 0, 0),
        ([1, 0], 0, -1),
        ([1, 0], 1, 0),
    ]

    for nums, k, expected in tests:
        got = sol.firstStableIndex(nums, k)
        status = "OK" if got == expected else "FAIL"
        print(f"{status}: nums={nums}, k={k} -> {got} (expected {expected})")
