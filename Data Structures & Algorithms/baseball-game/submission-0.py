class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_lst = []
        for ops in operations:
            if ops == '+':
                new_lst.append(int(new_lst[-2])+int(new_lst[-1]))
                print(new_lst)
            elif ops == 'C':
                new_lst.pop()
            elif ops == 'D':
                new_lst.append(int(new_lst[-1])*2)
            else:
                new_lst.append(int(ops))        
        return sum(new_lst)