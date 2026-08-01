class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s2 = sorted(list(s))
            t2 = sorted(list(t))
            return s2 == t2