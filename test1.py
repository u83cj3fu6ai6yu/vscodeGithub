#!/usr/bin/env python
# -*- coding: utf-8 -*-

'main'

__author__ = 'Lucien'

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import logging



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