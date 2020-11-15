# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:37 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QGridLayout,QWidget
from User import User
from Student import Student
from DashboardController import DashboardController

class DashboardLayout(QWidget):
    def __init__(self,user:User):
        super().__init__()
        self.__dashboard_grid = QGridLayout()
        self.user = user
        if type(self.user) == Student:
            print("Student dashboard")
        self.controller = DashboardController(self.user)
        self.setLayout(self.__dashboard_grid)
        
        
         
        
            