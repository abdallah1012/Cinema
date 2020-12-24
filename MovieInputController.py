# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:42:35 2020

@author: WarPeace101
"""

from MovieManagement import MovieManagement
from source import uploadToYoutube
import base64

#controller for the relevant layout to allow communication with other layouts and computation models
class MovieInputController:
    def __init__(self):

 
        self.movie_manager = MovieManagement() #manager to allow communication with movie management model
        

    #talks to movie manager to add movie to database and to youtube
    #transforms first thumbnail to base64, then checks if movie is already uploaded by user, then tries uploading to youtube, if sucessfull then it uploads relevant data to database
    #params: string moviename, int courseID, string description, int userID, string url (path to movie), string thumbnail (path to thumbnail)
    #returns 0 for database errors, 1 if sucessfull, 2 if movie already exists, 3 if error with youtube api, 4 if movie can't be found
    def addMovie(self, moviename, courseID, description, userID, url, thumbnail, tag1, tag2, tag3, style):
        
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
#            videoid = 999
        except:
            return 3 #youtube error
        
        if(exists == 0):         
                result = self.movie_manager.addMovie(moviename, courseID, description, userID, "https://youtu.be/" + videoid['id'], encoded_string, tag1, tag2, tag3, style)
#                result = self.movie_manager.addMovie(moviename, courseID, description, userID, "test", encoded_string, tag1, tag2, tag3, style)
                print(result)
                if(result == 1):
                    return 1 #sucessfully added course to database
                else:
                    print("failed to add Movie")
                    return 0 #database error
        else:
            #TODO: ADD code here that removes the youtube video from youtube since the database failed to insert it
            return 2 #movie  already exists with user
        