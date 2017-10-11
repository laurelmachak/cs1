class Student(object):
    ''' a student, takes first name & last
    name as args  '''
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.assignments = {}
    def full_name(self):
        ''' returns string of student's first and last name'''
        return ("{} {}").format(self.first, self.last)
    def get_assignment(self, assignment_id, assignment_grade):
        self.assignments[assignment_id] = [assignment_grade]


''' ___Tests___'''

'''
A001 = Student("Steve", "Buscemi")
print(A001.full_name())
print(A001.assignments)
A001.get_assignment("homework1", 97)
print(A001.assignments)
'''
