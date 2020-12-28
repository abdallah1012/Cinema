# -*- coding: utf-8 -*-


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
    def addMovie(self, movieName, courseID, description , userID, url, thumbnail64, tag1, tag2, tag3, style):

        sqlstmt = "INSERT INTO movies (moviename, moviecourseID, professorID, description, url, tag1, tag2, tag3, style, views, thumbnail) VALUES ('"+str(movieName)+"', '"+str(courseID)+"', '"+str(userID)+"', '"+str(description)+"', '"+str(url)+"','"+str(tag1)+"','"+str(tag2)+"','"+str(tag3)+"','"+str(style)+"','"+str(0)+"', %s);"      
        
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
        
    def getThumbNailsURL(self):
        
        sqlstmt = "SELECT thumbnail, url, movieID, moviename FROM movies"
        
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        
        if(len(df) == 0):
            return 0 #no thumbnails found
        else:
            return df
    def getThumbNailsMovieID(self,movieID):
        
        sqlstmt = "SELECT thumbnail, url, movieID, moviename FROM movies WHERE movieID = '"+str(movieID)+"'"
        
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        
        if(len(df) == 0):
            return 0 #no thumbnails found
        else:
            return df
        

    def getCourseMovies(self,C_ID):
        sqlstmt = "SELECT moviename, thumbnail, url, movieID FROM movies WHERE moviecourseID = '"+str(C_ID)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        if(len(df) == 0):#no movies found for course
            return []
        else:
            return df
    def getCourseMovieID(self,C_ID):
        sqlstmt= "SELECT movieID, tag1, tag2, tag3 FROM movies WHERE moviecourseID = '"+str(C_ID)+"'"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        if(len(df) == 0):#no movies found for course
            return []
        else:
            return df
        

    def incrementViewsByURL(self,url):
            sqlstmt = "UPDATE movies SET views = views +1 WHERE url = '" +str(url) +"'"
            try:
                self.database_connection.execute(sqlstmt)
                return 1
            except:
                return 0
            
    def submitComment(self, movieID, comment, user):
        sqlstmt = "INSERT INTO comments (movieID, comment, username) VALUES ('"+str(movieID)+"', '"+str(comment)+"', '"+str(user)+"');"
        try:
            self.database_connection.execute(sqlstmt)
            return 1
        except:
            return 0
        

        
    def getComments(self, movieID):
        
        sqlstmt = "SELECT comment, username FROM comments WHERE movieID = '"+str(movieID)+"'"
        
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        if(len(df) > 0):
            return df
        else:
            return []
        
        
        
    def getWhatHot(self):
        sqlstmt = "SELECT movieID AS movieID FROM movies ORDER BY views DESC LIMIT 5"
        df = pd.read_sql_query(sqlstmt, self.database_connection)
        df = df.values.tolist()
        
        if(len(df) > 0):
            return df
        else:
            return []