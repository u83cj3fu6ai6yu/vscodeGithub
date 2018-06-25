#!/usr/bin/env python
# -*- coding: utf-8 -*-

'main'

__author__ = 'Lucien'

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import logging

#from module1 import *
'''
# Q2
myPath = "C:\\Users\\Lucien\\Desktop\\VSC_Python"
module1.print_dir_contents(myPath)

# Q3
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1,2,3,4,5)))
if 'a' in A0:
    print('OK')

# 裝飾器
def use_logging(func):

    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    
    return wrapper

@use_logging
def foo():
    print('i am foo')

# foo = use_logging(foo) 因為有@語法糖
foo()                   # 执行foo()就相当于执行 wrapper()
'''

# class 教學
class Human(object):
    def __init__(self, h = 1, w = 1):
        self.height = h
        self.weight = w
    
    def BMI(self):
        return self.weight / ((self.height/100) ** 2)

class Woman(Human):
    def __init__(self, h, w, bust = 0, waist = 0, hip = 0):
        super().__init__(h, w)
        self.bust = bust
        self.waist = waist
        self.hip = hip
    
    def printBWH(self):
        print("bust = {}, waist = {}, hip = {}".format(self.bust, self.waist, self.hip))

a = Woman(171, 60, 100, 64, 84)
print(a.BMI())
a.printBWH()