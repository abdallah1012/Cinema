## -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QHBoxLayout, QListWidget, QWidget, QPushButton, QListView, QAbstractItemView
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, Qt, QSize
import math
import base64
from ClickableThumbnail import ClickableThumbnail
#class that implements a widget capable of showing images with title and sliding them with animations right and left for showcasing
class ImageSlider(QWidget):

    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Python ") 
        
        self.setGeometry(1000,1000,2000,100)

        stylesheett= """
            QPushbutton{
            height: 50px;
            width: 50px;
            background-color: rgb(54,57,63);
            background-image: url("./Images/left.png");
            }

            QPushbutton#pic:hover{
            background-color: rgb(54,57,63);
            background-image: url("./Images/left_hover.png");
            }

            QPushbutton#pic2{
            height: 50px;
            width: 50px;
            background-color: rgb(54,57,63);
            background-image: url("./Images/right.png");
            }

            QPushbutton#pic2:hover{
            background-color: rgb(54,57,63);
            background-image: url("./Images/right_hover.png");
            }
        """

        self.setStyleSheet(stylesheett)
        self.hbox = QHBoxLayout() 
        self.list_widget = QListWidget()
        self.items = []
     
        # setting flow 
        self.list_widget.setFlow(QListView.LeftToRight) 
        self.list_widget.setIconSize(QtCore.QSize(190, 190))
        self.list_widget.hasAutoScroll()
        
        self.list_widget.setAutoFillBackground( False )
        
        self.pic = QPushButton()
        self.pic.setObjectName("pic")
        self.pic.clicked.connect(lambda:self.goleftSmooth())

        #use full ABSOLUTE path to the image, not relative
        
        self.hbox.addWidget(self.pic)

        self.hbox.addWidget(self.list_widget)
        
        self.pic2 = QPushButton()
        self.pic2.setObjectName("pic2")
        self.pic2.clicked.connect(lambda:self.gorightSmooth())

        
        self.hbox.addWidget(self.pic2)
        
        self.list_widget.horizontalScrollBar().setDisabled(True);
        self.list_widget.horizontalScrollBar().hide()
        
        self.list_widget.verticalScrollBar().setDisabled(True);
        self.list_widget.verticalScrollBar().hide()
        
        self.list_widget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel);
        
        self.setLayout(self.hbox)
        
        
        self.atCurrentRight = 16
        self.atCurrentLeft = 0
        
        self.timerBaseInterval = 25
        self.floorInterval = 5
        
        self.timer = QTimer(self)
        self.timer.setInterval(self.timerBaseInterval)
        self.timer.timeout.connect(self.goRight)
        
        self.timer2 = QTimer(self)
        self.timer2.setInterval(self.timerBaseInterval)
        self.timer2.timeout.connect(self.goLeft)
        
        self.rightCounter = 0
        self.leftCounter = 0
        
        self.incrementalStep = 1
        self.counterSize = 410
        
        self.lingertime = 1
        self.lingertimeCounter = 0
               
        self.show()
        

    
    #Takes list of images and adds them to the image container of this class
    def setImages(self, images, urls, movieIDs, titles):
        
        self.list_widget.clear()
        self.items = []
        self.list_widget.setViewMode(QListWidget.IconMode)
#        self.list_widget.setResizeMode(QListWidget.Adjust);
#        self.list_widget.setIconSize(QSize(150,150));
#        self.list_widget.setAcceptDrops(True);
#        self.list_widget.setDragEnabled(False);
        for i in range(len(images)):
                self.items.append(ClickableThumbnail(urls[i], movieIDs[i]))
                self.items[i].setText(titles[i])
                
                self.list_widget.addItem(self.items[i])
                
                pm = QPixmap()
                pm.loadFromData(base64.b64decode(images[i]))
                ic = QIcon()
                pm = pm.scaled(QSize(220, 150), Qt.IgnoreAspectRatio);
                ic.addPixmap(pm)
                if(ic.isNull() == False):
                    self.items[i].setIcon(ic)
 
                    
    #movies images to the right to slide left by initiating a timer that moves the images smoothly by pixels
    def goleftSmooth(self):
        self.timer2.start()
        self.pic.setDisabled(True)
        self.pic2.setDisabled(True)
    
    #movies images to the left to slide right by initiating a timer that moves the images smoothly by pixels
    def gorightSmooth(self):
        self.timer.start()
        self.pic.setDisabled(True)
        self.pic2.setDisabled(True)

    #Function that timer2 uses to movie images right
    #It works by modifying the timer interval (time needed until this function is called again) 
    #starts by high time interval to low then to high (slow fast slow)
    def goLeft(self):
        if(self.leftCounter != self.counterSize):
        
            if(self.leftCounter < math.ceil(self.counterSize*0.4)):
                if(self.lingertime > self.lingertimeCounter):
                    
                    self.lingertimeCounter += 1
                    
                else:
                    if(self.timer2.interval() > self.floorInterval):
                        self.timer2.setInterval(self.timer2.interval()-1)
                        self.lingertime = self.timerBaseInterval - self.timer2.interval()
                        self.lingertimeCounter = 5
            elif(self.leftCounter > self.counterSize - math.ceil(self.counterSize*0.4)):
                
                if(self.lingertime > self.lingertimeCounter):
                    
                    self.lingertimeCounter += 1
                    
                else:
                    if(self.timer2.interval() < self.timerBaseInterval):
                        self.timer2.setInterval(self.timer2.interval()+1)
                        self.lingertime = self.timerBaseInterval - self.timer2.interval()
                        self.lingertimeCounter = 5

            
            
            self.list_widget.horizontalScrollBar().setValue(self.list_widget.horizontalScrollBar().value() - self.incrementalStep)
            
            self.leftCounter += 1
      
            self.repaint()
            
            if(self.leftCounter == math.ceil(self.counterSize/2)):
                self.lingertimeCounter  = 5
                self.lingertime = self.timerBaseInterval
            
        else:
            
            self.timer2.setInterval(self.timerBaseInterval)
            self.leftCounter = 0
            self.timer2.stop()
            self.pic.setEnabled(True)
            self.pic2.setEnabled(True)

        if(self.list_widget.horizontalScrollBar().value() == 0):
            self.timer2.setInterval(self.timerBaseInterval)
            self.leftCounter = 0
            self.timer2.stop()
            self.pic.setEnabled(True)
            self.pic2.setEnabled(True)
            
            
    #functions similarly to goLeft but adds scrolls to the right by adding pixels to the scrollbar value rather than subtracting
    #TODO: integrate goleft and goright into 1 function, no need for 2
    def goRight(self):
        
#        print(self.timer.interval())
        if(self.rightCounter != self.counterSize):
        
            if(self.rightCounter < math.ceil(self.counterSize*0.4)):
                if(self.lingertime > self.lingertimeCounter):
                    
                    self.lingertimeCounter += 1
                    
                else:
                    if(self.timer.interval() > self.floorInterval):
                        self.timer.setInterval(self.timer.interval()-1)
                        self.lingertime = self.timerBaseInterval - self.timer.interval()
                        self.lingertimeCounter = 5
            elif(self.rightCounter > self.counterSize - math.ceil(self.counterSize*0.4)):
                
                if(self.lingertime > self.lingertimeCounter):
                    
                    self.lingertimeCounter += 1
                    
                else:
                    if(self.timer.interval() < self.timerBaseInterval):
                        self.timer.setInterval(self.timer.interval()+1)
                        self.lingertime = self.timerBaseInterval - self.timer.interval()
                        self.lingertimeCounter = 5

            
            
            self.list_widget.horizontalScrollBar().setValue(self.list_widget.horizontalScrollBar().value() + self.incrementalStep)
            
            self.rightCounter += 1
      
            self.repaint()
            
            if(self.rightCounter == math.ceil(self.counterSize/2)):
                self.lingertimeCounter  = 5
                self.lingertime = self.timerBaseInterval
            
        else:
            
            self.timer.setInterval(self.timerBaseInterval)
            self.rightCounter = 0
            self.timer.stop()
            self.pic.setEnabled(True)
            self.pic2.setEnabled(True)
            
        if(self.list_widget.horizontalScrollBar().value() == self.list_widget.horizontalScrollBar().maximum()):
            self.timer.setInterval(self.timerBaseInterval)
            self.rightCounter = 0
            self.timer.stop()
            self.pic.setEnabled(True)
            self.pic2.setEnabled(True)

# create pyqt5 app 
#App = QApplication(sys.argv) 
#  
## create the instance of our Window 
#ImageSlider = ImageSlider() 
#  
## start the app 
#sys.exit(App.exec()) 

