#!/usr/bin/env python
# File name: class_init.py
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name
p = Person('James')
p.say_hi()

