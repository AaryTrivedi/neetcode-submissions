class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsPtr = 0
        iterHasPop = False
        while True:
            if students[studentsPtr] == sandwiches[0]:
                students.pop(studentsPtr)
                sandwiches.pop(0)
                iterHasPop = True
            if len(students) == 0:
                break
            studentsPtr = (studentsPtr + 1) % len(students)
            if studentsPtr == 0:
                if iterHasPop == True:
                    iterHasPop = False
                else:
                    break
        return len(students)