# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:24:46 2020

@author: ojaro
"""

from PyQt5.QtWidgets import QPushButton,QLineEdit,QGridLayout,QWidget,QLabel
from User import User


class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sign_in_button = QPushButton("Sign In", self) 
        self.sign_in_button.setGeometry(100, 100, 120, 40) 
      
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("username")
    
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("password")
        self.password_entry.setEchoMode(QLineEdit.Password)
        
        self.error_message = QLabel("")
                 
        self.grid = QGridLayout()
        self.grid.addWidget(self.username_entry)
        self.grid.addWidget(self.password_entry)
        self.grid.addWidget(self.sign_in_button)
        self.grid.addWidget(self.error_message)
    
        self.setLayout(self.grid)
        self.sign_in_button.clicked.connect(lambda: self.ClickSignInButton())
        
        self.main_window = QWidget()
    
    def ClickSignInButton(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        result = User.AttemptSignIn(username,password)
        if result == "success":
            self.close()
            del self
        else:
            self.error_message.setText(result[0])
            
            


            
        
        
    