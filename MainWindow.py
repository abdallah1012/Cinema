# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:02:46 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QWidget,QGridLayout,QPushButton,QLabel
from User import User

class MainWindow(QWidget):
    def __init__(self, user:User):
        super().__init__()
        self.user_ = user
        self.grid_ = QGridLayout()
        
        self.dashboard_button_ = QPushButton("Dashboard")
        self.dashboard_button_.clicked.connect(lambda:self.DashboardTab())
        
        self.home_button_ = QPushButton("Home")
        self.home_button_.clicked.connect(lambda:self.HomeTab())

        self.grid_.addWidget(self.dashboard_button_)
        self.grid_.addWidget(self.home_button_)

        self.temp_label_ = QLabel("")

        self.setLayout(self.grid_)

        self.HomeTab()
        self.show()
        
            
    def HomeTab(self):
        self.setWindowTitle('Main Window')
        self.CLearGrid()    
        self.temp_label_.setText("Home tab clicked")
        self.grid_.addWidget(self.temp_label_)
   
    def DashboardTab(self):
       #Communicate with controller
        self.user_.LoadDashboardInfo()
        self.setWindowTitle('Dashboard')
        self.CLearGrid()
        self.temp_label_.setText("Dashboard tab clicked")
        self.grid_.addWidget(self.temp_label_)
        
    def CLearGrid(self):
        for i in reversed (range(self.grid_.count())):
            if i<=1:
                continue
            #self.grid_.itemAt(i).widget()()
            self.grid_.takeAt(i)
        
        
        
        
        
        