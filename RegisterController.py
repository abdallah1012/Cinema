# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 11:34:50 2020

@author: WarPeace101
"""

from sqlalchemy import create_engine
import pandas as pd
import WelcomeWidget


class RegisterController:
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.database_connection = create_engine('mysql+mysqlconnector://root@localhost/cinemadb?'.format('root', '', 'localhost', 'cinemadb'))
        
    
    def CheckUserExists(self, username):
        sqlstmt = "SELECT * FROM users WHERE username = '"+str(username)+"'"
        
        
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        if(len(df) > 0):
            return 1
        else:
            return 0
    
    def RegisterUser(self, username, firstname, lastname, password, user):
        #try later to encrypt password
        
        sqlstmt = "INSERT INTO users VALUES ('"+str(username)+"', '"+str(firstname)+"', '"+str(lastname)+"', '"+str(password)+"', '"+str(user)+"');"
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0
        
    
    def goBack(self):
        
        
        Signin = WelcomeWidget.WelcomeWidget()
        Signin.show()
        
        return "success"
        
        
        
        
        
        
        