#sub set without duplicates recursion:
class NoDup(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return[nums,[]]
        ans = []
        for s in self.subsets(nums[1:]):
            ans.append(s)
            ans.append([nums[0]]+s)
        return ans


#sub set with duplicate backtract
class Dup(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        self.backtrack(nums, [], ans, 0)
        return ans

    def backtrack(self, nums, li, ans, index):
        ans.append(li)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.backtrack(nums, li + [nums[i]], ans, i + 1)
