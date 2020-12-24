# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:13:48 2020

@author: warpeace101
"""
from PyQt5.QtWidgets import  QListWidgetItem

class ClickableThumbnail(QListWidgetItem):
    
    def __init__(self, url):
        super().__init__()
        
        self.url = url
        
    def itemPressed(self):
        print("here")
        print(self.url)
        

    
    
    