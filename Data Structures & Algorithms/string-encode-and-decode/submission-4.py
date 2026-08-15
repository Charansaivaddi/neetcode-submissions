class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        n = 0
        res_arr = []
        while n<len(s):
            j = n
            res = ""
            while s[j]!='#':
                j += 1
            l = int(s[n:j])
            for i in range(j+1, j+l+1):
                res += s[i]
            res_arr.append(res)
            n = j+l+1
        return res_arr
