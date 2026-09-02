class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Time: O(1), Space: O(1)
        # Brain teaser: har valid input ke liye answer hamesha True hota hai.
        #
        # Case 1: saare numbers even YA saare odd
        #   -> nums2 = nums1 rakh do. Parity already uniform hai.
        #
        # Case 2: mix of even aur odd (kam se kam 1 even + 1 odd)
        #   -> har i ke liye opposite parity wala koi j != i choose karo
        #      even - odd = odd
        #      odd - even = odd
        #   -> nums2 ke saare elements odd ho jaate hain.
        #
        # n == 1 bhi Case 1 me cover ho jata hai (sirf original number rakhna padta hai).
        return True


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    nums1 = [2, 3]
    print("Input:", nums1)
    print("Output:", sol.uniformArray(nums1))
    print("Expected: True")
    print()

    # Example 2
    nums2 = [4, 6]
    print("Input:", nums2)
    print("Output:", sol.uniformArray(nums2))
    print("Expected: True")
    print()

    # Extra: single element
    nums3 = [7]
    print("Input:", nums3)
    print("Output:", sol.uniformArray(nums3))
    print("Expected: True")
    print()

    # Extra: mixed longer
    nums4 = [1, 2, 4]
    print("Input:", nums4)
    print("Output:", sol.uniformArray(nums4))
    print("Expected: True")
