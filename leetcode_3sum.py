class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time: O(n^2), Space: O(1) excluding output (sorting takes O(n) or O(log n) depending on implementation)
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Skip duplicate values for the fixed number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("Input:", nums1)
    print("Output:", sol.threeSum(nums1))
    print("Expected: [[-1, -1, 2], [-1, 0, 1]]")
    print()

    # Example 2
    nums2 = [0, 1, 1]
    print("Input:", nums2)
    print("Output:", sol.threeSum(nums2))
    print("Expected: []")
    print()

    # Example 3
    nums3 = [0, 0, 0]
    print("Input:", nums3)
    print("Output:", sol.threeSum(nums3))
    print("Expected: [[0, 0, 0]]")
