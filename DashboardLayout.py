# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:37 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QGridLayout,QWidget,QPushButton, QLabel, QVBoxLayout, QInputDialog,QListWidget,QListView,QListWidgetItem
from User import User
from PyQt5.QtGui import QIcon, QPixmap
from DashboardController import DashboardController
from PyQt5.QtCore import pyqtSignal, QSize
from CourseInputDialog import CourseInputDialog
import re
from ClickableThumbnail import ClickableThumbnail

#layout that with course/movie upload and course enrollment and movie browsing interface
#functionality of this layout depends on the user's entity which is the type of user passed by parameter
class DashboardLayout(QWidget):  
    submitcourse_request = pyqtSignal()
    new_course_request = pyqtSignal()
    openCourse_request = pyqtSignal(int)
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
        

        self.__dashboard_grid.addWidget(self.add_course,1,1)
       
       
        self.movieProperties = [] 
        
        #ADD MOVIE GUI
        
        #self.add_movie = QPushButton("Add Movie")
        
       
        #self.add_movie.clicked.connect(lambda:self.new_movie_request.emit())
        
        
        #
        self.list_widget = QListWidget()
        
#        self.list_widget.setFlow(QListView.LeftToRight) 
        self.list_widget.setIconSize(QSize(190, 190))
        self.list_widget.hasAutoScroll()
        
        self.list_widget.setAutoFillBackground( False )
        self.items_title = self.user.courses
        self.items = []
        for i in range(len(self.items_title)):
                self.items.append(ClickableThumbnail(self.items_title[i][1]))
                self.items[i].setText((self.items_title[i][0]))
                self.list_widget.addItem(self.items[i])
                
        


        self.controller = DashboardController(self.user)

        
        self.__dashboard_grid.addWidget(self.list_widget,2,1)
        
        self.message = QLabel("")
        self.__dashboard_grid.addWidget(self.message,3,1)
        
        self.courseInput = None
        self.setLayout(self.__dashboard_grid)
        
        self.list_widget.itemPressed.connect(lambda: self.CourseIsClicked())
       
#        if len(self.courses)!=0:
#            for course in self.courses:
#                course.clicked.connect(lambda:self.load_course_request.emit(course.text()))
        
        
        
    #contacts controller to submit course, currently is professor's course upload feature
    def submitcourse(self):
        self.result = self.controller.addCourse(self.name, self.syllabus, self.user.id)
        

    #contacts controller to submit movie under name of of course, currently is for professor's movie upload feature
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
        
       
    def CourseIsClicked(self):
#         self._WatchMovie_.emit(self.recommended_display.list_widget.selectedItems()[0].url)
        self.openCourse_request.emit(self.list_widget.selectedItems()[0].url)
        
  
        
            