# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:02:46 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QStackedLayout, QHBoxLayout, QFrame, QMainWindow, QAction, QMessageBox
from User import User
from HomeLayout import HomeLayout
from DashboardLayout import DashboardLayout
from ProfileLayout import ProfileLayout
from MovieLayout import MovieLayout
from CourseInputDialog import CourseInputDialog
from MovieInputDialog import MovieInputDialog

class MainWidget(QMainWindow):
    
    def __init__(self, user:User):
        super().__init__()
        
        self.mainWidget = QWidget()
        
        self.setMinimumSize(500,500)
        self.user = user
        self.setStyleSheet(open('main.css').read())
        self.dashboard_button = QPushButton("Dashboard")
        self.dashboard_button.clicked.connect(lambda:self.LoadDashboardLayout())
        
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(lambda:self.LoadHomeLayout())
        
        self.profile_button = QPushButton("Profile")
        self.profile_button.clicked.connect(lambda:self.LoadProfileLayout())
                
        
        self.grid = QGridLayout()

    
        self.upperLayout = QHBoxLayout()
        
        self.upperLayout.addWidget(self.dashboard_button)
        self.upperLayout.addWidget(self.home_button)
        self.upperLayout.addWidget(self.profile_button)
        
        self.upperExternal = QFrame()
        self.upperExternal.setStyleSheet(".QFrame{background-color: white; border: 2px solid black; border-radius: 10px;}");
    
        self.upperExternal.setLayout(self.upperLayout)
        
        
       
        self.home_layout = None
        self.dashboard_layout = None
        self.profile_layout = None
        self.course_layout = None
        self.new_course_layout = None
        self.movie_layout = None
        
        self.stack = QStackedLayout()
        
        self.grid.addWidget(self.upperExternal,1,1)
        self.grid.addLayout(self.stack,2,1)
        
        self.mainWidget.setLayout(self.grid)
        self.setCentralWidget(self.mainWidget)
        self.LoadHomeLayout()
        
        
        exit = QAction("&Exit", self)
        exit.triggered.connect(self.closeEvent)
        
        
        self.show()
    
    def closeEvent(self, event):
        
        self.silence()
        close = QMessageBox()
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        
        if close == QMessageBox.Yes:        
            event.accept()
        else:
            event.ignore()
    
    
    #HomeLayoout
    def LoadHomeLayout(self):
        self.setWindowTitle("Home")
        if self.home_layout == None:
            self.home_layout = HomeLayout(self.user)
            self.home_layout._WatchMovie_.connect(lambda:self.LoadMovieLayout())
            self.stack.addWidget(self.home_layout)
        self.stack.setCurrentWidget(self.home_layout)
        
    def LoadMovieLayout(self):
        self.setWindowTitle("Movie")
        if self.movie_layout!=None:
            self.stack.removeWidget(self.movie_layout)
            del self.movie_layout
            
        self.movie_layout = MovieLayout()
        self.stack.addWidget(self.movie_layout)
        self.stack.setCurrentWidget(self.movie_layout) 
 
    
    
    

    #DashBoardLayout       
    def LoadDashboardLayout(self):
        self.setWindowTitle("Dashboard")
        if self.dashboard_layout == None:
            self.dashboard_layout = DashboardLayout(self.user)
            self.dashboard_layout.submitcourse_request.connect(self.submitCourse)
            self.dashboard_layout.new_course_request.connect(self.LoadCourseLayout)
            self.dashboard_layout.new_movie_request.connect(self.LoadDashMovieLayout)
            self.dashboard_layout.submitmovie_request.connect(self.submitMovie)
            
            self.stack.addWidget(self.dashboard_layout)
        self.stack.setCurrentWidget(self.dashboard_layout)
        self.silence()
        
    def LoadCourseLayout(self):
        self.courseInput = CourseInputDialog()
        self.courseInput.show()
        self.courseInput.done.clicked.connect(lambda:self.take_input())
        
    def take_input(self):
        self.dashboard_layout.name = self.courseInput.le1.text()
        self.dashboard_layout.syllabus = self.courseInput.le2.text()
        self.dashboard_layout.addCoursename.setText("Course Name: " + self.courseInput.le1.text())
        self.dashboard_layout.addCourseSyllabus.setText("Description: " + self.courseInput.le2.text())
        self.courseInput.close()
        self.courseInput.deleteLater()
        self.dashboard_layout.Submit = QPushButton("Submit")
        self.dashboard_layout.infoShown.addWidget(self.dashboard_layout.Submit)
        self.dashboard_layout.Submit.clicked.connect(lambda:self.dashboard_layout.submitcourse())
        self.dashboard_layout.Submit.clicked.connect(lambda:self.dashboard_layout.submitcourse_request.emit())
    
    def submitMovie(self):
        result = self.dashboard_layout.result
        self.dashboard_layout.Submit.hide()
        self.dashboard_layout.addMovieDesc.setText("")
        self.dashboard_layout.addMoviePath.setText("")
        if(result == 1):
            self.dashboard_layout.addMovieName.setText("Course Added Successfully")
        elif(result == 0):
            self.dashboard_layout.addMovieName.setText("Database Error")
        elif(result == 2):
            self.dashboard_layout.addMovieName.setText("Course Already Added Before")
        elif(result == 3):
            self.dashboard_layout.addMovieName.setText("Youtube Error")
        else:
            self.dashboard_layout.addMovieName.setText("Unknown Error") 


    def submitCourse(self):
        result = self.dashboard_layout.result
        self.dashboard_layout.Submit.hide()
        self.dashboard_layout.addCourseSyllabus.setText("")
        if(result == 1):
            self.dashboard_layout.addCoursename.setText("Course Added Successfully")
        elif(result == 0):
            self.dashboard_layout.addCoursename.setText("Database Error")
        elif(result == 2):
            self.dashboard_layout.addCoursename.setText("Course Already Added Before")
        elif(result == 3):
            self.dashboard_layout.addCoursename.setText("Youtube Error")
        else:
            self.dashboard_layout.addCoursename.setText("Unknown Error") 

    
    def LoadDashMovieLayout(self):
        self.movieInput = MovieInputDialog(self.dashboard_layout.controller.courses)
        self.movieInput.show()
        self.movieInput.done.clicked.connect(lambda:self.take_input_movie())
    
    
    def take_input_movie(self):
        self.dashboard_layout.name = self.movieInput.le.text() + " / " + self.movieInput.le1.text()
        self.dashboard_layout.syllabus = self.movieInput.le2.text()    
        self.dashboard_layout.movieProperties = [] #reset it
        self.dashboard_layout.movieProperties.append(self.movieInput.movieLabel.text())
        self.dashboard_layout.movieProperties.append(self.movieInput.thumbLabel.text())
        self.dashboard_layout.addMovieName.setText("Movie/Course Name: " + self.dashboard_layout.name)
        self.dashboard_layout.addMovieDesc.setText("Description: " + self.movieInput.le2.text())
        self.dashboard_layout.addMoviePath.setText("Movie Path: " + self.movieInput.movieLabel.text())
        self.movieInput.close()
        self.movieInput.deleteLater()
        self.dashboard_layout.Submit = QPushButton("Submit")
        self.dashboard_layout.movieInfoShown.addWidget(self.dashboard_layout.Submit)
        self.dashboard_layout.Submit.clicked.connect(lambda:self.dashboard_layout.submitmovie())
        self.dashboard_layout.Submit.clicked.connect(lambda:self.dashboard_layout.submitmovie_request.emit())

    #ProfileLayout
    def LoadProfileLayout(self):
        self.setWindowTitle("Profile")
        if self.profile_layout == None:
            self.profile_layout = ProfileLayout(self.user)
            self.stack.addWidget(self.profile_layout)
        self.stack.setCurrentWidget(self.profile_layout)
        self.silence()

    
 
        
     
    

    
    def silence(self):
        if(self.movie_layout != None):
            self.movie_layout.Stop()
        

        