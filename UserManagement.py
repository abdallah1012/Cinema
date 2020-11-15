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
        
    def CheckForUsername(self, username):
        sqlstmt = "SELECT * FROM users WHERE username = '"+str(username)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        if(len(df) > 0):
            return 1
        else:
            return 0
    
    def CheckForUserPass(self, username, password):
        sqlstmt = "SELECT entity FROM users WHERE username = '"+str(username)+"' AND password = '"+str(password)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        if(len(df) > 0):
            return 1 , df[0][0]
        else:
            return 0 , ''
        
    
    def AddToUsers(self, username, firstname, lastname, password, user):
        
        #try later to encrypt password
        sqlstmt = "INSERT INTO users VALUES ('"+str(username)+"', '"+str(firstname)+"', '"+str(lastname)+"', '"+str(password)+"', '"+str(user)+"');"
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0
    
    
    
    
    
    
    
    
    
    