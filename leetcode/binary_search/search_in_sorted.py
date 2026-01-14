class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + ((r-l)//2)

            if nums[l] < nums[r]:
                print("entering sorted array")
                il, ir = l, r

                while il <= ir:
                    im = il + ((ir-il)//2)

                    if nums[im] == target:
                        return im
                    elif nums[il] < target:
                        il = im + 1
                    else:
                        ir = im - 1
                return -1
            elif nums[m] == target:
                return m
            elif nums[l] > nums[m]:
                l = m + 1
                print("updading l", l)
            else:
                r = m - 1
                print("updating r", r)

        return -1
