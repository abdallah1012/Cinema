# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:42:35 2020

@author: WarPeace101
"""

from MovieManagement import MovieManagement
from source import uploadToYoutube
import base64

class MovieInputController:
    def __init__(self):

 
        self.movie_manager = MovieManagement()
        

    def addMovie(self, moviename, courseID, description, userID, url, thumbnail):
        
        try:
            with open(thumbnail, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                image_file.close()
        except:
            return 4 #cant read file
        
        try:      
            exists = self.movie_manager.CheckForMovieUser(moviename, userID)
        except:         
            return 0 #Database error
        
        try:
            videoid = uploadToYoutube(url, moviename, description, thumbnail)
        except:
            return 3 #youtube error
        
        if(exists == 0):         
                result = self.movie_manager.addMovie(moviename, courseID, description, userID, "https://youtu.be/" + videoid['id'], encoded_string)
#                result = self.movie_manager.addMovie(moviename, courseID, description, userID, "test", encoded_string)
                if(result == 1):
                    return 1 #sucessfully added course to database
                else:
                    print("failed to add course")
                    return 0 #database error
        else:
            #TODO: ADD code here that removes the youtube video from youtube since the database failed to insert it
            return 2 #course already exists with user
        