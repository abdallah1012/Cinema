# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 12:02:11 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout
from abc import ABCMeta,abstractmethod

class MainLayout(QWidget,metaclass=ABCMeta):
    def __init__(self,user_id:int):
        self.user_id = user_id
        
        self.dashboard_button = QPushButton("Dashboard")
        self.dashboard_button.clicked.connect(lambda:self.ClickDashboardButton())
        
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(lambda:self.ClickHomeButton())
        
        self.profile_button = QPushButton("Profile")
        self.profile_button.clicked.connect(lambda:self.ClickProfileButton())
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
    @abstractmethod
    def ClickHomeButton(self):
        pass
    
    @abstractmethod    
    def ClickDashboardButton(self):
       pass
    
    @abstractmethod    
    def ClickProfileButton(self):
        pass