class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        begin = 0
        end = len(heights) - 1

        while begin < end:
            vol = min(heights[begin], heights[end]) * (end - begin)
            if vol > max_vol:
                max_vol = vol

            if heights[begin] > heights[end]:
                end -= 1
            else:
                begin += 1

        return max_vol