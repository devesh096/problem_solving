"""
LeetCode 3876. Construct Uniform Parity Array II
Difficulty: Medium
https://leetcode.com/problems/construct-uniform-parity-array-ii/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        # Time: O(n)  |  Space: O(1)
        #
        # Key idea:
        # Array ke sabse chhote number ki parity decide karti hai ki kya possible hai.
        # - Agar minimum odd hai, to us odd ko keep karke saare even numbers
        #   (jo usse bade honge) minus karke odd banaye ja sakte hain.
        # - Agar minimum even hai, to koi bhi odd number even nahi ban sakta
        #   (kyunki uske liye usse chhota odd chahiye, jo exist nahi karta).
        #   Is case mein sirf tab true jab poori array even ho.

        mn = min(nums1)
        if mn % 2 == 1:
            return True
        return all(x % 2 == 0 for x in nums1)


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 4, 7], True),
        ([2, 3], False),
        ([4, 6], True),
        ([1], True),
        ([2], True),
        ([2, 4, 5], False),
        ([1, 2, 4], True),
        ([3, 5, 7], True),
        ([8, 2, 10, 1], True),
    ]

    for nums, expected in tests:
        got = sol.uniformArray(nums)
        status = "OK" if got == expected else "FAIL"
        print(f"{status}  nums1={nums}  expected={expected}  got={got}")
