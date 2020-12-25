#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 14:05:53 2020

@author: bbaajour
"""

from PyQt5.QtWidgets import QLabel,QWidget,QPushButton, QGridLayout, QLineEdit
from User import User
from ChangePasswordController import ChangePasswordController

class ChangePasswordLayout(QWidget):
    def __init__(self,user:User):
        self.user = user
        super().__init__()
        self.title="Change Password"
        self.__password_grid =  QGridLayout()
        self.controller = ChangePasswordController(self.user)
        
        self.previous_password= QLabel("Previous Password")
        self.new_password= QLabel("New Password")
        
        self.previous_password_edit= QLineEdit
        self.new_password_edit= QLineEdit
        
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(lambda:self.BackEvent())
        
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(lambda:self.ConfirmEvent())
        
        self.change_result= QLabel("")
        
        self.__password_grid.addWidget(self.previous_password,0,0)
        self.__password_grid.addWidget(self.previous_password_edit,0,1)
        self.__password_grid.addWidget(self.new_password,1,0)
        self.__password_grid.addWidget(self.new_password_edit,1,1)
        self.__password_grid.addWidget(self.back_button,2,0)
        self.__password_grid.addWidget(self.confirm_button,2,1)
        
        self.setLayout(self.__profile_grid)
        
        
        
        
    def BackEvent(self):
        self.controller.goBack()
        
    def ConfirmEvent(self):
        self.change_result.setPlaceholderText(self.controller.changePassword(self.previous_password_edit.text(), self.new_password_edit.text()))
