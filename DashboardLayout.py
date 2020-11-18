# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:37 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QGridLayout,QWidget,QPushButton
from User import User
from DashboardController import DashboardController
from PyQt5.QtCore import pyqtSignal

class DashboardLayout(QWidget):
    load_course_request = pyqtSignal(str)
    new_course_request = pyqtSignal(str)
    def __init__(self,user:User):
        super().__init__()
        self.__dashboard_grid = QGridLayout()
        self.user = user
        self.exampleCourse = QPushButton("Example course")
        self.add_course = QPushButton("Add Course") #enroll for student, create for professor
        self.add_course.clicked.connect(lambda:self.new_course_request.emit(str(user.id)))
        self.__dashboard_grid.addWidget(self.add_course)
        
        self.courses = [self.exampleCourse] #courses will typically be clickable labels

        self.controller = DashboardController(self.user)
        #TODO: populate courses list from dashbaord controller result and display on GUI
        
        self.__dashboard_grid.addWidget(self.exampleCourse)
        
        self.setLayout(self.__dashboard_grid)
        
        if len(self.courses)!=0:
            for course in self.courses:
                course.clicked.connect(lambda:self.load_course_request.emit(course.text()))
        
        
         
        
            