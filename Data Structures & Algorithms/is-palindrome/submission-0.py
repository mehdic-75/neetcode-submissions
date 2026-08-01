class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s2 == s2[::-1]
        