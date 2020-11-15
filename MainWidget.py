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

class MainWidget(QWidget):
    def __init__(self, user:User):
        super().__init__()
        self.setMinimumSize(500,500)
        self.user = user
        
        self.dashboard_button = QPushButton("Dashboard")
        self.dashboard_button.clicked.connect(lambda:self.ClickDashboardButton())
        
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(lambda:self.ClickHomeButton())
        
        self.profile_button = QPushButton("Profile")
        self.profile_button.clicked.connect(lambda:self.ClickProfileButton())
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.dashboard_button)
        self.grid.addWidget(self.home_button)
        self.grid.addWidget(self.profile_button)
    
        self.home_layout = None
        self.dashboard_layout = None
        self.profile_layout = None
        
        self.stack = QStackedLayout()
        self.stack.addWidget(self.dashboard_layout)
        self.stack.addWidget(self.profile_layout)
        
        self.grid.addLayout(self.stack,4,1)
        
        self.setLayout(self.grid)
        self.LoadHomeLayout()
        self.show()
    
    def ClickHomeButton(self):
        self.setWindowTitle("Home")
        if self.home_layout == None:
            self.stack.addWidget(self.home_layout)
            self.home_layout = HomeLayout(self.user)
        self.stack.setCurrentWidget(self.home_layout)
        
    def ClickDashboardButton(self):
        self.setWindowTitle("Dashboard")
        if self.dashboard_layout == None:
            self.dashboard_layout = DashboardLayout(self.user)
            self.stack.addWidget(self.dashboard_layout)
        self.stack.setCurrentWidget(self.dashboard_layout)
        
    def ClickProfileButton(self):
        self.setWindowTitle("Profile")
        if self.profile_layout == None:
            self.profile_layout = ProfileLayout()
            self.stack.addWidget(self.profile_layout)
        self.stack.setCurrentWidget(self.profile_layout)

    
    # def ClearGrid(self):
    #     for i in range(self.stack.count()):
    #         if self.stack.widget(i).isVisible():
    #             self.stack.widget(i).hide()
        
       
        
        
        
        
        