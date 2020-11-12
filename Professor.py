# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:20:16 2020

@author: ojaro
"""
from User import User

class Professor(User):
    def __init__(self,ID:int):
        super().__init__()
        
    def UploadMovie(self):
        pass
    def CreateCourse(name:str,description:str,prerequisites:list):
        pass
    def LoadDashboardInfo(self):
        print("Prof views dashboard")