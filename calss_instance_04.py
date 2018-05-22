#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1、python支持动态给类和实例增加属性和方法；
# 2、python __slots__只能限制实例的属性及方法，对于类则没有影响，对于子类则更是没有限制。

class Student(object):
    __slots__ = ('name', 'age', 'set_age', 'score')
    pass

s = Student()

#动态给实例增加属性
s.name = 'Michael'
print(s.name)

#动态给实例增加方法和属性
def  set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

#动态给类增加属性
Student.gender = 'male'
print(Student.gender)
print(s.gender)

#动态给类增加方法和属性
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(66)
print(s.score)
