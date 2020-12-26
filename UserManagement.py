# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:23:29 2020

@author: WarPeace101
"""
import pandas as pd
from sqlalchemy import create_engine
import base64
#This class is responsible for communicating with the database, mianly with the users table 
#the users table at 12/17/2020 3:51PM contains (userID, username, firstname, lastname, password, entity)

class UserManagement():
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.database_connection = create_engine('mysql+mysqlconnector://root@localhost/cinemadb?'.format('root', '', 'localhost', 'cinemadb'))
        
    #Use this function to check if the username is available or not
    #params: string username (the username to be checked if its already used)
    #returns 1 if username exists and 0 if it doesn't
    def CheckForUsername(self, username):
        sqlstmt = "SELECT * FROM users WHERE username = '"+str(username)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        if(len(df) > 0):
            return 1
        else:
            return 0
    
    #Checks if the username password combo exists
    #params: string username, string password 
    #returns (1, entity, userID) if successful in finding, else returns (0, '', '')
    def CheckForUserPass(self, username, password):
        sqlstmt = "SELECT entity, userID FROM users WHERE username = '"+str(username)+"' AND password = '"+str(password)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        if(len(df) > 0):
            return 1 , df[0][0], str(df[0][1])
        else:
            return 0 , '', ''
        
    
    #Adds row/entry to database table "users"
    #params: string username, string firstname, string lastname, string password, string user
    #returns 1 if successfuly executed and 0 if failed (error comes from database in case its down or SQL syntax error or input error)
    def AddToUsers(self, username, firstname, lastname, password, user):
        #Students have odd userIDs while professors have them even
        #try later to encrypt password
        sqlstmt = "INSERT INTO users(username, firstname, lastname, password, entity) VALUES ('"+str(username)+"', '"+str(firstname)+"', '"+str(lastname)+"', '"+str(password)+"', '"+str(user)+"');"
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            print("Failed")
            return 0
    
    
    def getUserInfo(self, userID):
        sqlstmt = "SELECT username, firstname, lastname, image FROM users WHERE userID = '"+str(userID)+"'"      
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        if(len(df) > 0):
            return df
        else:
            return []
        
    
    def AddToUsersWithImage(self, username, firstname, lastname, password, user, imagePath):
        sqlstmt = "INSERT INTO users(username, firstname, lastname, password, entity, image) VALUES ('"+str(username)+"', '"+str(firstname)+"', '"+str(lastname)+"', '"+str(password)+"', '"+str(user)+"', %s);"
        
        try:
            with open(imagePath, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                image_file.close()
        except:
            return 2 #cant read file
        
        try:
            
            self.database_connection.execute(sqlstmt, encoded_string)
            return 1
        except:
            return 0
    
    
    def giveUserImage(self, userID, imagePath):
        sqlstmt = "UPDATE users SET image = %s WHERE userID = '"+str(userID)+"'"
        try:
            with open(imagePath, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                image_file.close()
        except:
            return 2 #cant read file
        
        try:
            
            self.database_connection.execute(sqlstmt, encoded_string)
            return 1
        except:
            return 0
    
    
    
    