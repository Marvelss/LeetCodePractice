class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r, k = 0, len(nums) - 1, len(nums) - 1
        result = [0] * len(nums)
        while l <= r:
            if nums[l] * nums[l] < nums[r] * nums[r]:
                result[k] = nums[r] * nums[r]
                r -= 1

            else:
                result[k] = nums[l] * nums[l]
                l += 1
            k -= 1
        return result


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    p = Solution()
    print(p.sortedSquares(nums))
