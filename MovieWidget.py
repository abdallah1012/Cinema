import sys
import os.path
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, \
    QVBoxLayout, QAction, QFileDialog, QApplication
import vlc
import pafy 
import threading 
import time 

class MovieWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.url = "https://youtu.be/oHg5SJYRHA0"
        self.setWindowTitle("Movie Player")

        # creating a basic vlc instance
        self.instance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()
        self.isPaused = True
        

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
#        self.moviebox = QVBoxLayout()
#        self.moviebox.addWidget(self.widget)
#        self.widget.setLayout(self.moviebox)
#        print("here")
        
        self.videoframe = QFrame()
        self.palette = self.videoframe.palette()
        self.palette.setColor (QPalette.Window,
                               QColor(0,0,0))
        self.videoframe.setPalette(self.palette)
        self.videoframe.setAutoFillBackground(True)

        self.positionslider = QSlider(Qt.Horizontal, self)
        self.positionslider.setToolTip("Position")
        self.positionslider.setMaximum(1000)
        self.positionslider.sliderMoved.connect(self.setPosition)

        self.hbuttonbox = QHBoxLayout()
        self.playbutton = QPushButton("Play")
        self.hbuttonbox.addWidget(self.playbutton)


        self.stopbutton = QPushButton("Stop")
        self.hbuttonbox.addWidget(self.stopbutton)
        self.stopbutton.clicked.connect(self.Stop)

        self.hbuttonbox.addStretch(1)
        self.volumeslider = QSlider(Qt.Horizontal, self)
        self.volumeslider.setMaximum(100)
        self.volumeslider.setValue(self.mediaplayer.audio_get_volume())
        self.volumeslider.setToolTip("Volume")
        self.hbuttonbox.addWidget(self.volumeslider)
        self.volumeslider.valueChanged.connect(self.setVolume)

        self.vboxlayout = QVBoxLayout()
        self.vboxlayout.addWidget(self.videoframe)
        self.vboxlayout.addWidget(self.positionslider)
        self.vboxlayout.addLayout(self.hbuttonbox)

        self.widget.setLayout(self.vboxlayout)

        self.playbutton.clicked.connect(lambda: self.PlayPause())
        self.stopbutton.clicked.connect(lambda: self.Stop())
        
#        self.show()
        self.resize(640,480)
       
        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateUI)   
#        
#        self.loaded = False
#        self.video = pafy.new(self.url) 
#        
#        self.best = self.video.getbest() 
#            
#        self.media = self.instance.media_new(self.best.url)
#        
#        self.mediaplayer.set_media(self.media)
#        
#        if sys.platform.startswith('linux'): # for Linux using the X Server
#            self.mediaplayer.set_xwindow(self.videoframe.winId())
#        elif sys.platform == "win32": # for Windows
#            self.mediaplayer.set_hwnd(self.videoframe.winId())
#        elif sys.platform == "darwin": # for MacOS
#            self.mediaplayer.set_nsobject(int(self.videoframe.winId()))
            
#        self.OpenFile()

   
 

    def PlayPause(self):
        print("Play Pause")
        if(self.loaded == False):
            
            self.loaded = True     
#            self.OpenFile()

                
        if self.mediaplayer.is_playing():
            
            self.mediaplayer.pause()
            self.playbutton.setText("Play")
            self.isPaused = True
        else:
            
            self.mediaplayer.play()
            self.playbutton.setText("Pause")
            self.timer.start()
            self.isPaused = False

    def Stop(self):
        self.mediaplayer.stop()
        self.playbutton.setText("Play")


    def OpenFile(self, filename=None):
      
        self.video = pafy.new(self.url) 
        self.best = self.video.getbest()
        self.media = self.instance.media_new(self.best.url)
        self.mediaplayer.set_media(self.media)
        
        if sys.platform.startswith('linux'): # for Linux using the X Server
                self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32": # for Windows
                self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin": # for MacOS
                self.mediaplayer.set_nsobject(int(self.videoframe.winId()))
    
        

    def setVolume(self, Volume):
        #Set the volume
        
        self.mediaplayer.audio_set_volume(Volume)

    def setPosition(self, position):        
        # setting the position to where the slider was dragged
        self.mediaplayer.set_position(position / 1000.0)
        # the vlc MediaPlayer needs a float value between 0 and 1, Qt
        # uses integer variables, so you need a factor; the higher the
        # factor, the more precise are the results
        # (1000 should be enough)

    def updateUI(self):
        # setting the slider to the desired position     
        self.positionslider.setValue(self.mediaplayer.get_position() * 1000)

        

