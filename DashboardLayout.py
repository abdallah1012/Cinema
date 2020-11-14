# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:42:37 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QGridLayout,QLabel,QWidget

class DashboardLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.__dashboard_grid = QGridLayout()
        self.temp_label = QLabel("Dashboard tab clicked")
        self.__dashboard_grid.addWidget(self.temp_label)
        self.setLayout(self.__dashboard_grid)