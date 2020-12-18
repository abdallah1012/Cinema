# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:58:22 2020

@author: ojaro
"""

import pandas as pd
from sqlalchemy import create_engine
import re

#class responsible for managing the "movies" database table
#at the time of 12/17/2020 4:25PM the table "movies" contains the columns
#(movieID, moviename, moviecourseID, professorID, description, url, thumbnail)
class MovieManagement:
    def __init__(self):   
       
        #change localhost to IP address and root to username of database
        #This was tested using wampserver
        self.database_connection = create_engine('mysql+mysqlconnector://root@localhost/cinemadb?'.format('root', '', 'localhost', 'cinemadb'))
        
    
    #adds movie to database
    #params: string movieName, int courseID, string description, int userID, string url, 64-byte encoded thumbnail64
    #returns 1 if successfull and 0 and if failed
    def addMovie(self, movieName, courseID, description , userID, url, thumbnail64):

        sqlstmt = "INSERT INTO movies (moviename, moviecourseID, professorID, description, url, thumbnail) VALUES ('"+str(movieName)+"', '"+str(courseID)+"', '"+str(userID)+"', '"+str(description)+"', '"+str(url)+"', %s);"      
        
        try:
            self.database_connection.execute(sqlstmt, thumbnail64)
            return 1
        except:
            return 0
        
    #checks if movie's name is already used by that professor
    #params: string moviename, int userID
    #returns 1 if found, 0 if not
    def CheckForMovieUser(self, moviename, userID):
        
        sqlstmt = "SELECT movieID FROM movies WHERE moviename = '"+str(moviename)+"' AND professorID = '"+str(userID)+"'"
        
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        if(len(df) > 0):
            return 1 
        else:
            return 0 
    
    #gets all thumbnails for all movies present in the movies table in the database
    #returns the thumbnails encoded in BLOB-64 if successfull and 0 if no thumbnails are found
    #TODO: add security layer in case sql execution failed (database error)
    def getThumbNails(self):
        
        sqlstmt = "SELECT thumbnail FROM movies"
        
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        
        if(len(df) == 0):
            return 0 #no thumbnails found
        else:
            return df
        