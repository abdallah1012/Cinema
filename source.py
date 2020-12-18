# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:54:58 2020

@author: ojaro
"""


from Google import Create_Service
from googleapiclient.http import MediaFileUpload

#MACRO input variables for API
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
YOUTUBE_DELETE_SCOPE = ["https://www.googleapis.com/auth/youtube.force-ssl", "https://www.googleapis.com/auth/youtube"]


#use this function to upload to youtube
#params: string path, string title, string description, string thumbpath
def uploadToYoutube(path, title, description, thumbpath):
    
    
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    
    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': title,
            'description': description,
            'tags': ['development']
        },
        'status': {
            'privacyStatus': 'unlisted',
    #        'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }
    
#    mediaFile = MediaFileUpload('test23.mp4')
    mediaFile = MediaFileUpload(path)
    
    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

       
    service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload(thumbpath)
    ).execute()
    
    return response_upload

#TODO: this still needs to be fixed
def delete_vid(url):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, YOUTUBE_DELETE_SCOPE)
    service.videos().delete(id=url, onBehalfOfContentOwner=None).execute()

  