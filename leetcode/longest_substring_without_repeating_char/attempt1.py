class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        start = 0
        end = 0
        sub_str = []

        for i in range(len(s)):
            if s[i] not in sub_str:
                sub_str.append(s[i])
                end = i

                print("new char added")
                print(sub_str)
                print("#")
            else:
                pos = sub_str.index(s[i])+1
                sub_str = sub_str[pos:]
                sub_str.append(s[i])

                if start < end:
                    start = start + s[start:end +1].index(s[i]) + 1
                    end = i
                    print("duplicate found", start)
                    print("updated substr: ", sub_str)
                    print("#")

            if (end-start)+1 > longest:
                longest = end-start+1
                print("updated longest", start+1, end, longest)
                print("#")

        return longest

sol = Solution()
print(sol.lengthOfLongestSubstring("aab"))