#!/usr/bin/python
# coding: UTF-8
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total E %d" % Employee.empCount

    def displayEmployee(self):
        print "Nanme: ", self.name, ",Salary:", self.salary


e1 = Employee("wfm", 100)
e2 = Employee("dd", 200)
e1.displayEmployee()
e1.displayEmployee()
print "Total Employee %d" % Employee.empCount
