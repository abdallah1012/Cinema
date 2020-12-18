# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:52:02 2020

@author: ojaro
"""

#?? hello ??
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal
class Course(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        