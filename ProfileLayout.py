# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:30 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QWidget,QLabel, QPushButton, QSpacerItem, QFileDialog
from PyQt5.QtGui import QPixmap
from User import User
from ProfileController import ProfileController


#Layout for the profile interface
#TODO: show relevant details for the user
class ProfileLayout(QWidget):
    def __init__(self,user:User):
        super().__init__()
        self.title = 'User Profile'
        
        self.__profile_grid = QGridLayout()
        self.user = user
        self.controller = ProfileController(self.user)
        
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(lambda:self.BackEvent())
        
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(lambda:self.getFile())
        
        self.change_password = QPushButton("Change Password")
        self.change_password.clicked.connect(lambda:self.changePassword())
        
        self.username = QLabel()
        self.username.setPlaceholderText("Username")
    
        self.firstName = QLabel()
        self.firstName.setPlaceholderText("First Name")
        
        self.lastName = QLabel()
        self.lastName.setPlaceholderText("Last Name")
        
        self.user_username = QLabel()
        self.username.setPlaceholderText(self.user.username)
    
        self.user_firstName = QLabel()
        self.firstName.setPlaceholderText(self.user.first_name)
        
        self.user_lastName = QLabel()
        self.lastName.setPlaceholderText(self.user.last_name)
        
        self.image = QPixmap("./image.jpg")
        self.image_label = QLabel()
        self.image_label.setPixmap(self.image)
        self.image_label.resize(5,5);
        
        self.spacer= QSpacerItem(20,5)
        
        self.__profile_grid.addWidget(self.back_button,0,0)
        self.__profile_grid.addWidget(self.spacer,0,1)
        self.__profile_grid.addWidget(self.image_label,1,0)
        self.__profile_grid.addWidget(self.edit_button,1,1)
        self.__profile_grid.addWidget(self.username,2,0)
        self.__profile_grid.addWidget(self.user_username,2,1)
        self.__profile_grid.addWidget(self.firstName,3,0)
        self.__profile_grid.addWidget(self.user_firstName,3,1)
        self.__profile_grid.addWidget(self.lastName,4,0)
        self.__profile_grid.addWidget(self.user_lastName,4,1)
        self.__profile_grid.addWidget(self.change_password,5,0)
        
        
    
        self.setLayout(self.__profile_grid)
        
    def BackEvent(self):
        self.controller.goBack()
        
    def getFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        self.image_label.setPixmap(QPixmap(fname))
        self.controller.editProfilePic(fname)
        
    def changePassword(self):
        self.controller.changePassword()
        
        