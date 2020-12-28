# -*- coding: utf-8 -*-


#?? hello ??
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSignal
class Course(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        