from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(1)
        # Approach:
        # 1. Compute XOR of entire array and count zeros.
        # 2. If total XOR != 0 → whole array works → return n
        # 3. If all elements are 0 → no non-zero XOR possible → return 0
        # 4. Otherwise total XOR is 0 but some non-zero exists →
        #    remove any one non-zero element → remaining XOR becomes that element ≠ 0
        #    → return n - 1

        n = len(nums)
        total_xor = 0
        zero_count = 0

        for num in nums:
            total_xor ^= num
            if num == 0:
                zero_count += 1

        # Case 1: whole array already has non-zero XOR
        if total_xor != 0:
            return n

        # Case 2: every element is zero
        if zero_count == n:
            return 0

        # Case 3: XOR is zero, but at least one non-zero element exists
        return n - 1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [1, 2, 3]
    print(f"Input: {nums1}")
    print(f"Output: {sol.longestSubsequence(nums1)}")  # Expected: 2
    print()

    # Example 2
    nums2 = [2, 3, 4]
    print(f"Input: {nums2}")
    print(f"Output: {sol.longestSubsequence(nums2)}")  # Expected: 3
    print()

    # Extra test: all zeros
    nums3 = [0, 0, 0]
    print(f"Input: {nums3}")
    print(f"Output: {sol.longestSubsequence(nums3)}")  # Expected: 0
    print()

    # Extra test: XOR zero but has non-zero
    nums4 = [1, 2, 3]  # 1^2^3 = 0
    print(f"Input: {nums4}")
    print(f"Output: {sol.longestSubsequence(nums4)}")  # Expected: 2
