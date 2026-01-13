class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = dict()

        longest = 0

        for i in range(len(s)):
            # element not seen yet, add to dict
            if s[i] not in substr:
                substr[s[i]] = i

            # repeat character
            else:
                dup = substr[s[i]]
                # remove all chars before the dup, add dup again
                substr = {k: v for k, v in substr.items() if v <= dup}
                substr[s[i]] = i

            # update longest
            if len(substr) > longest:
                longest = len(substr)

        return longest
