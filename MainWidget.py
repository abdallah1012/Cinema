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
from CourseLayout import CourseLayout
from NewCourseLayout import NewCourseLayout
from MovieLayout import MovieLayout


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
    
    def LoadHomeLayout(self):
        self.setWindowTitle("Home")
        if self.home_layout == None:
            self.home_layout = HomeLayout(self.user)
            self.home_layout._WatchMovie_.connect(lambda:self.LoadMovieLayout())
            self.stack.addWidget(self.home_layout)
        self.stack.setCurrentWidget(self.home_layout)
        
    def LoadDashboardLayout(self):
        self.setWindowTitle("Dashboard")
        if self.dashboard_layout == None:
            self.dashboard_layout = DashboardLayout(self.user)
            self.dashboard_layout.load_course_request.connect(self.LoadCourseLayout)
            self.dashboard_layout.new_course_request.connect(self.LoadNewCourseLayout)
            self.stack.addWidget(self.dashboard_layout)
        self.stack.setCurrentWidget(self.dashboard_layout)
        self.silence()
        
    def LoadProfileLayout(self):
        self.setWindowTitle("Profile")
        if self.profile_layout == None:
            self.profile_layout = ProfileLayout(self.user)
            self.stack.addWidget(self.profile_layout)
        self.stack.setCurrentWidget(self.profile_layout)
        self.silence()

    def LoadCourseLayout(self,course_id):
        self.setWindowTitle("Course")
        if self.course_layout!=None:
            self.stack.removeWidget(self.course_layout)
            del self.course_layout
            
        self.course_layout = CourseLayout(course_id)
        self.stack.addWidget(self.course_layout)
        self.stack.setCurrentWidget(self.course_layout)  
    
    def LoadNewCourseLayout(self,user_id):
        self.setWindowTitle("New Course")
        if self.new_course_layout!=None:
            self.stack.removeWidget(self.new_course_layout)
            del self.add_course_layout
            
        self.new_course_layout = NewCourseLayout(user_id)
        self.stack.addWidget(self.new_course_layout)
        self.stack.setCurrentWidget(self.new_course_layout)  
        
    def LoadMovieLayout(self):
        self.setWindowTitle("Movie")
        if self.movie_layout!=None:
            self.stack.removeWidget(self.movie_layout)
            del self.movie_layout
            
        self.movie_layout = MovieLayout()
        self.stack.addWidget(self.movie_layout)
        self.stack.setCurrentWidget(self.movie_layout)  
        
    def silence(self):
        self.movie_layout.Stop()
        
        