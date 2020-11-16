# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:02:46 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QStackedLayout
from User import User
from HomeLayout import HomeLayout
from DashboardLayout import DashboardLayout
from ProfileLayout import ProfileLayout
from CourseLayout import CourseLayout

class MainWidget(QWidget):
    
    def __init__(self, user:User):
        super().__init__()
        self.setMinimumSize(500,500)
        self.user = user
        
        self.dashboard_button = QPushButton("Dashboard")
        self.dashboard_button.clicked.connect(lambda:self.LoadDashboardLayout())
        
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(lambda:self.LoadHomeLayout())
        
        self.profile_button = QPushButton("Profile")
        self.profile_button.clicked.connect(lambda:self.LoadProfileLayout())
        
        # self.load_course.connect(lambda: self.LoadCourseLayout())
        
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.dashboard_button)
        self.grid.addWidget(self.home_button)
        self.grid.addWidget(self.profile_button)
    
        self.home_layout = None
        self.dashboard_layout = None
        self.profile_layout = None
        self.course_layout = None
        # self.search_layout = None
        
        self.stack = QStackedLayout()
        
        self.grid.addLayout(self.stack,4,1)
        
        self.setLayout(self.grid)
        self.LoadHomeLayout()
        self.show()
    
    def LoadHomeLayout(self):
        self.setWindowTitle("Home")
        if self.home_layout == None:
            self.home_layout = HomeLayout(self.user)
            self.stack.addWidget(self.home_layout)
        self.stack.setCurrentWidget(self.home_layout)
        
    def LoadDashboardLayout(self):
        self.setWindowTitle("Dashboard")
        if self.dashboard_layout == None:
            self.dashboard_layout = DashboardLayout(self.user)
            self.dashboard_layout.load_course_request.connect(self.LoadCourseLayout)
            self.stack.addWidget(self.dashboard_layout)
        self.stack.setCurrentWidget(self.dashboard_layout)
        
    def LoadProfileLayout(self):
        self.setWindowTitle("Profile")
        if self.profile_layout == None:
            self.profile_layout = ProfileLayout(self.user)
            self.stack.addWidget(self.profile_layout)
        self.stack.setCurrentWidget(self.profile_layout)

    def LoadCourseLayout(self,course_id):
        self.setWindowTitle("Course")
        if self.course_layout!=None:
            self.stack.removeWidget(self.course_layout)
            del self.course_layout
            
        self.course_layout = CourseLayout(course_id)
        self.stack.addWidget(self.course_layout)
        self.stack.setCurrentWidget(self.course_layout)


        # print(course_id)
        
       
        
        
        
        
        