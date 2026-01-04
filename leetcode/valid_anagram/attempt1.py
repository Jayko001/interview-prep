class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        s_elements = dict()
        t_elements = dict()
        for i in s:
            if i in s_elements:
                s_elements[i] += 1
            else:
                s_elements[i] = 1
        for j in t:
            if j in t_elements:
                t_elements[j] += 1
            else:
                t_elements[j] = 1
        if s_elements == t_elements:
            return True
        else:
            return False
