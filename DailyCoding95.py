class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(start):
            end = len(nums) - 1
            while start < end:
                swap(start, end)
                start += 1
                end -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        j = len(nums) - 1
        if i >= 0:
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

        swap(i, j)
        reverse(i + 1)

# https://leetcode.com/problems/next-permutation/solution/