from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1) after prefix computation
        s = list(accumulate(stones))
        f = s[-1]
        for i in range(len(s) - 2, 0, -1):
            f = max(f, s[i] - f)
        return f


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    stones1 = [-1, 2, -3, 4, -5]
    print(f"Input: stones = {stones1}")
    print(f"Output: {sol.stoneGameVIII(stones1)}")
    print("Explanation: Alice takes first 4 stones (sum=2), Bob takes remaining (sum=-3). Diff = 2 - (-3) = 5.\n")

    # Example 2
    stones2 = [7, -6, 5, 10, 5, -2, -6]
    print(f"Input: stones = {stones2}")
    print(f"Output: {sol.stoneGameVIII(stones2)}")
    print("Explanation: Alice takes all stones (sum=13), Bob scores 0. Diff = 13.\n")

    # Example 3
    stones3 = [-10, -12]
    print(f"Input: stones = {stones3}")
    print(f"Output: {sol.stoneGameVIII(stones3)}")
    print("Explanation: Alice must take both (sum=-22). Diff = -22.")
