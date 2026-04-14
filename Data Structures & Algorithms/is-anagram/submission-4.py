class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_lst = list(t)
        s_lst = list(s)
        for char in t:
            if char in s_lst:
                s_lst.pop(s_lst.index(char))
            else:
                return False
        if len(s_lst) == 0:
            return True
        else:
            return False
    