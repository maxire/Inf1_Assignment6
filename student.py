from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        self.modules.append(title)
        self.grades[title] = title.get_grade()

    def get_list_modules(self):
        for each in self.modules:
            print("Modules of Student %s:\n" % self.name, each)

    def get_grades(self):
        for each in self.grades:
            print("Grades of Student %s:\n" % self.name, each,":", self.grades[each])

### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6