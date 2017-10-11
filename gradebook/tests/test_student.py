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
