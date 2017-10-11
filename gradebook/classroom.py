#import student

class Classroom(object):
    ''' an classroom '''

    def __init__(self, course_name):
        self.course_name = course_name
        self.roster = {}
        self.course_work = []

    def assign_work(self, assignment_id):
        ''' takes string of assignment name '''
        self.assignment_id = assignment_id
        self.course_work.append(assignment_id)
        return

    def add_students(self, list_of_students):
        ''' add a student to roster with
        array of student objects as arg
        key: generated student id (string), and
        value: an instance of a student'''
        for student_object in list_of_students:
            student_id = str(len(self.roster))
            self.roster[student_id] = student_object



    '''
    def assign_to_class(self, assignment_name):
        students = self.roster.values()
        for student in students:
            student.assignments[assignment_name] = 100
    '''


''' ___Tests___ '''

'''
new_classroom = Classroom("AP_English")
print(len(new_classroom.roster))
new_classroom.add_students(["placeholder"])
new_classroom.add_students(["another one"])
new_classroom.add_students(["third", "fourth"])
print(new_classroom.roster)
print(len(new_classroom.roster))
'''
