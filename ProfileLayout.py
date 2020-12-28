# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:30 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QWidget,QLabel, QPushButton, QSpacerItem, QFileDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from User import User
from ProfileController import ProfileController
import base64
from PyQt5.QtCore import pyqtSignal 
#Layout for the profile interface
#TODO: show relevant details for the user
class ProfileLayout(QWidget):
    changePass_request = pyqtSignal()
    changeImage_request = pyqtSignal(bytes)
    def __init__(self,user:User):
        super().__init__()
        self.title = 'User Profile'
        
        self.__profile_grid = QGridLayout()
        self.user = user
        self.controller = ProfileController(self.user)
        
        
        
        self.edit_button = QPushButton("Edit")
        self.edit_button.setObjectName("edit_button")
        self.edit_button.setFixedWidth(100)
        self.edit_button.clicked.connect(lambda:self.getFile())
        
        self.change_password = QPushButton("Change Password")
        self.change_password.setObjectName("change_password")
        self.change_password.setFixedWidth(200)
        self.change_password.clicked.connect(lambda:self.changePassword())
        
        self.username = QLabel("Username")
        self.firstName = QLabel("First Name")
        self.lastName = QLabel("Last Name")     
        self.user_username = QLabel(self.user.username)   
        self.user_firstName = QLabel(self.user.first_name)     
        self.user_lastName = QLabel(self.user.last_name)
       
        self.image = self.user.image
        self.image_label = QLabel()
       
        if(len(self.image) != 0):
            pm = QPixmap()
            pm.loadFromData(base64.b64decode(self.user.image))
            self.image_label.setPixmap(pm)
            self.image_label.setScaledContents(True);
        
        self.spacer= QSpacerItem(20,5)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.image_label)
        
        self.__profile_grid.addWidget(self.username,2,0)
        self.__profile_grid.addWidget(self.user_username,2,1)
        self.__profile_grid.addWidget(self.firstName,3,0)
        self.__profile_grid.addWidget(self.user_firstName,3,1)
        self.__profile_grid.addWidget(self.lastName,4,0)
        self.__profile_grid.addWidget(self.user_lastName,4,1)
      
        self.vbox.addWidget(self.edit_button)
        self.vbox.addLayout(self.__profile_grid)
        self.vbox.addWidget(self.change_password)
        
        
        self.errorMessage = QLabel()
        self.vbox.addWidget(self.errorMessage)
        
        self.setLayout(self.vbox)
        

        
    def getFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.png *.jpg *.gif )")
        self.image_label.setPixmap(QPixmap(fname[0]))
        result, image = self.controller.editProfilePic(fname[0])
        self.changeImage_request.emit(image)
        
    def changePassword(self):
        self.changePass_request.emit()
#        self.controller.changePassword()
        
        