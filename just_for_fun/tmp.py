#!/usr/bin/env python3
#! -*- utf-8 -*-

class Dog(object):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def bark(self):
        print(self.get_name() + "is sb")
