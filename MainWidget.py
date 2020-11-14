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
        self.user_ = user
        
        self.dashboard_button = QPushButton("Dashboard")
        self.dashboard_button.clicked.connect(lambda:self.LoadDashboardLayout())
        
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(lambda:self.LoadHomeLayout())
        
        self.profile_button = QPushButton("Profile")
        self.profile_button.clicked.connect(lambda:self.LoadProfileLayout())
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.dashboard_button)
        self.grid.addWidget(self.home_button)
        self.grid.addWidget(self.profile_button)
    
        self.home_layout = HomeLayout()
        self.dashboard_layout = DashboardLayout()
        self.profile_layout = ProfileLayout()
        
        self.stack = QStackedLayout()
        self.stack.addWidget(self.home_layout)
        self.stack.addWidget(self.dashboard_layout)
        self.stack.addWidget(self.profile_layout)
        
        self.grid.addLayout(self.stack,4,1)
        
        self.setLayout(self.grid)
        
        self.show()
    
    def LoadHomeLayout(self):
        self.stack.setCurrentIndex(0)
        
    def LoadDashboardLayout(self):
        self.stack.setCurrentIndex(1)
        
    def LoadProfileLayout(self):
        self.stack.setCurrentIndex(2)

    
    def ClearGrid(self):
        for i in range(self.stack.count()):
            if self.stack.widget(i).isVisible():
                self.stack.widget(i).hide()
        
       
        
        
        
        
        