class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dict_students = {0:students.count(0),1:students.count(1)}
        for sandwich in sandwiches:
            if dict_students[sandwich] >0:
                dict_students[sandwich]-=1
            else:
                return dict_students[0]+dict_students[1]
        return 0

