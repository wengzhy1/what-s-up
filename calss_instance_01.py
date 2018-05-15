#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.print_score(), lisa.get_grade(), '\n')
print(bart.print_score(), bart.get_grade(), '\n')
print(lisa.name, lisa.get_grade(), '\n')
print(bart.name, bart.get_grade(), '\n')
print(lisa.name, lisa.print_score(), lisa.get_grade(), '\n')
print(bart.name, bart.print_score(), bart.get_grade(), '\n')
