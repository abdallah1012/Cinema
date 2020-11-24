# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:54:58 2020

@author: ojaro
"""

import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

def uploadToYoutube(path):
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
#    upload_date_time = datetime.datetime(2019, 12, 25, 12, 30, 0).isoformat() + '.000Z'
    
    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': 'Testing HOw api works',
            'description': 'Larger upload',
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

    #response_upload.getId()    
    #service.thumbnails().set(
    #    videoId=response_upload.get('id'),
    #    media_body=MediaFileUpload('thumbnail.jpg')
    #).execute()
    
    return response_upload
