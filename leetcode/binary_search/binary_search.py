class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = -1
        start = 0
        end = len(nums) - 1

        while start <= end:
            med = start + ((end - start) // 2)
            if target == nums[med]:
                return med
            if target < nums[med]:
                end = med - 1
            else:
                start = med + 1
        return found
