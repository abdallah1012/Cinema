import sys
import os.path
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, \
    QVBoxLayout, QAction, QFileDialog, QApplication, QMessageBox, QPlainTextEdit, QLabel, QScrollArea, QTextEdit
import vlc
import pafy 
import threading 
import time 
from MovieController import MovieController
from Professor import Professor

#layout for presenting a movie with all navigation features
class MovieLayout(QWidget):

    def __init__(self, url, movieID, user):
        super().__init__()
        self.controller = MovieController(url)
        self.url = url
        self.user = user
        self.setWindowTitle("Movie Player")
        self.movieID = movieID
        # creating a basic vlc instance
        self.instance = vlc.Instance()
        # creating an empty vlc media player
        self.mediaplayer = self.instance.media_player_new()
        self.isPaused = True
        

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
        self.playbutton = QPushButton()
        self.playbutton.setObjectName("playbutton")
        self.hbuttonbox.addWidget(self.playbutton)
        
        
        result = self.controller.isMovieForUser(self.movieID, self.user.id)
        if(isinstance(self.user, Professor) == True and len(result) > 0):
            self.numberofViews = result[0][1]
            self.description = result[0][0]
            self.numofLikes = result[0][2]
            self.infoButton = QPushButton("Statistics")            
            self.hbuttonbox.addWidget(self.infoButton)
            self.infoButton.clicked.connect(lambda: self.openStats())

        self.stopbutton = QPushButton()
        self.stopbutton.setObjectName("stopbutton")
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

        
        status = self.controller.getLikeStatus(self.movieID, self.user.id)
        if(status == 0):
            self.likeButton = QPushButton("Like")
        else:
            self.likeButton = QPushButton("DisLike")
        
        
        self.likeButton.clicked.connect(lambda: self.LikeDislike())
        self.comment = QPlainTextEdit()
        self.likehbox = QHBoxLayout()
        self.comment.setPlaceholderText("Type Comment Here ...")
        self.comment.setObjectName("comment")
        self.comment.setFixedHeight(50)
        self.commentbox = QVBoxLayout()        
        self.commentSubmit = QPushButton("Comment")
        self.commentSubmit.setObjectName("commentSubmit")
        self.commentSubmit.setFixedWidth(200)
        self.commentSubmit.clicked.connect(lambda: self.submitComment())
        self.commentbox.addWidget(self.comment)
        self.likehbox.addWidget(self.commentSubmit)
        self.likehbox.addWidget(self.likeButton)
        self.commentbox.addLayout(self.likehbox)
        
        self.commentSection = QLabel("Comments:")
        self.commentSection.setFixedHeight(50)
        self.commentSection.setObjectName("commentSection")
        self.commentSection.setFixedHeight(30)
        self.commentbox.addWidget(self.commentSection)
        self.commentSection_comments = QTextEdit("No Comments Yet")
        self.commentSection_comments.setObjectName("commentSection_comments")
        self.commentSection_comments.setReadOnly(True)
        self.commentSection_comments.setFixedHeight(50)
        
        self.commentbox.addWidget(self.commentSection_comments)
        self.vboxlayout.addLayout(self.commentbox)
        
        
        self.setLayout(self.vboxlayout)
        self.playbutton.clicked.connect(lambda: self.PlayPause())
        self.stopbutton.clicked.connect(lambda: self.Stop())

        self.resize(640,480)
       
        self.timer = QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateUI)   
        
        self.stats = None
        
        self.loaded = False
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
            
        
        self.LoadComments()

    def openStats(self):
        if(self.stats != None):
            del self.stats
        
        result = self.controller.isMovieForUser(self.movieID, self.user.id)
        if(isinstance(self.user, Professor) == True and len(result) > 0):
            self.numberofViews = result[0][1]
            self.description = result[0][0]
            self.numofLikes = result[0][2]
        
        self.stats = self.controller.openStatsLayout(self.numberofViews, self.description, self.numofLikes)
        self.stats.show()
        
    def LikeDislike(self):
        if(self.likeButton.text() == "DisLike"):
            self.controller.removieLike(self.movieID, self.user.id)
            self.likeButton.setText("Like")
        elif(self.likeButton.text() == "Like"):
            self.controller.LikeMovie(self.movieID, self.user.id)
            self.likeButton.setText("DisLike")
            
    
    def submitComment(self):
        if(self.comment.toPlainText() != ""):
            result = self.controller.submitComment(self.movieID, self.comment.toPlainText(), self.user.username)
            if(result == 1):
                self.commentSection_comments.setPlainText(self.user.username + ": " + self.comment.toPlainText() + "\n" + self.commentSection_comments.toPlainText())
                self.comment.setPlainText("") 
    
    
    def LoadComments(self):
        comments = self.controller.getComments(self.movieID)
        comment = ""
        for i in comments:
            comment += i[1] + ": " + i[0] + "\n"
        self.commentSection_comments.setPlainText(comment)
 
    #Plays and pauses the movie, same button changes status from play to pause
    def PlayPause(self):
        print("Play Pause")
        if(self.loaded == False):     
            self.loaded = True     

        if self.mediaplayer.is_playing():
            
            self.mediaplayer.pause()
            #self.playbutton.setText("Play")
            self.isPaused = True
        else:
            
            self.mediaplayer.play()
            #self.playbutton.setText("Pause")
            self.timer.start()
            self.isPaused = False

    #stops the movie, unloads it, pressing this requires loading the movie again
    def Stop(self):
        self.mediaplayer.stop()
        #self.playbutton.setText("Play")

    #Opens the movie from youtube and sets it in the appropriate layout item to be showcased
    #TODO: add and use param (string youtube_url) 
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
    
        
    #Changes the volume of the media player
    def setVolume(self, Volume):
        #Set the volume 
        self.mediaplayer.audio_set_volume(Volume)

    #Sets the position of the video slider, responsible for going to different times in the movie
    def setPosition(self, position):        
        # setting the position to where the slider was dragged
        self.mediaplayer.set_position(position / 1000.0)
        # the vlc MediaPlayer needs a float value between 0 and 1, Qt
        # uses integer variables, so you need a factor; the higher the
        # factor, the more precise are the results
        # (1000 should be enough)

    #function used by timer to keep the movie's time slider indicator in the right position
    def updateUI(self):
        # setting the slider to the desired position     
        self.positionslider.setValue(self.mediaplayer.get_position() * 1000)





#Initiator
def run():
    app = QApplication(sys.argv)
    welcome_widget = MovieLayout("https://www.youtube.com/watch?v=LeYsRMZFUq0&t=6s",1)
    welcome_widget.show()
    sys.exit(app.exec_())
   
	
#if __name__ == '__main__':
#   run()
