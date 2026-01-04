class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = dict()
        for item in nums:
            if item not in count:
                count[item] = 1
            else:
                return True
        return False
