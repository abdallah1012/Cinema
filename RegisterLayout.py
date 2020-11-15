# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:10:37 2020

@author: warpeace101
"""

from PyQt5.QtWidgets import QGridLayout,QPushButton,QLineEdit,QLabel, QWidget, QStackedLayout, QRadioButton
from PyQt5.QtCore import pyqtSignal
from RegisterController import RegisterController



class RegisterLayout(QWidget):
    success_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("Username")
    
        self.firstName = QLineEdit()
        self.firstName.setPlaceholderText("First Name")
        
        self.lastName = QLineEdit()
        self.lastName.setPlaceholderText("Last Name")
        
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(lambda:self.SubmitUser())
        
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(lambda:self.BackEvent())
        
        self.std_rb = QRadioButton("Student")
        self.prf_rb = QRadioButton("Professor")
        
        self.error_message = QLabel("")
        
        self.grid = QGridLayout()
        self.grid.addWidget(self.username_entry,0,0)
        self.grid.addWidget(self.password,1,0)
        self.grid.addWidget(self.firstName,2,0)
        self.grid.addWidget(self.lastName,3,0)
        self.grid.addWidget(self.std_rb,4,0)
        self.grid.addWidget(self.prf_rb,4,1)
        self.grid.addWidget(self.submit_button,5,0)
        self.grid.addWidget(self.back_button,6,0)
        self.grid.addWidget(self.error_message,7,0)

        self.controller = RegisterController()
        
        self.setLayout(self.grid)
        
        self.show()
        
        
        self.success_signal.connect(lambda:self.cleanUp())
        
        
    def SubmitUser(self):
        user = ""
        if(self.std_rb.isChecked() == True):
            user = "student"
        elif(self.prf_rb.isChecked() == True):
            user = "professor"
        else:
            user = "error"
        
        username = self.username_entry.text()
        firstName = self.firstName.text()
        lastName = self.lastName.text()
        password = self.password.text()
        
        #Add extra security statements to ensure username is proper and only has letters
        exists = self.controller.CheckUserExists(username)
        
        if(exists == 1):
            self.error_message.setText("Choose another username")
            state = 0
        elif(user == "error"):
            self.error_message.setText("Choose a User Type")
            state = 0
        elif(username != "" and firstName != "" and lastName != "" and password != ""):
            state = self.controller.RegisterUser(username, firstName, lastName, password, user)
        else:
            self.error_message.setText("Fill all Fields")
            state = 0
        
        if(state == 1):
            self.error_message.setText("Success")
    
    
    def BackEvent(self):
        state = self.controller.goBack()
        if(state == "success"):
            self.success_signal.emit()
        
        
    def cleanUp(self):
        self.close()
        self.deleteLater()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        