# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:40 2020

@author: ojaro
"""
from User import User


class Student(User):
    def __init__(self,ID:int):
        super().__init__()
    def LoadDashboardInfo(self):
        print("Student views dashboard")