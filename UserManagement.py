# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:23:29 2020

@author: WarPeace101
"""
import pandas as pd
from sqlalchemy import create_engine

class UserManagement():
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.database_connection = create_engine('mysql+mysqlconnector://root@localhost/cinemadb?'.format('root', '', 'localhost', 'cinemadb'))
        
    def CheckForUsername(self, sqlstmt):
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        if(len(df) > 0):
            return 1
        else:
            return 0
    
    def CheckForUserPass(self, sqlstmt):
        pass
    
    def AddToUsers(self, sqlstmt):
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0
    
    
    
    
    
    
    
    
    
    