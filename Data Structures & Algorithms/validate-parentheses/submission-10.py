class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {'(':')','{':'}','[':']'}
        new_stack = []
        counter = 0
        for string in s:
            if string == '(' or string == '{' or string == '[':
                new_stack.append(string)
                counter +=1
            else:
                if len(new_stack)>0 and par_dict.get(new_stack[-1])== string:
                    new_stack.pop()
                    counter -=1
                else:
                    return False
        return len(new_stack) == 0 and counter ==0