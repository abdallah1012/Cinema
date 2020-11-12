# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:54:51 2020

@author: ojaro
"""
from abc import ABCMeta, abstractmethod

    
class User:
    __metclass__ = ABCMeta 
    
    def __init__(self):
        pass
    
    @abstractmethod    
    def LoadDashboardInfo(self):
        raise NotImplementedError("Must override ViewDashboard")
    
    
        
    