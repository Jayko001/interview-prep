class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(1)
            for j in range(len(nums)):
                if i != j:
                    output[i] *= nums[j]

        return output