# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:37 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QGridLayout,QWidget,QPushButton, QLabel, QVBoxLayout
from User import User
from DashboardController import DashboardController
from PyQt5.QtCore import pyqtSignal
from CourseInputDialog import CourseInputDialog


class DashboardLayout(QWidget):  
    submitcourse_request = pyqtSignal()
    new_course_request = pyqtSignal()
    
    def __init__(self,user:User):
        super().__init__()
        self.__dashboard_grid = QGridLayout()
        self.user = user
        
        #ADD COURSE GUI
        self.add_course = QPushButton("Add Course") #enroll for student, create for professor
        self.add_course.clicked.connect(lambda:self.new_course_request.emit())
        self.addCoursename = QLabel("")
        self.addCourseSyllabus = QLabel("")
        
        
        
        self.infoShown = QVBoxLayout()
        self.infoShown.addWidget(self.addCoursename)
        self.infoShown.addWidget(self.addCourseSyllabus)
        
        
        self.name = ""
        self.syllabus = ""
        
        self.exampleCourse = QPushButton("Example course")
        self.__dashboard_grid.addWidget(self.add_course,1,1)
        self.__dashboard_grid.addLayout(self.infoShown,2, 1)
       
        
        
        self.courses = [self.exampleCourse] #courses will typically be clickable labels

        self.controller = DashboardController(self.user)
        #TODO: populate courses list from dashbaord controller result and display on GUI
        
        self.__dashboard_grid.addWidget(self.exampleCourse,3,1)
        self.courseInput = None
        self.setLayout(self.__dashboard_grid)
        
        if len(self.courses)!=0:
            for course in self.courses:
                course.clicked.connect(lambda:self.load_course_request.emit(course.text()))
        
        
        
    def AddCourse(self, userID):        
        self.courseInput = CourseInputDialog()
        self.courseInput.show()
        self.courseInput.done.clicked.connect(lambda:self.take_input())
        
#        self.controller.addCourse()
    

    
    def submitcourse(self):
        self.result = self.controller.addCourse(self.name, self.syllabus, self.user.id)
        
       
        
  
        
            