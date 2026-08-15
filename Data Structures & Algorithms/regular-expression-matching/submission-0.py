class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(p), len(s)
        def recMatch(i, j):
            if j==n:
                return i==m
            match = i<m and (s[i]==p[j] or p[j]==".")
            if (j+1)<n and p[j+1]=="*":
                return recMatch(i, j+2) or (match and recMatch(i+1, j))
            if match:
                return recMatch(i+1, j+1)
            return False
        return recMatch(0, 0)