class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_set = set(t)
        s_set = set(s)
        if len(s) != len(t):
            return False
        for letter in t_set:
            if t.count(letter) != s.count(letter):
                return False
        return True

        