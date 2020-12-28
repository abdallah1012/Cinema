#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5.QtWidgets import QLabel,QWidget,QPushButton, QGridLayout, QLineEdit, QVBoxLayout
from User import User
from ChangePasswordController import ChangePasswordController
from PyQt5.QtCore import pyqtSignal


class ChangePasswordLayout(QWidget):
    goback_request = pyqtSignal(int)
    
    def __init__(self,user:User):
        self.user = user
        super().__init__()
        self.title="Change Password"
        self.__password_grid =  QGridLayout()
        self.controller = ChangePasswordController(self.user)
        
        self.previous_password= QLabel("Previous Password")
        self.new_password= QLabel("New Password")
        
        self.previous_password_edit= QLineEdit()
        self.new_password_edit= QLineEdit()
        
        self.back_button = QPushButton("Back")
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(lambda:self.BackEvent())
        
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(lambda:self.ConfirmEvent())
        self.confirm_button.setObjectName("confirm_button")
        self.change_result= QLabel("")
        
        self.__password_grid.addWidget(self.previous_password,0,0)
        self.__password_grid.addWidget(self.previous_password_edit,0,1)
        self.__password_grid.addWidget(self.new_password,1,0)
        self.__password_grid.addWidget(self.new_password_edit,1,1)
        self.__password_grid.addWidget(self.back_button,2,0)
        self.__password_grid.addWidget(self.confirm_button,2,1)
        
        
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.__password_grid)
        self.vbox.addWidget(self.change_result)
        
        
        
        self.setLayout(self.vbox)
        
        
        
        
    def BackEvent(self):
        self.goback_request.emit(0)
        
    def ConfirmEvent(self):
        result = self.controller.changePassword(self.previous_password_edit.text(), self.new_password_edit.text())
        
        if(result == 1):
            self.goback_request.emit(1)
#            self.change_result.setText("Success")
        elif(result == 2):
            self.change_result.setText("Wrong Old Password")
        elif(result == 3):
            self.change_result.setText("Database Error")
