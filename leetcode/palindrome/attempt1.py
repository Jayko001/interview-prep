class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c for c in s if c.isalnum()).lower()
        l = len(s)
        print(s)
        for i in range(int(l/2)):
            if s[i] == s[-i-1]:
                continue
            else:
                return False
        return True