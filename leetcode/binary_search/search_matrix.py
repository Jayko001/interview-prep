class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                nums = matrix[m]
                il = 0
                ir = len(nums)

                while il <= ir:
                    im = il + ((ir - il) // 2)
                    if nums[im] == target:
                        return True
                    elif nums[im] > target:
                        ir = im - 1
                    else:
                        il = im + 1
                return False

            elif matrix[m][0] < target and matrix[m][-1] < target:
                l = m + 1
            else:
                r = m - 1

        return False