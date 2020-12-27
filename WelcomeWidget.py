# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:24:46 2020

@author: ojaro
"""


from PyQt5.QtWidgets import QWidget
from SignInLayout import SignInLayout

#This is the first widget that gets instantiated, it is responsible for setting up the SignInLayout
class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.sign_in_layout = SignInLayout()
        self.setLayout(self.sign_in_layout)
        self.setStyleSheet(open('main.css').read())
        self.sign_in_layout.success_signal.connect(lambda:self.cleanUp())
        self.show()

    #Responsible for removing the widget and its traces, used by pyqt signal after signing in
    def cleanUp(self):
        self.close()
        self.deleteLater()
        
        
        
    
    
            


            
        
        
    