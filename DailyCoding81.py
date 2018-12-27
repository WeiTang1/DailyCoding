class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hm = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 1:
            return [x for x in hm[digits]]
        if len(digits) == 0:
            return []
        ret = []
        for ans in self.letterCombinations(digits[1:]):
            for d in hm[digits[0]]:
                ret.append(d+ans)
        return ret


