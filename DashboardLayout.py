# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:37 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QGridLayout,QWidget,QPushButton, QLabel, QVBoxLayout, QInputDialog
from User import User
from DashboardController import DashboardController
from PyQt5.QtCore import pyqtSignal
from CourseInputDialog import CourseInputDialog
import re


class DashboardLayout(QWidget):  
    submitcourse_request = pyqtSignal()
    new_course_request = pyqtSignal()
    
    new_movie_request = pyqtSignal()
    submitmovie_request = pyqtSignal()
    def __init__(self,user:User):
        super().__init__()
        self.__dashboard_grid = QGridLayout()
        self.user = user
        
        #ADD COURSE GUI
        self.add_course = QPushButton("Add Course") #enroll for student, create for professor
        self.add_course.clicked.connect(lambda:self.new_course_request.emit())
        
  
        
        self.name = ""
        self.syllabus = ""
        
        self.exampleCourse = QPushButton("Example course")
        self.__dashboard_grid.addWidget(self.add_course,1,1)
       
       
        self.movieProperties = [] 
        
        #ADD MOVIE GUI
        
        self.add_movie = QPushButton("Add Movie")
        
       
        self.add_movie.clicked.connect(lambda:self.new_movie_request.emit())
        
        
        self.__dashboard_grid.addWidget(self.add_movie,2,1)
        

        
        
        self.courses = [self.exampleCourse] #courses will typically be clickable labels

        self.controller = DashboardController(self.user)

        
        self.__dashboard_grid.addWidget(self.exampleCourse,3,1)
        
        self.message = QLabel("")
        self.__dashboard_grid.addWidget(self.message,4,1)
        
        self.courseInput = None
        self.setLayout(self.__dashboard_grid)
        
        if len(self.courses)!=0:
            for course in self.courses:
                course.clicked.connect(lambda:self.load_course_request.emit(course.text()))
        
        
        
    
    def submitcourse(self):
        self.result = self.controller.addCourse(self.name, self.syllabus, self.user.id)
        

    
    def submitmovie(self):
        seg = re.split(" / ", self.name) #seg[0] is the course name, seg[1] is the movie name
        courseID = ""
        print(seg[0])
        for i in self.controller.courses:
            print(i[0])
            if (str(i[0]) == str(seg[0])):
                courseID = i[1]
                break
        #self.movieproperties index 0 is the url path and 1 is the thumbnail path
        self.result = self.controller.addMovie(seg[1], courseID,  self.syllabus, self.user.id, self.movieProperties[0], self.movieProperties[1])
        
       
        
  
        
            