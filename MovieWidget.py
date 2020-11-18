# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 09:49:33 2020

@author: ojaro
"""
from PyQt5.QtWidgets import QWidget,QMainWindow
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer,QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget
import time
import pafy
import vlc
class MovieWidget(QWidget):
    def __init__(self):
        self.url = "https://youtu.be/oHg5SJYRHA0"
        super().__init__()
  
  
        self.video = pafy.new(self.url) 
        self.best = self.video.getbest() 
        self.media = vlc.MediaPlayer(self.best.url) 
        self.media.play()
        time.sleep(10)
        self.media.stop()
        self.show()
