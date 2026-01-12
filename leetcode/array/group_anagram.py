class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [[]]
        d = {}
        c = 0

        for s in strs:
            l = list(s)
            l.sort()
            print(l)
            w = "".join(l)

            if w not in d:
                d[w] = c
                output.append([])
                output[c].append(s)
                c += 1
            else:
                index = d[w]
                output[index].append(s)
        print(d)

        return output