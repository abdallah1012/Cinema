# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:10:37 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel
from PyQt5.QtCore import pyqtSignal
from SignInController import SignInController


class SignInLayout(QGridLayout):
    success_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        
        self.register_button = QPushButton("Register")
        self.sign_in_button = QPushButton("Sign In") 
        
        self.register_button.setGeometry(100, 100, 120, 40) 
        self.sign_in_button.setGeometry(100, 100, 120, 40) 
      
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("username")
    
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("password")
        self.password_entry.setEchoMode(QLineEdit.Password)
        
        self.error_message = QLabel("")
                 
        self.addWidget(self.username_entry)
        self.addWidget(self.password_entry)
        self.addWidget(self.sign_in_button)
        self.addWidget(self.register_button)
        self.addWidget(self.error_message)
    
        
        self.sign_in_button.clicked.connect(lambda: self.ClickSignInButton())
        self.register_button.clicked.connect(lambda: self.ClickRegisterButton())
        self.controller = SignInController()

    def ClickSignInButton(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        result = self.controller.AttemptSignIn(username,password)
        if result == "success":
            self.success_signal.emit()
        else:
            self.error_message.setText(result)
            
    def ClickRegisterButton(self):
       state = self.controller.ToRegister()
       if(state == "success"):
           self.success_signal.emit()
           
        
        
        
        